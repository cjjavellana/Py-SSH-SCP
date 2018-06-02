FROM centos:7

USER root

RUN yum install -y epel-release 
yum install -y gcc && \
yum install -y python-devel && \
yum install -y mysql-devel && \
yum install -y python-pip && \
pip install --upgrade pip && \
mkdir -p /app/deploy && \
mkdir -p /tmp/workdir

ADD src/logging.yaml /app/deploy
ADD src/pyscp.py /app/deploy
ADD src/scpcopy.py /app/deploy
ADD src/httpuploader.py /app/deploy


