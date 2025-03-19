FROM alpine:3.18

RUN apk -U --no-progress --no-cache upgrade \
 && apk -U --no-progress --no-cache add busybox bash sudo curl git python3 py3-pip py3-flask py3-requests socat py3-curl \
 && git clone https://github.com/iwojim0/net-uptime.git \
 && pip install tcp-latency icmplib --break-system-packages \
 && chmod +x /net-uptime/*.sh

COPY *.json /net-uptime/config/
COPY *.png /net-uptime/static/

USER root
WORKDIR /net-uptime

ENTRYPOINT [ "./start.sh" ]

