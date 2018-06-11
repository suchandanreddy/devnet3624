FROM alpine:3.3
 
RUN apk add --update iperf
 
LABEL \
 cisco.resources.network.0.interface-name="eth0" \
 cisco.cpuarch=x86_64 \
 cisco.resources.profile="custom" \
 cisco.resources.cpu="1000" \
 cisco.resources.memory="1000" \
 cisco.startup.target="/bin/sh"
