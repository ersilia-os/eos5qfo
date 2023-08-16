import sys
import os

# current file directory
file_path = os.path.dirname(os.path.abspath(__file__))

# hide gpus
os.environ["CUDA_VISIBLE_DEVICES"]="-1"

# point to the rexgen_direct paths
path_root = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..", "..")
sys.path.append(os.path.abspath(path_root))

from rexgen_direct.rexgen_direct.core_wln_global.directcorefinder import DirectCoreFinder 
from rexgen_direct.rexgen_direct.rank_diff_wln.directcandranker import DirectCandRanker





# load rexgen core models
directcorefinder = DirectCoreFinder()
directcorefinder.load_model()
directcandranker = DirectCandRanker()
directcandranker.load_model()


def rexgen(smiles_list):
    print(smiles_list)
    outcome_list = []
    for reaction_list in smiles_list:
        react_smiles= '.'.join(reaction_list)
        (react_smiles, bond_preds, bond_scores, cur_att_score) = directcorefinder.predict(react_smiles)
        outcomes = directcandranker.predict(react_smiles, bond_preds, bond_scores)
        if len(outcomes) == 0:
            outcome_list += [None]
        else:
            outcome_list += [outcomes[0]['smiles']]
    return outcome_list


        

