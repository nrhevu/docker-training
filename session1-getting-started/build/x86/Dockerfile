FROM --platform=linux/amd64 ubuntu:22.04

# RUN apt-get update && apt-get install -y build-essential
RUN apt-get update && apt-get install -y wget

# Install miniconda
ENV CONDA_DIR=/opt/conda
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/conda && rm ~/miniconda.sh

# Put conda in path so we can use conda activate
ENV PATH=$CONDA_DIR/bin:$PATH

RUN pip install fastapi uvicorn && conda clean -ay

COPY . /app
WORKDIR /app

CMD ["python", "test.py"]