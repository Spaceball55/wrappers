#!/bin/bash
#SBATCH --job-name=metaRNN
#SBATCH --partition=interactive
#SBATCH --ntasks=2
#SBATCH --nodes=1
#SBATCH --mem=5G
#SBATCH --time=3-00:00:00
#SBATCH --nodelist=mhgcp-r01
#SBATCH -o out_slurm/metaRNN-%j.out
#SBATCH -e out_slurm/metaRNN-%j.err

start=$(date +%s)
echo "starting at $(date) on $(hostname)"

# Print the SLURM job ID.
echo "SLURM_JOBID=$SLURM_JOBID"

# Run the application
./run_metaRNN.sh

end=$(date +%s)
echo "ended at $(date) on $(hostname). Time elapsed: $(date -u -d @$((end-start)) +'%H:%M:%S')"
exit 0
