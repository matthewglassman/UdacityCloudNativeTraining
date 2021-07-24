FROM golang:alpine
WORKDIR /go/src/app
COPY . /go/src/app
RUN go mod init
RUN go build -o helloworld
EXPOSE 6111
CMD ["/go/src/app/helloworld"]