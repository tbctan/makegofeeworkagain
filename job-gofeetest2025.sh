#!/bin/bash
#PBS -q xh2
#PBS -l select=1:ncpus=24:mpiprocs=24:ompthreads=1
#PBS -j oe
#PBS -N test

ulimit -s unlimited
source /home/bctan/gpawenv/bin/activate


module purge
module use --append /home/krojas/share/modulefiles

module load qe/7.2 ##will load intel2020 modules

#export I_MPI_ADJUST_ALLGATHERV=2
#export I_MPI_PIN=1
cd ${PBS_O_WORKDIR}

export PATH=/home/bctan/gpawenv/bin:$PATH
export PYTHONPATH=/home/bctan/GPAW/src/gpaw-25.1.0:$PYTHONPATH
export PYTHONPATH=/home/bctan/GPAW/src/2306gofeeNEW:$PYTHONPATH
#export PATH=$HOME/GPAW/src/gofeeNEW/statistics_tools/survival_statistics:$PATH

# Activate gofee environment
export I_MPI_PIN=1
export I_MPI_ADJUST_ALLGATHERV=2


#ENVIRONMENT CHECK
echo " "
echo " "
echo $(pwd) 
echo "MPIRUN    " $(which mpirun)
echo "PYTHON    " $(which python)
echo "ASE       " $(which ase)
#### echo "GOFEE     " $(which gofee)
echo "GPAW      " $(which gpaw)
hostname
echo " ============= "
date
mpiexec python -u run_search.py
echo "END"
date
