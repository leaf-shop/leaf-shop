FROM python:alpine

WORKDIR /backend
COPY . .
RUN apk --no-cache add gcc musl-dev linux-headers
RUN pip install -r requirements.txt
EXPOSE 8000/tcp
