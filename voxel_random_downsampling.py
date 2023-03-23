import open3d as o3d
import numpy as np
pcd = o3d.geometry.PointCloud()
f = np.fromfile("021_00007_0.bin","float32")
scale = len(f[1:])
point_cloud_with_normal = f[1:].reshape(int(scale/11),11)
pcd.points = o3d.utility.Vector3dVector(point_cloud_with_normal[:, 0:3])
pcd.normals = o3d.utility.Vector3dVector(point_cloud_with_normal[:, 3:6])
# print(point_cloud_with_normal[:, 0:3].shape())

downpcd = pcd
for size in range(1,1000):
    downpcd = pcd.voxel_down_sample(voxel_size=(size/1000))
    print(len(downpcd.points))
    if len(downpcd.points)-2048 <= 300 and len(downpcd.points)-2048 >= 0:
        break
    elif len(downpcd.points)-2048 <= 0:
        size-=1
        downpcd = pcd.voxel_down_sample(oxel_size=(size/1000))
        break
# print(len(downpcd.points))
downpcd = downpcd.random_down_sample(sampling_ratio = 2048/len(downpcd.points))
o3d.visualization.draw_geometries([downpcd])

# data = np.ndarray((2309,2048,3))
# data_points = np.asarray(downpcd.points)
# data[0] = data_points
# print(data_points)