

FROM ubuntu:latest

LABEL maintainer="Sachin Sudhakar Shetty <ssshetty@campus.uni-paderborn.de>"

RUN \
    export DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
    --reinstall ca-certificates \
    build-essential \
    software-properties-common \
    wget \
    vim \
    git-core \
    ssh-client \
    make \
    cmake \
    systemd 

#Install python3
RUN add-apt-repository --yes ppa:deadsnakes/ppa
RUN apt-get install -y \
    --no-install-recommends \
    python3.8 \
    python3.8-venv \
    python3-pip

# install libraries
RUN pip install aiohttp[speedups]

RUN mkdir /usr/local/share/ca-certificates/cacert.org && \
    wget -P /usr/local/share/ca-certificates/cacert.org http://www.cacert.org/certs/root.crt http://www.cacert.org/certs/class3.crt && \
    update-ca-certificates && \
    git config --global http.sslCAinfo /etc/ssl/certs/ca-certificates.crt

ENV RPISTATUS=False
ENV WD_DIR=/usr/local/src/evio

WORKDIR /usr/local/src/evio

COPY . /usr/local/src/evio 

# Docker image standalone
CMD /usr/local/src/evio/script/standalone_docker.sh
