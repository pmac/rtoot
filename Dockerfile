FROM quay.io/deis/base:0.3.0
CMD ["nginx"]

RUN apt-get update && \
    apt-get install -y --no-install-recommends nginx

COPY nginx.conf /etc/nginx/nginx.conf
COPY build/ /usr/share/nginx/html
