FROM bentoml/model-server:0.11.0-py36
MAINTAINER ersilia

RUN conda install -c rdkit rdkit=2017.09.1 -y
RUN python -m pip install tensorflow==1.6.0
RUN python -m pip install numpy==1.19.2

WORKDIR /repo
COPY . /repo
