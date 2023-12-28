FROM nginx:alpine
RUN mkdir /etc/nginx/sites-available
COPY ./sites-available/default  /etc/nginx/sites-available/
CMD ["nginx", "-g", "daemon off;"]