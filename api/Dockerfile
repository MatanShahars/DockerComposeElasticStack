FROM alpine:3.14.0
ADD api /usr/local/bin/api
RUN apk add --no-cache curl
ADD remote_ip_visualization.ndjson /usr/local/bin/remote_ip_visualization.ndjson
RUN chmod 777 /usr/local/bin/api
RUN chmod 777 /usr/local/bin/remote_ip_visualization.ndjson
CMD /usr/local/bin/api