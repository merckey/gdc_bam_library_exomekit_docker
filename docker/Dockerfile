FROM ubuntu:xenial-20161010

MAINTAINER Jeremiah H. Savage <jeremiahsavage@gmail.com>

ENV version 0.1

RUN apt-get update \
    && apt-get install -y \
       python3-pip \
    && apt-get clean \
    && pip3 install gdc_bam_library_exomekit_docker \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
