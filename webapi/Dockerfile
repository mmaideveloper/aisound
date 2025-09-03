# Use Miniconda as base image
FROM continuumio/miniconda3

# Set working directory
WORKDIR /app

# Copy environment.yml first to leverage Docker layer caching
COPY environment.yml .

COPY .env .

# Update conda and install specific version
#ENV CONDA_PKGS_DIRS=/opt/conda/pkgs

#RUN conda install -n base -c defaults conda=25.7.0
ENV CONDA_TOS_ACCEPT=true
#clean
RUN conda clean --all --yes
# Create the Conda environment
RUN conda update -n base -c defaults conda && \
    conda env create -f environment.yml

# Activate the environment by default
SHELL ["conda", "run", "-n", "aisound-env", "/bin/bash", "-c"]

# Copy the rest of your application code
COPY . .

# Expose the port FastAPI will run on
EXPOSE 8000

# Run the FastAPI app using Uvicorn
CMD ["conda", "run", "-n", "aisound-env", "uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]


