import numpy as np
import h5py as h5
import open3d as o3d
import random
import os

select_train = {"bag":59+1,
                "bed":220-59,
                "bin":309-220,
                "box":581-309,
                "cabinet":898-581,
                "chair":1017-898,
                "desk":1156-1017,
                "display":1335-1156,
                "door":1553-1335,
                "pillow":1740-1553,
                "shelf":1853-1740,
                "sink":1937-1853,
                "sofa":2031-1937,
                "table":2243-2031,
                "toilet":2308-2243}
select_test  = {"bag":16+1,
                "bed":56-16,
                "bin":84-56,
                "box":159-84,
                "cabinet":237-159,
                "chair":267-237,
                "desk":309-267,
                "display":351-309,
                "door":400-351,
                "pillow":454-400,
                "shelf":476-454,
                "sink":497-476,
                "sofa":521-497,
                "table":563-521,
                "toilet":580-563}
# 定义旋转矩阵
angle1 = 45/180 * np.pi
cosval1 = np.cos(angle1)
sinval1 = np.sin(angle1)
rotation_matrix1 = np.array([[cosval1, 0, sinval1],
                            [0, 1, 0],
                            [-sinval1, 0, cosval1]])
angle2 = 180/180 * np.pi
cosval2 = np.cos(angle2)
sinval2 = np.sin(angle2)
rotation_matrix2 = np.array([[cosval2, 0, sinval2],
                            [0, 1, 0],
                            [-sinval2, 0, cosval2]])


# 确定文件下标及个数
f1 = h5.File("training_objectdataset45_180.h5",'w')
f3 = h5.File("test_objectdataset45_180.h5",'w')
f2 = h5.File("raw_training_objectdataset.h5",'r')
f4 = h5.File("raw_test_objectdataset.h5",'r')
data = np.ndarray((2309,2048,3))
data_test = np.ndarray((581,2048,3))
# Existing datasets should be retrieved using the group indexing syntax
f1.create_dataset('label',(2309,),dtype=int,data=f2['label'][:])
f3.create_dataset('label',(581,),dtype=int,data=f4['label'][:])


# 读取文件，旋转下采样点云，写入h5文件
dirslist = [] # 获取目录信息，方便转换工作目录
with open("dirslist.txt","r") as f_dirslist:
    lines = f_dirslist.readlines()
    for line in lines:
        dirslist.append(line[:-2])

scene=0
scene_test=0
for dir in dirslist:
    path = "/home/chenxiang/dataset/PB_T50_RS/"
    len_select_pcd = select_train[dir] 
    len_select_test_pcd = select_test[dir]
    dir = path+dir
    os.chdir(dir)   #修改当前工作目录
    f_pcd = os.listdir(dir)
    # print(os.getcwd())
    # 随机获取指定目录下的点云文件
    f_select_pcd = random.sample(f_pcd,len_select_pcd+20)
    count=0
    count_test=0

    # 写入训练集
    for file in f_select_pcd:
        # 旋转下采样操作
        f = np.fromfile(file,"float32")
        scale = int(len(f[1:]))
        a = f[1:].reshape(int(scale/11),11)
        for i in range(0,int(scale/11)):
            xyz = a[i][0:3]
            # normal = a[i][3:6]
            xyz = np.dot(xyz,rotation_matrix1)
            # normal = np.dot(normal,rotation_matrix1)
            a[i][0:3] = xyz
            # a[i][3:6] = normal
        a = a.reshape(1,scale)
        f[1:] = a
        # f.tofile(pcd) # 暂时不需要保存文件
        pcd = o3d.geometry.PointCloud()
        point_cloud_with_normal = f[1:].reshape(int(scale/11),11)
        pcd.points = o3d.utility.Vector3dVector(point_cloud_with_normal[:, 0:3])
        # pcd.normals = o3d.utility.Vector3dVector(point_cloud_with_normal[:, 3:6])
        downpcd = pcd #     体素随机下采样
        if len(downpcd.points) > 2048:
            for size in range(1,1000):
                downpcd = pcd.voxel_down_sample(voxel_size=(size/1000))
                if len(downpcd.points)-2048 <= 300 and len(downpcd.points)-2048 >= 0:
                    break
                elif len(downpcd.points)-2048 < 0:
                    if size-1>0:
                        downpcd = pcd.voxel_down_sample(voxel_size=((size-1)/1000))
                        break
                    else:
                        break
            if len(downpcd.points)>2048:
                downpcd = downpcd.random_down_sample(sampling_ratio = 2048/len(downpcd.points))

        # 写入h5文件
        if count < len_select_pcd:
            if len(downpcd.points) == 2048:
                count+=1
                data_points = np.asarray(downpcd.points)
                data[scene] = data_points
                scene+=1
            else:
                continue
        else:
            break
    print('training is done')


    f_pcd = [x for x in f_pcd if x not in f_select_pcd]   
    f_select_test_pcd = random.sample(f_pcd,len_select_test_pcd+20)
    # 写入测试集
    for file in f_select_test_pcd:
        # 旋转下采样操作
        f = np.fromfile(file,"float32")
        scale = int(len(f[1:]))
        a = f[1:].reshape(int(scale/11),11)
        for i in range(0,int(scale/11)):
            xyz = a[i][0:3]
            # normal = a[i][3:6]
            xyz = np.dot(xyz,rotation_matrix2)
            # normal = np.dot(normal,rotation_matrix2)
            a[i][0:3] = xyz
            # a[i][3:6] = normal
        a = a.reshape(1,scale)
        f[1:] = a
        # f.tofile(pcd) # 暂时不需要保存文件
        pcd = o3d.geometry.PointCloud()
        point_cloud_with_normal = f[1:].reshape(int(scale/11),11)
        pcd.points = o3d.utility.Vector3dVector(point_cloud_with_normal[:, 0:3])
        # pcd.normals = o3d.utility.Vector3dVector(point_cloud_with_normal[:, 3:6])
        downpcd = pcd #     体素随机下采样
        if len(downpcd.points) > 2048:
            for size in range(1,1000):
                downpcd = pcd.voxel_down_sample(voxel_size=(size/1000))
                if len(downpcd.points)-2048 <= 300 and len(downpcd.points)-2048 >= 0:
                    break
                elif len(downpcd.points)-2048 < 0:
                    if size-1>0:
                        downpcd = pcd.voxel_down_sample(voxel_size=((size-1)/1000))
                        break
                    else:
                        break
            if len(downpcd.points)>2048:
                downpcd = downpcd.random_down_sample(sampling_ratio = 2048/len(downpcd.points))

        # 写入h5文件
        if count_test < len_select_test_pcd:
            if len(downpcd.points) >= 2048:
                count_test+=1
                data_points = np.asarray(downpcd.points)
                data_test[scene_test] = data_points
                scene_test+=1
            else:
                continue
        else:
            break
    print('test is done')

    print(dir+' is done')
    os.chdir("/home/chenxiang/dataset/PB_T50_RS/")
# Initialize the dataset to an existing NumPy array by providing the data parameter:
data_h5 = f1.create_dataset('data',data=data)
data_test_h5 = f3.create_dataset('data',data=data_test)
f1.close()
f3.close()