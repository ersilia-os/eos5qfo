FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN conda create -n eos5qfo_py36 python=3.6
RUN conda install -n eos5qfo_py36 -c rdkit rdkit=2017.09.1
RUN pip install tensorflow==1.6.0
RUN pip install numpy==1.19.2

WORKDIR /repo
COPY . /repo
