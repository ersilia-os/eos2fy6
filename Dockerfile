FROM bentoml/model-server:0.11.0-py38
MAINTAINER ersilia

RUN pip install rdkit-pypi==2022.9.5 scikit-learn==0.24.2
RUN pip install xgboost==1.4.1

WORKDIR /repo
COPY . /repo
