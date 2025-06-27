"""User provided customizations.

Here one changes the default arguments for compiling _gpaw.so.

Here are all the lists that can be modified:

* libraries
  List of libraries to link: -l<lib1> -l<lib2> ...
* library_dirs
  Library search directories: -L<dir1> -L<dir2> ...
* include_dirs
  Header search directories: -I<dir1> -I<dir2> ...
* extra_link_args
  Arguments forwarded directly to linker
* extra_compile_args
  Arguments forwarded directly to compiler
* runtime_library_dirs
  Runtime library search directories: -Wl,-rpath=<dir1> -Wl,-rpath=<dir2> ...
* extra_objects
* define_macros

To override use the form:

    libraries = ['somelib', 'otherlib']

To append use the form

    libraries += ['somelib', 'otherlib']
"""

# flake8: noqa

# compiler = 'gcc'
# platform_id = ''
#compiler    = '/opt/intel/compilers_and_libraries_2020.2.254/linux/bin/intel64/icc'
mpicompiler = '/opt/intel/compilers_and_libraries_2020.2.254/linux/mpi/intel64/bin/mpiicc'
mpilinker   = '/opt/intel/compilers_and_libraries_2020.2.254/linux/mpi/intel64/bin/mpiicc'
platform_id = ''

extra_compile_args += ['-fPIC', '-O2', '-axCOMMON-AVX512,CORE-AVX512,CORE-AVX2,CORE-AVX-I,AVX,SSE4.2,SSE4.1,SSSE3,SSE3,SSE2', '-fopenmp']
extra_link_args += ['-mkl=sequential', '-fopenmp']

# MPI:
mpi = True
compiler = '/opt/intel/compilers_and_libraries_2020.2.254/linux/mpi/intel64/bin/mpiicc'

#if mpi:
#    compiler = 'mpiicc'


# FFTW3:
fftw = True
if fftw:
    include_dirs += ['/opt/intel/compilers_and_libraries_2020.2.254/linux/mkl/include/fftw']
#    include_dirs += ['/opt/intel/compilers_and_libraries_2017.4.196/linux/mkl/include/fftw']

# ScaLAPACK (version 2.0.1+ required):
scalapack = False
if scalapack:
    libraries += ['mkl_def', 'mkl_scalapack_lp64', 'mkl_blacs_intelmpi_lp64', 'scalapack']


# FFTW3:
#fftw = True
#if fftw:
#    libraries += ['fftw3']

# ScaLAPACK (version 2.0.1+ required):
#scalapack = True
# Enable advanced IntelMKL specific scalapack functions (pzgeevx)
# intelmkl = True
#if scalapack:
#    libraries += ['scalapack']

# Use Elpa (requires ScaLAPACK and Elpa API 20171201):
if 0:
    elpa = True
    elpadir = '/usr/local/elpa-2017.05.002-2018.0.128' #    elpadir = '/home/user/elpa'
    libraries += ['elpa']
    library_dirs += ['{}/lib'.format(elpadir)]
    runtime_library_dirs += ['{}/lib'.format(elpadir)]
    include_dirs += ['{}/include/elpa-xxxx.xx.xxx'.format(elpadir)]

# LibXC:
# In order to link libxc installed in a non-standard location
# (e.g.: configure --prefix=/home/user/libxc-2.0.1-1), use:

# - static linking:
if 0:
    xc = '/home/bctan/lib/libxc-6.2.2/'
#    xc = '/home/user/libxc-4.0.4/'
    include_dirs += [xc + 'include']
    extra_link_args += [xc + 'lib/libxc.a']
    if 'xc' in libraries:
        libraries.remove('xc')

# - dynamic linking (requires rpath or setting LD_LIBRARY_PATH at runtime):
if 0:
    xc = '/home/bctan/lib/libxc-6.2.2/' #    xc = '/home/user/libxc-4.0.4/'
    include_dirs += [xc + 'include']
    library_dirs += [xc + 'lib']
    # You can use rpath to avoid changing LD_LIBRARY_PATH:
    runtime_library_dirs += [xc + 'lib']
    if 'xc' not in libraries:
        libraries.append('xc')

# Enable this, if your MPI doesn't support MPI_INPLACE
if 0:
    undef_macros.append('GPAW_MPI_INPLACE')

# libvdwxc:
if 0:
    libvdwxc = True
    path = '/home/user/libvdwxc'
    include_dirs += ['%s/include' % path]
    library_dirs += ['%s/lib' % path]
    runtime_library_dirs += ['%s/lib' % path]
    libraries += ['vdwxc']
