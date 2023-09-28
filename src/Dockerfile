FROM ubuntu:22.04

# APL network configuration from
# https://aplprod.servicenowservices.com/sp?id=kb_article&sys_id=c0de6fe91b83d85071b143bae54bcb34
RUN apt-get update && apt-get install -y ca-certificates curl && \
    (curl -svL http://apllinuxdepot.jhuapl.edu/linux/APL-root-cert/JHUAPL-MS-Root-CA-05-21-2038-B64-text.cer -o /usr/local/share/ca-certificates/JHUAPL-MS-Root-CA-05-21-2038-B64-text.crt || true) && \
    update-ca-certificates
ENV PIP_CERT=/etc/ssl/certs/ca-certificates.crt


RUN apt-get update && apt-get install -y \
    python3 python3-pip

COPY requirements.txt *.py /usr/local/src/demo/
WORKDIR /usr/local/src/demo
RUN pip3 install -r requirements.txt
