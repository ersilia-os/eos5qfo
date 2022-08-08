import pandas as pd
import numpy as np
import sys
import os

# current file directory
file_path = os.path.dirname(os.path.abspath(__file__))

# hide gpus
os.environ["CUDA_VISIBLE_DEVICES"]="-1"

# point to the rexgen_direct paths
path_root = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..", "..")
sys.path.append(os.path.abspath(path_root))

from framework.rexgen_direct.rexgen_direct.core_wln_global.directcorefinder import DirectCoreFinder 
from framework.rexgen_direct.rexgen_direct.rank_diff_wln.directcandranker import DirectCandRanker
from framework.rexgen_direct.rexgen_direct.scripts.eval_by_smiles import edit_mol

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# read smiles input and model metadata csv files
smiles_df = pd.read_csv(input_file)
reaction_smiles_list = smiles_df.iloc[:, 0].to_list()

# load rexgen core models
directcorefinder = DirectCoreFinder()
directcorefinder.load_model()
directcandranker = DirectCandRanker()
directcandranker.load_model()

outcome_df = pd.DataFrame(columns=['products'])
for react in reaction_smiles_list:
    (react, bond_preds, bond_scores, cur_att_score) = directcorefinder.predict(react)
    outcomes = directcandranker.predict(react, bond_preds, bond_scores)
    if len(outcomes) == 0:
        outcome_df.loc[len(outcome_df.index)] = [np.NaN]
    else:
        outcome_df.loc[len(outcome_df.index)] = [outcomes[0]['smiles']]
    
# write output to csv
outcome_df.to_csv(output_file, index=False)
