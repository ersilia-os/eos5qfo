import pandas as pd
import numpy as np
import sys
import os
import json

# current file directory
file_path = os.path.dirname(os.path.abspath(__file__))

# hide gpus
os.environ["CUDA_VISIBLE_DEVICES"]="-1"

# point to the rexgen_direct paths
path_root = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..", "..")
sys.path.append(os.path.abspath(path_root))

from rexgen_direct.rexgen_direct.core_wln_global.directcorefinder import DirectCoreFinder 
from rexgen_direct.rexgen_direct.rank_diff_wln.directcandranker import DirectCandRanker
from rexgen_direct.rexgen_direct.scripts.eval_by_smiles import edit_mol





# load rexgen core models
directcorefinder = DirectCoreFinder()
directcorefinder.load_model()
directcandranker = DirectCandRanker()
directcandranker.load_model()


def rexgen(smiles_list):
    outcome_list = []
    for react in smiles_list:
        (react, bond_preds, bond_scores, cur_att_score) = directcorefinder.predict(react)
        outcomes = directcandranker.predict(react, bond_preds, bond_scores)
        if len(outcomes) == 0:
            outcome_list += [None]
        else:
            outcome_list += [outcomes[0]['smiles']]
    return outcome_list


        

