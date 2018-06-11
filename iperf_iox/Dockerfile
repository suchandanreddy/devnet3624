FROM alpine:3.3
 
RUN apk add --update iperf
 
LABEL \
 cisco.type=lxc \
 cisco.resources.network.0.interface-name="eth0" \
 cisco.cpuarch=x86_64 \
 cisco.kernel-version="4.4.51" \
 cisco.resources.profile="custom" \
 cisco.resources.cpu="1000" \
 cisco.resources.memory="1000" \
 cisco.resources.disk="2" \
 cisco.startup.target="/bin/sh"
