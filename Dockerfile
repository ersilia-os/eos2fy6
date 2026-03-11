FROM bentoml/model-server:0.11.0-py38
MAINTAINER ersilia

RUN conda install -c conda-forge scikit-learn==0.24.2 rdkit==2022.09.4
RUN pip install xgboost==1.4.1

WORKDIR /repo
COPY . /repo
