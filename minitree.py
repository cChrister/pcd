import open3d as o3d
import numpy as np

pcd = o3d.geometry.PointCloud()
f = np.fromfile("014_00014.bin","float32")
point_cloud_with_normal = f[1:].reshape(6534,11)
pcd.points = o3d.utility.Vector3dVector(point_cloud_with_normal[:, 0:3])
pcd.normals = o3d.utility.Vector3dVector(point_cloud_with_normal[:, 3:6])

pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.01, max_nn=30)) 
pcd.orient_normals_consistent_tangent_plane(100) 
print(np.asarray(pcd.normals)[:10, :]) 
 
o3d.visualization.draw_geometries([pcd], point_show_normal=True, window_name="最小生成树向量估计",
                                  width=1024, height=768,
                                  left=50, top=50,
                                  mesh_show_back_face=False)  # 可视化点云和法线
