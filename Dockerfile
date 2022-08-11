FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN sudo apt update
RUN sudo apt install python3.6

RUN conda create -n eos5qfo_py36 python=3.6 -y
RUN conda install -n eos5qfo_py36 -c rdkit rdkit=2017.09.1 -y
RUN python3.6 -m pip install tensorflow==1.6.0
RUN python3.6 -m pip install numpy==1.19.2

WORKDIR /repo
COPY . /repo
