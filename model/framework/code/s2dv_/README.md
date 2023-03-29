# S2DV HepG2 toxicity


Code for "S2DV HepG2 toxicity: A Strategy for Prediction of liver toxicity of potential compounds, verified by wet-lab experiments."

# Requirements
- python 3.7
- scikit-learn==0.24.2
- xgboost==1.4.1
- rdkit==2022.9.4

# Model
The S2DV HepG2 toxicity model was saved in the "model" folder.

# Prediction of liver toxicity of potential compounds
1. Create a conda environment:
`conda create -n nameofenv python=3.7`
2. Activate conda environment:
`conda activate nameofenv`
3. Install dependencies.<br>
`pip install scikit-learn==0.24.2`<br>
`pip install xgboost==1.4.1`<br>
`pip install rdkit==2022.9.4`<br>
4. cd `model/framework/code`
2. Run `python main.py ../<name_of_input_file>.csv ../<name_of_output_file>.csv`