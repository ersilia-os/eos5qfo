# imports
import os
import csv
import sys
import json
from rexgen import rexgen
# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))




# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    smiles_list=[]
    next(reader)  # skip header
    for r in reader:
        if len(r)==1:
            smiles_list.append([r[0]] + [k[0] for k in reader])
            break
        smiles_list.append(r)
    

# run model
outputs = rexgen(smiles_list)

#check input and output have the same length
input_len = len(smiles_list)
output_len = len(outputs)
assert input_len == output_len



with open(output_file, "w") as json_file:
    json.dump(outputs, json_file, indent=4) 