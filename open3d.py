"""
In this code we use open3d deal with different 3d file
| .ply .pcd .bin | open/write/visiualize/other ops  |

python 3.7
open3d 0.16.0
"""
import open3d as o3d
import numpy as np

# we use read_point_cloud to open .ply .pcd
pcd = o3d.io.read_point_cloud("feature.pcd")
ply = o3d.io.read_point_cloud("lego_pointnerf.ply")
cor = np.asarray(ply.points).astype("float32")
rgb = np.asarray(ply.colors).astype("float32")
# nor = pcd.normals
# we use np.fromfile to read .bin
# f = np.fromfile("secene.bin","float32")
# f = f[1:].reshape(num_points,num_features)

# create .pcd .ply
pcd = o3d.geometry.PointCloud()
ply = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(cor)
pcd.colors = o3d.utility.Vector3dVector(rgb)
# pcd.normals = o3d.utility.Vector3dVector(nor)

# voxel_down_sample just for point_cloud
pcd = pcd.voxel_down_sample(voxel_size=(0.04))

ply = pcd
# visiualize pcd ply
o3d.visualization.draw_geometries([pcd])
o3d.visualization.draw_geometries([ply])

# write point_cloud into .pcd .ply
# we can just use pcd I/O deal with both file
o3d.io.write_point_cloud("./feature.pcd", pcd)
o3d.io.write_point_cloud("./feature.ply", ply)
# we use np.tofile write .bin
# np.tofile(f)
