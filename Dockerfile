FROM ubuntu:22.04 as base

COPY . /mplop_sem2_final

WORKDIR /mplop_sem2_final

EXPOSE 8003

RUN apt-get update &&\
    apt-get install -y python3 python3-pip &&\
    apt-get update &&\
    pip install -r requirements.txt

CMD cd src &&\
    uvicorn main:app --host 0.0.0.0 --port 8004
