# imports
import numpy as np
from rdkit.Chem import AllChem

def get_ECFP(mol, radio):
    ECFPs = mol2alt_sentence(mol, radio)
    if len(ECFPs) % (radio + 1) != 0:
        ECFPs = ECFPs[:-(len(ECFPs) % (radio + 1))]
    ECFP_by_radio = list((np.array(ECFPs).reshape((int(len(ECFPs) / (radio + 1)), (radio + 1))))[:, radio])
    return ECFP_by_radio


def mol2alt_sentence(mol, radius):
    radii = list(range(int(radius) + 1))
    info = {}
    _ = AllChem.GetMorganFingerprint(mol, radius, bitInfo=info)  # info: dictionary identifier, atom_idx, radius

    mol_atoms = [a.GetIdx() for a in mol.GetAtoms()]
    dict_atoms = {x: {r: None for r in radii} for x in mol_atoms}

    for element in info:
        for atom_idx, radius_at in info[element]:
            dict_atoms[atom_idx][radius_at] = element  # {atom number: {fp radius: identifier}}

    # merge identifiers alternating radius to sentence: atom 0 radius0, atom 0 radius 1, etc.
    identifiers_alt = []
    for atom in dict_atoms:  # iterate over atoms
        for r in radii:  # iterate over radii
            identifiers_alt.append(dict_atoms[atom][r])

    alternating_sentence = map(str, [x for x in identifiers_alt if x])

    return list(alternating_sentence)


def get_sentence_vec(tokens,embedding,token_dict):
    #The tokens of a sentence are converted into the vec of the sentence 
    # using embedding, and the sentence vec is calculated using the mean value
    feature_vec = np.zeros(512) #Create a 1-dimensional array of all 0s
    n=0
    for token in tokens:
        if token in token_dict:
            feature_vec = np.add(feature_vec, embedding[token_dict[token]])
        else:n+=1
    sent_vec = np.divide(feature_vec, len(tokens)-n)
    return sent_vec

def vec_predict(vec,models,ML_model):

    #Read a stored data table in pkl format, not big
    for model_name,model in models:
        if model_name == ML_model:
           # Y_predict = model.predict(vec.reshape(1, -1)) # returns the actual label
            Y_predict_p = model.predict_proba(vec.reshape(1, -1))[:, 1] # returns the probability

    # return Y_predict, Y_predict_p   # To return both actual prediction and probability
    return Y_predict_p