# -*- coding: utf-8 -*-

#Importations nécessaires 
from aizynthfinder.chem import Molecule
import pandas as pd
import numpy as np
from tqdm.notebook import tqdm

#Dictionnaire de correspondance des groupes/numéros 
grp_fp = {"Aldehyde": "004",
         "Cetone":"005",
         "Enamine":"024",
         "Alcool":"028",
         "Phenol":"034",
         "Ether":"037",
         "Amine":"047",
         "Halogene":"061",
         "Acide Carboxylique":"076",
         "Lactone":"079",
         "Uree":"133",
         "Alcene":"199"}



def model_fp_from_fp(f_r,f_p):
    '''
    Retourne les fingerprints désirés (produit, reaction) à partir des fp des réactifs et des produits
    '''
    return f_p, f_p-f_r

def fp_out_of_database_line(line_str):
    '''
    On recrée le fingerprint à partir de la façon dont il est stocké
    '''
    res_fp = np.zeros(2048)
    grps_idx = line_str.split(" ")
    for grp_idx in grps_idx[:-1]:
        idx = grp_idx.split("-")
        n = len(idx)
        if (n==1):
            res_fp[int(idx[0])] = 1
        elif n==2:
            res_fp[int(idx[0])] = int(idx[1])
        else:
            res_fp[int(idx[0])] = - int(idx[2])
    return res_fp
    
def transform_fp_for_model(base_fp):
    return base_fp[["Product_Fingerprint","Reaction_Fingerprint"]]


def select_grp(base_fp_false,base_fp_true,name_grps):
    '''
    Selectionne les fingerprints dont la réaction correspond à une reaction de name_grps qui est la liste qui contient l'ensemble des grps sélectionnés
    '''
    fname_false = [f"{grp}_False_Reactions.csv" for grp in name_grps]
    fname_true = [f"/{grp}_True_Reactions.csv" for grp in name_grps]
    res = []
    #On récupère les réactions associées aux groupes qui nous intéressent dans le cas des fausses réactions et des vraies réactions 
    for i  in range(len(name_grps)):
        data_false,data_true = pd.read_csv(fname_false[i]).to_numpy(),pd.read_csv(fname_true[i]).to_numpy() 
        false_temp1,false_temp2 = [],[]
        true_temp1,true_temp2 = [],[]
        progress_bar = tqdm(total = data_false.shape[0])
        for idx in data_false:
            idx = int(idx)
            try:
                false_temp2.append(fp_out_of_database_line(base_fp_false.iloc[idx,2]))
                false_temp1.append(fp_out_of_database_line(base_fp_false.iloc[idx,1]))
            except AttributeError:
                continue
            progress_bar.update(1)
        progress_bar = tqdm(total = data_true.shape[0])
        for idx in data_true:
            idx = int(idx)
            try:
                true_temp2.append(fp_out_of_database_line(base_fp_true.iloc[idx,2]))
                true_temp1.append(fp_out_of_database_line(base_fp_true.iloc[idx,1]))
            except AttributeError:
                continue
            progress_bar.update(1)
        res.append((np.array(false_temp1),np.array(false_temp2),np.array(true_temp1),np.array(true_temp2)))
    return res






