DATE=`date "+%Y%m%d-%H%M"`
eval "$(~/miniconda3/bin/conda shell.bash hook)"
conda activate platform_env
nohup python3 server.py > log/out_${DATE}.log 2> log/error_${DATE}.log