FROM centos:7

USER root

RUN yum install -y epel-release && \
sed -i -e 's/keepcache=0/keepcache=1/g' /etc/yum.conf && \
yum install -y gcc && \
yum install -y python-devel && \
yum install -y mysql-devel && \
yum install -y python-pip && \
pip install --upgrade pip && \
pip install fabric && \
pip install MySQL-python


