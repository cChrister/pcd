#!/bin/bash
for dir in */;do
    cd $dir
    for file in *[^indicespartbug].bin;do
        python ../rotate.py --name $file
    done
    echo "${dir} rotations is done"
    cd ..
done

# scp IIPL.101:/home/chenxiang/dataset/PB_T50_RS/test_objectdataset.h5 .
# scp .\training_objectdataset1.h5 .\test_objectdataset1.h5 IIPL.112:/home/chenxiang/code/RepSurf/classification/data/ScanObjectNN/main_split