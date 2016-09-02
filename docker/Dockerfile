FROM alpine:3.4

MAINTAINER Jeremiah H. Savage <jeremiahsavage@gmail.com>

RUN apk add --update \
        ca-certificates \
        openssl \
    && update-ca-certificates \
    && cd /usr/local/share \
    && wget https://github.com/jeremiahsavage/gdc_bam_library_exomekit_docker/raw/master/bam_libraryname_capturekey.json \
    && cd -