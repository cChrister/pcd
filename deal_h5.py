#####################h5文件制作##########################
import h5py
import SimpleITK as sitk
import os


def GetHDF5File(imgpath, labelpath, name='HDF5Filename'):
    f = h5py.File(os.path.join('E:\\result', name + ".h5"), 'w') //根据需要修改h5存放路径
    imglist = os.listdir(imgpath)  //获取训练集原图路径下所有的文件名
    for i in imglist:   //依次遍历所有的图片
        groupname = i.split('.nii.gz')[0]  //根据需求给文件命名
        new_group = f.create_group(groupname)  //creat group
        image = sitk.ReadImage(os.path.join(imgpath, i))  //读取图片
        arr = sitk.GetArrayFromImage(image)   //将图片转换为数组形式 
        Afterarr = (((arr- arr.min()) / (arr.max() - arr.min())) * 255).astype('uint8')
        //进行归一化
        new_group.create_dataset('volume', dtype='uint8', data=Afterarr)  //create dataset
        labellist = os.listdir(labelpath)  //获取训练集label路径下所有的文件名

        for j in labellist:
        	if i == j:
            	label = sitk.ReadImage(os.path.join(labelpath, j))  
            	label_arr = sitk.GetArrayFromImage(label)
            	label = label_arr.astype('uint8')import h5py
import os
import numpy as np
import SimpleITK as sitk

dataset = h5py.File('F:\\xxx.h5', 'r')   //指定h5文件的路径
savepath = "F:\\..."   //另存为nii文件的路径
first_level_keys = [key for key in dataset.keys()]
for first_level_key in first_level_keys:
    if not os.path.exists(os.path.join(savepath, first_level_key)):
        os.makedirs(os.path.join(savepath, first_level_key))
    second_level_keys = [key for key in dataset[first_level_key].keys()]
    for second_level_key in second_level_keys:
        if not os.path.exists(os.path.join(savepath, first_level_key, second_level_key)):
            os.makedirs(os.path.join(savepath, first_level_key, second_level_key))
        image_arr = np.array(dataset[first_level_key][second_level_key])
        img = sitk.GetImageFromArray(image_arr)
        img.SetSpacing([1.0, 1.0, 1.0])   //根据需求修改spacing
        sitk.WriteImage(img, os.path.join(savepath, first_level_key, second_level_key, second_level_key + ".nii.gz"))
    print(first_level_key)

            	new_group.create_dataset('segmentation', dtype='uint8', data=label) //根据需求命名
    f.close()

imgpath = 'E:\\imageTr'   //训练集原图的路径
labelpath = 'E:\\labelTr'   //训练集label的路径
GetHDF5File(imgpath, labelpath, 'HDF5Filename')  //根据需要修改h5的文件名，
                                                          //这里是HDF5Filename

#########################h5文件读取########################
