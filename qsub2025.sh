#!/bin/bash
#PBS -q xi1
#PBS -l select=1:ncpus=16:mpiprocs=16:ompthreads=1
#PBS -j oe
#PBS -N label

ulimit -s unlimited

export I_MPI_ADJUST_ALLGATHERV=2
export I_MPI_PIN=1
cd ${PBS_O_WORKDIR}

source /home/bctan/gpawenv/bin/activate
module load  intel/2020.2.254   intelmpi/2020.2.254



python atomization.py
