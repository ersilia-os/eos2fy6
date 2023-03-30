# imports
import csv
import sys
import pickle as pkl
import os
from rdkit import Chem
from rdkit.Chem import AllChem
import numpy as np

#then import my	own	modules
from s2dv_.s2dv_modular import get_ECFP, mol2alt_sentence, get_sentence_vec, vec_predict

#parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))
# checkpoints directory
checkpoints_dir = os.path.abspath(os.path.join(root, "..", "..", "checkpoints"))


def main(smiles):   
    mol = Chem.MolFromSmiles(smiles)  
    
    if len(get_ECFP(mol, 1)) != 0:
        # return ECFP
        ECFP = get_ECFP(mol, 1)
        
        HepG2_model = pkl.load(
            open(os.path.join(checkpoints_dir, 'HepG2.ECFP.models.pkl'), 'rb+'))
        HepG2_token = pkl.load(
            open(os.path.join(checkpoints_dir, 'HepG2_token.pkl'), 'rb+'))
        HepG2_emb = pkl.load(
            open(os.path.join(checkpoints_dir, 'HepG2_emb.pkl'), 'rb+'))

        if (np.isfinite(get_sentence_vec(ECFP, HepG2_emb, HepG2_token)).any()): 
            HepG2_vec = get_sentence_vec(ECFP, HepG2_emb, HepG2_token)     
            HepG2_prob_predict = vec_predict(HepG2_vec, HepG2_model, 'SVM')
            return HepG2_prob_predict
        else:
            HepG2_prob_predict = [""]
            return HepG2_prob_predict
    else:
        HepG2_prob_predict = [""]
        return HepG2_prob_predict


with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["HepG2_toxicity_prob_predict"])  # header

with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]
    for smiles in smiles_list:
        output = main(smiles)
        with open(output_file, "a") as f:
            writer = csv.writer(f)
            print(output)
            writer.writerow(output)