FROM python:3.11-alpine as base

RUN apk add git
RUN git clone --branch docker https://github.com/Jim137/TwASAP.git
RUN pip install -r /TwASAP/requirements.txt

WORKDIR /

#########
# Prod  #
#########
FROM python:3.11-alpine

RUN apk add --no-cache bash && \
    rm -rf /var/cache/apk/*

COPY --from=base /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=base /TwASAP /TwASAP

ADD /Docker/setup.sh /TwASAP/
ADD /Docker/exec.sh /TwASAP/

WORKDIR /TwASAP
ENTRYPOINT ["/bin/bash", "setup.sh"]
CMD []
