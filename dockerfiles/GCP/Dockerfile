FROM us-docker.pkg.dev/inductive-cocoa-378409/kohya-ss/base:latest
COPY . .
STOPSIGNAL SIGINT
RUN aws configure set region us-east-1
RUN aws configure set output json
RUN install -o root -g root -m 0755 /app/bin/kubectl /usr/local/bin/kubectl
ENV LD_PRELOAD=libtcmalloc.so