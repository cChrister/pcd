alias con="conda activate pcd"
alias ..="cd .."
alias ll="ls -alh"

# conda env activate ..
alias pcd="conda activate pcd"
alias pet="conda activate pet"
alias tf="conda activate tf"
alias lfnet="conda activate lfnet"
alias d2net="conda activate d2net"
alias bpcr="conda activate bpcr"
alias nn="conda activate pointnn"
# pip source
alias aliyun="pip config set global.index-url https://mirrors.aliyun.com/pypi/simple"
alias tsinghua="pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple/"
alias pypi="pip config set global.index-url https://pypi.org/simple"

# rar
export PATH=/home/chenxiang/rar:$PATH
# colmap
export PATH=/home/chenxiang/colmap/usr/local/bin:$PATH
# zsh
export PATH=/home/chenxiang/zsh/bin:$PATH

# cuda-10.0
#export CUDA_HOME=/usr/local/cuda-10.0
#export PATH=/usr/local/cuda-10.0/bin:$PATH
#export LD_LIBRARY_PATH=/usr/local/cuda-10.0/lib64:$LD_LIBRARY_PATH

# cuda-10.1
export CUDA_HOME=/home/chenxiang/cuda-10.1
export PATH=/home/chenxiang/cuda-10.1/bin:$PATH
export LD_LIBRARY_PATH=/home/chenxiang/cuda-10.1/lib64:$LD_LIBRARY_PATH

# cuda-10.2
#export CUDA_HOME=/usr/local/cuda-10.2
#export PATH=/usr/local/cuda-10.2/bin:$PATH
#export LD_LIBRARY_PATH=/usr/local/cuda-10.2/lib64:$LD_LIBRARY_PATH

# cuda-11.1
#export CUDA_HOME=/usr/local/cuda-11.1
#export PATH=/usr/local/cuda-11.1/bin:$PATH
#export LD_LIBRARY_PATH=/usr/local/cuda-11.1/lib64:$LD_LIBRARY_PATH

# cuda-11.2
#export CUDA_HOME=/usr/local/cuda-11.2
#export PATH=/usr/local/cuda-11.2/bin:$PATH
#export LD_LIBRARY_PATH=/usr/local/cuda-11.2/lib64:$LD_LIBRARY_PATH

# gcc rely library
export LD_LIBRARY_PATH=/home/chenxiang/gcc-7.2.0/gmp-6.1.0/lib:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/home/chenxiang/gcc-7.2.0/mpfr-3.1.4/lib:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/home/chenxiang/gcc-7.2.0/mpc-1.0.3/lib:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=/home/chenxiang/gcc-7.2.0/isl-0.16.1/lib:$LD_LIBRARY_PATH
export PATH=/home/chenxiang/gcc-7.2.0/m4-1.4.19/bin:$PATH

# gcc
export LD_LIBRARY_PATH=/home/chenxiang/gcc-7.2.0/gcc/lib:$LD_LIBRARY_PATH
export PATH=/home/chenxiang/gcc-7.2.0/gcc/bin:$PATH
export PATH=/home/chenxiang/gcc-7.2.0/gcc/lib64:$PATH
