FROM nginxinc/nginx-unprivileged:1-alpine
LABEL maintainer="fumex9910@gmail.com"

COPY ./default.conf.tpl /etc/nginx/default.conf.tpl
COPY ./uwsgi_params /etc/nginx/uwsgi_params
COPY ./run.sh /run.sh

ENV LISTEN_PORT=8000
ENV APP_HOST=app
ENV APP_PORT=9000

USER root

# RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers zlib-dev jpeg-dev && apk add libjpeg && pip install Pillow --no-cache-dir && apk del .tmp

RUN mkdir -p /vol/static && \
    chmod 775 /vol/static && \
    touch /etc/nginx/conf.d/default.conf && \
    chown nginx:nginx /etc/nginx/conf.d/default.conf && \
    chmod +x /run.sh

VOLUME /vol/static

USER nginx

CMD ["/run.sh"]