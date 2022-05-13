# production
FROM nginx:stable-alpine

WORKDIR /app
RUN apk add --no-cache py3-bcrypt py3-cffi py3-pip python3 && \
    pip3 install --no-cache-dir flask python-dotenv mysql-connector-python flask-cors flask-jwt-extended gunicorn && \
    mkdir /tmp/gsock
COPY ./web/dist /usr/share/nginx/html
COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf
COPY ./api .
CMD gunicorn --bind 127.0.0.1:5000 --daemon wsgi:app && \
    nginx -g 'daemon off;'
