## cuda-10.1  
[教程](https://zhuanlan.zhihu.com/p/198161777)  
[历史cuda版本](https://developer.nvidia.com/cuda-toolkit-archive)  
[历史cudnn版本](https://developer.nvidia.com/rdp/cudnn-archive)  
- CUDA版本一定要对应，Linux系统版本号不一定要对应  
- 下载CUDA runfile进行安装，只安装CUDA Toolkit，修改安装路径  
- 安装完成后一定记得删除 /tmp/cuda-installer.log 文件  
> 安装路径 /home/chenxiang/cuda-10.1  
  export PATH=/home/chenxiang/cuda-10.1/bin:$PATH  
  export LD_LIBRARY_PATH=/home/chenxiang/cuda-10.1/lib64:$LD_LIBRARY_PATH  


## gcc-7.2.0
[gcc安装教程](https://blog.csdn.net/u012528143/article/details/105845883)  
[历史gcc/mp4/gmp/mpfr/mpc版本](http://ftp.gnu.org/gnu/gcc/)  
[历史isl版本](https://gcc.gnu.org/pub/gcc/infrastructure/)  
[gcc问题mp4/gmp/mpfr/mpc](https://www.jianshu.com/p/829059c0e6d2)  
[gcc问题sys/ustat.h](https://blog.csdn.net/chuansailang4709/article/details/108513788)  
[gcc问题assertion_failed](https://blog.csdn.net/weixin_46584887/article/details/122538399)  
- 安装过程中大部分是路径错误, make install后 libgmp.la / libmpfr.la / libmpc.la
- 注意修改环境变量  

1. 获取安装包  (安装包放在gcc-7.2.0内)
    > wget https://ftp.gnu.org/gnu/gcc/gcc-7.2.0/gcc-7.2.0.tar.gz  
        wget https://ftp.gnu.org/gnu/m4/m4-1.4.19.tar.gz  
        wget https://ftp.gnu.org/gnu/gmp/gmp-6.1.0.tar.bz2  
        wget https://ftp.gnu.org/gnu/mpfr/mpfr-3.1.4.tar.gz  
        wget https://ftp.gnu.org/gnu/mpc/mpc-1.0.3.tar.gz  
        wget https://gcc.gnu.org/pub/gcc/infrastructure/isl-0.16.1.tar.bz2  
    tar -zxvf / tar -jxvf  
2. make && make install  
    > ./configure --prefix=/home/chenxiang/gcc-7.2.0/m4-1.4.19  
    ./configure --prefix=/home/chenxiang/gcc-7.2.0/gmp-6.1.0  
    ./configure  --prefix=/home/chenxiang/gcc-7.2.0/mpfr-3.1.4 --with-gmp-include=/home/chenxiang/gcc-7.2.0/gmp-6.1.0/include --with-gmp-lib=/home/chenxiang/gcc-7.2.0/gmp-6.1.0/lib  
    ./configure --prefix=/home/chenxiang/gcc-7.2.0/mpc-1.0.3 --with-gmp-include=/home/chenxiang/gcc-7.2.0/gmp-6.1.0/include --with-gmp-lib=/home/chenxiang/gcc-7.2.0/gmp-6.1.0/lib --with-mpfr-include=/home/chenxiang/gcc-7.2.0/mpfr-3.1.4/include --with-mpfr-lib=/home/chenxiang/gcc-7.2.0/mpfr-3.1.4/lib  
    ./configure --prefix=/home/chenxiang/gcc-7.2.0/isl-0.16.1 --with-gmp-prefix=/home/chenxiang/gcc-7.2.0/gmp-6.1.0  
    ./configure --prefix=/home/chenxiang/gcc-7.2.0/gcc --with-gmp-include=/home/chenxiang/gcc-7.2.0/gmp-6.1.0/include --with-gmp-lib=/home/chenxiang/gcc-7.2.0/gmp-6.1.0/lib --with-mpfr-include=/home/chenxiang/gcc-7.2.0/mpfr-3.1.4/include --with-mpfr-lib=/home/chenxiang/gcc-7.2.0/mpfr-3.1.4/lib --with-mpc-include=/home/chenxiang/gcc-7.2.0/mpc-1.0.3/include --with-mpc-lib=/home/chenxiang/gcc-7.2.0/mpc-1.0.3/lib --with-isl-include=/home/chenxiang/gcc-7.2.0/isl-0.16.1/include --with-isl-lib=/home/chenxiang/gcc-7.2.0/isl-0.16.1/lib -enable-languages=c,c++ -disable-multilib  
    make -j8 > LOG.txt
3. 修改gcc编译过程中出现的BUG
    > vim libsanitizer/sanitizer_common/sanitizer_platform_limits_posix.cc  (具体修改内容详见上方博客)  
    sed -e '1152 s|^|//|' -i libsanitizer/sanitizer_common/ sanitizer_platform_limits_posix.cc  
4. 配置环境变量  
    >export LD_LIBRARY_PATH=/home/chenxiang/gcc-7.2.0/gmp-6.1.0/lib:$LD_LIBRARY_PATH  
    export LD_LIBRARY_PATH=/home/chenxiang/gcc-7.2.0/mpfr-3.1.4/lib:$LD_LIBRARY_PATH  
    export LD_LIBRARY_PATH=/home/chenxiang/gcc-7.2.0/mpc-1.0.3/lib:$LD_LIBRARY_PATH  
    export LD_LIBRARY_PATH=/home/chenxiang/gcc-7.2.0/isl-0.16.1/lib:$LD_LIBRARY_PATH  
    export LD_LIBRARY_PATH=/home/chenxiang/gcc-7.2.0/gcc/lib:$LD_LIBRARY_PATH  
    export PATH=/home/chenxiang/gcc-7.2.0/m4-1.4.19/bin:$PATH  
    export PATH=/home/chenxiang/gcc-7.2.0/gcc/bin:$PATH  
    export PATH=/home/chenxiang/gcc-7.2.0/gcc/lib64:$PATH
