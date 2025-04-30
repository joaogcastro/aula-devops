FROM alpine:latest

RUN apk add --no-cache curl bash

WORKDIR /test

COPY test.sh .

RUN chmod +x test.sh

CMD ["./test.sh"]
