FROM ubuntu:16.04
MAINTAINER Tamas Kalman <ktamas77@gmail.com>

ENV DEBIAN_FRONTEND noninteractive
ENV TERM xterm

RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get -y install iputils-ping net-tools ntp locales
RUN apt-get -y install wget mc nano telnet man

ENV LANG=en_US.UTF-8
RUN locale-gen en_US.UTF-8 && update-locale LANG=en_US.UTF-8

RUN apt-get -y install python
RUN apt-get -y install python-pip
RUN pip install --upgrade pip
RUN pip install flask flask-jsonpify flask-restful requests pyyaml

CMD flask run --host=0.0.0.0 --port=5000