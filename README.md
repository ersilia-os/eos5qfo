# RexGen
## Model identifiers
- Slug: rexgen
- Ersilia ID: eos5qfo
- Tags: GNN, ML, synthesis

# Model description
Utilizes a Weisfeiler-Lehman graph neural network to predict the products of an organic reaction given the reactants. 
- Input: Reactants as a single SMILES string. Individual reactants are in SMILES format and combined into the same string with a '.' separator (e.g. reactants “CCC” and “CCO” are input as “CCC.CCO”). 
- Output: Products as a SMILES string
- Model type: Generative
- Training set: 400,000. Training data is accessible via https://github.com/dan2097/patent-reaction-extraction.
- Mode of training: Pretrained

# Source code
Wengong Jin, Connor Coley, Regina Barzilay, Tommi Jaakkola. Predicting Organic Reaction Outcomes with Weisfeiler-Lehman Network. arXiv:1709.04555, 13, Sepember 2017. 	

- Code: https://github.com/connorcoley/rexgen_direct
- Checkpoints: https://github.com/connorcoley/rexgen_direct/tree/master/rexgen_direct/core_wln_global/model-300-3-direct

# License
The GPL-v3 license applies to all parts of the repository that are not externally maintained libraries. This repository uses the externally maintained library "rexgen_direct", located at [/model/framework](https://github.com/ersilia-os/eos5qfo/tree/main/model/framework/rexgen_direct) and licensed under a [GNU General Public License](https://github.com/ersilia-os/eos5qfo/blob/main/model/framework/rexgen_direct/LICENSE).

# History 
- Model was downloaded on 8/5/2022 from https://github.com/connorcoley/rexgen_direct
- Files enumerated in [NOTICE.md](https://github.com/ersilia-os/eos5qfo/blob/main/model/framework/rexgen_direct/NOTICE.md) contain modified import statements for Ersilia compatibility.

# About us
The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission or [volunteer](https://www.ersilia.io/volunteer) with us!
