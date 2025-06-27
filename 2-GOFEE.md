Unfortunately GOFEE is not working yet.

Download and install GOFEE following http://grendel-www.cscaa.dk/mkb/installation/installation.html#install-from-source

Edit run_search.py header to follow file supplied since directory structure is different. 

Load environment in qsub file following job-gofee2025.sh.

Just use AGOX




run search py headers
import numpy as np

from gpaw import GPAW, FermiDirac, Mixer, PW #PoissonSolver, Mixer, PW
from gpaw.utilities import h2gpts

from gofee.surrogate.gpr import GPR

from ase.io import read, write

import sys
from gofee.candidates.candidate_generation import CandidateGenerator, StartGenerator
from gofee.utils import OperationConstraint
from gofee.candidates.basic_mutations import RattleMutation, PermutationMutation, RattleMutation2
from gofee.gofee import GOFEE
import os
import numpy as np
import math
