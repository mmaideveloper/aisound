param containerAppName string
param location string = resourceGroup().location
param containerEnv string
param logAnalyticsName string = 'log-${uniqueString(resourceGroup().id)}'
param acrName string 
param imageName string

resource acr 'Microsoft.ContainerRegistry/registries@2023-01-01-preview' = {
  name: acrName
  location: location
  sku: {
    name: 'Basic'
  }
  properties: {
    adminUserEnabled: true
  }
}

output acrLoginServer string = acr.properties.loginServer
var acrCreds = listCredentials(acr.id, acr.apiVersion)
output acrUsername string = acrCreds.username

resource logAnalytics 'Microsoft.OperationalInsights/workspaces@2022-10-01' = {
  name: logAnalyticsName
  location: location
  properties: {
    sku: {
      name: 'PerGB2018'
    }
    retentionInDays: 30
    publicNetworkAccessForIngestion: 'Enabled'
    publicNetworkAccessForQuery: 'Enabled'
  }
}

output logAnalyticsWorkspaceId string = logAnalytics.id


resource env 'Microsoft.App/managedEnvironments@2023-05-01' = {
  name: '${containerEnv}-env'
  location: location
  properties: {
    appLogsConfiguration: {
      destination: 'log-analytics'
      logAnalyticsConfiguration: {
        customerId: logAnalytics.properties.customerId
        sharedKey: listKeys(logAnalytics.id, logAnalytics.apiVersion).primarySharedKey
      }
    }
  }
}

resource app 'Microsoft.App/containerApps@2023-05-01' = {
  name: containerAppName
  location: location
  properties: {
    managedEnvironmentId: env.id
    configuration: {
      ingress: {
        external: true
        targetPort: 8000
      }
      registries: [
        {
          server: acr.properties.loginServer
          username: acrCreds.username
          passwordSecretRef: 'acr-password'
        }
      ]
      secrets: [
        {
          name: 'acr-password'
          value: acrCreds.passwords[0].value
        }
      ]
    }
    template: {
      containers: [
        {
          name: containerAppName
          image: '${imageName}'
        }
      ]
    }
  }
}
