import open3d as o3d
import numpy as np
import os
path = os.getcwd()
os.chdir(path+"/bag")

pcd = o3d.geometry.PointCloud()
f = np.fromfile("005_00020_0.bin","float32")
scale = int(len(f[1:]))
point_cloud_with_normal = f[1:].reshape(int(scale/11),11)
pcd.points = o3d.utility.Vector3dVector(point_cloud_with_normal[:, 0:3])
pcd.normals = o3d.utility.Vector3dVector(point_cloud_with_normal[:, 3:6])
o3d.visualization.draw_geometries([pcd])
