From ubuntu:18.04

WORKDIR /root/

COPY requirement first/ ./

RUN pwd \
    && apt-get update \
    && apt-get install -y vim nginx mongodb supervisor python3-pip \
    && pip3 install -r requirement.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/
    && rm -rf /var/lib/apt/lists/*


