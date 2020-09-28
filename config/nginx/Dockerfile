# Use an official node runtime as a parent image
FROM nginx:1.17

COPY config/nginx/service.conf /etc/nginx/nginx.conf
ADD ./media usr/share/nginx/html/media/
ADD ./static static/
