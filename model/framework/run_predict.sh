source $CONDA_PREFIX_1/etc/profile.d/conda.sh
conda activate eos5qfo_py36
python3.6 $1/code/main.py $2 $3
conda deactivate 
