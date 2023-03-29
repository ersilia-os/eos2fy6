FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN pip install scikit-learn==0.24.2
RUN pip install xgboost==1.4.1
RUN pip install rdkit==2022.9.4

WORKDIR /repo
COPY . /repo
