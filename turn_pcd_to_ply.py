import open3d as o3d
import numpy as np
import os

path = os.getcwd()
os.chdir(path+"/bag")
f1 = np.fromfile("005_00020_0.bin","float32")
ply = o3d.geometry.TriangleMesh()
scale = int(len(f1[1:]))
a = f1[1:].reshape(int(scale/11),11)

# 定义旋转矩阵，进行旋转
angle = 180/180 * np.pi
cosval = np.cos(angle)
sinval = np.sin(angle)
rotation_matrix = np.array([[cosval, 0, sinval],
                            [0, 1, 0],
                            [-sinval, 0, cosval]])
for i in range(0,int(scale/11)):
        xyz = a[i][0:3]
        xyz = np.dot(xyz,rotation_matrix)
        a[i][0:3] = xyz

points_array = a[:, 0:3]
ply.vertices = o3d.utility.Vector3dVector(points_array)
o3d.io.write_triangle_mesh(path+"/7.ply", ply)