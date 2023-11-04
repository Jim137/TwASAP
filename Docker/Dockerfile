FROM python:3.11-slim

RUN git clone https://github.com/Jim137/TwASAP.git
RUN git checkout docker
# COPY . /TwASAP/
ADD Docker/setup.sh /TwASAP/
ADD Docker/exec.sh /TwASAP/
RUN cd /TwASAP
WORKDIR /TwASAP
RUN pip install -r requirements.txt

ENTRYPOINT ["/bin/bash", "setup.sh"]
CMD []
