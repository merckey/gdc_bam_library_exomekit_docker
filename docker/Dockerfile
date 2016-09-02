FROM alpine:3.4

MAINTAINER Jeremiah H. Savage <jeremiahsavage@gmail.com>

RUN apk add --update \
        bash \
        ca-certificates \
        git \
        openssl \
        python3 \
    && update-ca-certificates \
    && rm -rf /var/cache/apk/* \
    && cd /usr/local/share \
    && git clone https://github.com/jeremiahsavage/gdc_bam_library_exomekit_docker.git \
    && mv gdc_bam_library_exomekit_docker/*.json ./ \
    && mv gdc_bam_library_exomekit_docker/intervals ./ \
    && rm -rf gdc_bam_library_exomekit_docker \
    && cd -