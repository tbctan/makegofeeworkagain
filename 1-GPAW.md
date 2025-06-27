# GPAW Summoning Ritual on Smith 2025
!! Advice: instead of GOFEE just use AGOX, but may still need GPAW.

### Preparation

Select intel module and use it consistently throughout install. make sure these are loaded with module list.  
`module load intel/2020.2.254 intelmpi/2020.2.254`

### Install Python

Remove previous python installations. create new one 

> module load python/3.9.19
> deactivate
> python -m venv gpawenv
> module purge
> source ~/newenv/bin/activate
> module load intel/2020.2.254 intelmpi/2020.2.254

At this point can install gpaw requirements using pip install gpaw. Of course it's not going to work, but at least the requirements are there. Pip is also not recommended because it is precompiled so unoptimized for mpi.

Install prereqs with 
`pip install numpy scipy ase cymem cython decorator mpi4py pytest`
###  Install libxc

> cd ~/src/ 
> wget https://gitlab.com/libxc/libxc/-/archive/6.2.2/libxc-6.2.2.tar.bz2 
> tar -xf libxc-6.2.2.tar.bz2 
> cd libxc-6.2.2 
> autoreconf -i        #generates config if not available
> ./configure CFLAG="-O2 -fPIC" --enable-shared --disable-fortran --prefix=/home/bctan/lib/libxc-6.2.2
> make 
> make install

Change prefix to your directory. Can also use Kurt's libxc module. 


### Install GPAW

Download gpaw for custom install as specified in https://gpaw.readthedocs.io/install.html#download or via 
> wget https://pypi.org/packages/source/g/gpaw/gpaw-25.1.0.tar.gz
> tar -xf gpaw-25.1.0.tar.gz

Edit the following files: 
1. setup.py: 
setup.py file I used is included in repository as setup-works2025.py.  
Change options in setup.py to 
> parallel_python_interpreter = False
> compiler = None
> mpi = None
> noblas = True # False
> nolibxc = True # False
> fftw = False
> scalapack = False
> libvdwxc = False
> elpa = False
> gpu = False
> intelmkl = True #False

i really just disabled stuff until it ran without errors. good luck.


2. siteconfig.py
Download siteconfig.py file in git repository. Change bctan to user as needed in libxc directory.  


3. ~/.bashrc:
add these to your .bashrc: 
> XC=~/libxc-6.2.2 
> export C_INCLUDE_PATH=$XC/include 
> export LIBRARY_PATH=$XC/lib export LD_LIBRARY_PATH=$XC/lib

Now, run
> python setup.py build
> python setup.py install


### Test GPAW
Try submitting qsub.sh (with environment variables changed) on Smith. This will run atomization.py which gets energies of H2 and H2O.
