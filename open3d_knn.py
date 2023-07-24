#################################### 
#    File Name: knn_distance.py
#    Author: steve
#    E-mail: yqykrhf@163.com
#    Created Time: Sun 30 Apr 2023 08:51:59 PM CST
#    Brief: Compute knn neighbor with relative distance of chosen points
#    Reference: http://www.open3d.org/docs/latest/python_api_in/open3d.ml.torch.layers.KNNSearch.html
#    TODO: Not support GPU as reported in https://github.com/isl-org/Open3D/issues/5407
####################################

import torch
import open3d as o3d
import open3d.ml.torch as ml3d
import numpy as np
import argparse
import time


def args_config():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file_name', type=str, help='ply file name', \
                        default='/home/steve/Desktop/pc/pointnerf/lego_pointnerf.ply')
    parser.add_argument('--k_n', type=int, default=8, help='the number of nearest neighbors')
    parser.add_argument('--vis', action='store_true', help='Enable visualize') 
    parser.add_argument('--vis_radius', type=int, help='sphere radius of chosen points visualization', \
                        default=0.005)
    parser.add_argument('--ignore_query_point', action='store_true', help="If True the points that coincide with"
                        "the center of the search window will be ignored. This excludes the query point if ‘queries’"
                        "and ‘points’ are the same point cloud.")
    config = parser.parse_args()
    return config

def knn(args):
    # device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    device = torch.device('cpu')
    # load points, print necessary infomation
    pcd = o3d.io.read_point_cloud(args.file_name)
    pcd_array = np.asarray(pcd.points)
    
    idx_chosen = [65535]# chosen point cloud
    # idx_chosen = list(range(pcd_array.shape[0]))
    
    
    # queries_array = np.array([[0, 0, 1],
                            # [0.5, 2, 3]])
    
    queries_array = pcd_array[idx_chosen]
    queries_array.shape = (-1, 3)
    print(time.strftime(f'[%m.%d--%H:%M:%S] Start...'))
    print(f"Load a point cloud from {args.file_name} with points {pcd_array.shape[0]}.")
    
    # compute queries knn
    start = time.time()
    points = torch.tensor(pcd_array, dtype=torch.float32, device=device)
    queries = torch.tensor(queries_array, dtype=torch.float32, device=device)
    num_queries = queries_array.shape[0]
    
    nsearch = ml3d.layers.KNNSearch(return_distances=True, ignore_query_point=args.ignore_query_point)
    
    ans = nsearch(points, queries, args.k_n)
    print(ans.neighbors_distance)
    zero_num = (ans.neighbors_distance == 0.).sum()
    print(zero_num)
    
    # if torch.count_nonzero(ans.neighbors_distance) != args.k_n:
    
    # if not args.ignore_query_point:
    #     ans = nsearch(points, queries, args.k_n)
    # else:
    #     # [TODO] triger bug, if queried point not exists in pcd
    #     ans = nsearch(points, queries, args.k_n + 1)
    
    neighbors_index = ans.neighbors_index.reshape(num_queries, args.k_n)
    neighbors_distance = ans.neighbors_distance.reshape(num_queries, args.k_n)
    end = time.time()
    print(f'knn with distance eplapsed time {(end - start):.4f} s')
    print(f'knn idx: {neighbors_index}')
    
    if args.vis:
        # o3d.visualization.draw_geometries([pcd])
        print("Visualize the point cloud.")
        # paint all points with specified color except the chosen points and neighbors
        np.asarray(pcd.colors)[:, :] = [0.5, 0.5, 0.5]
        # draw neighbors with specified color
        np.asarray(pcd.colors)[neighbors_index, :] = [0, 1, 0]
        
        vis = o3d.visualization.Visualizer()
        vis.create_window(window_name=f"lego_pointnerf {args.k_n} knn with distance")
        vis.get_render_option().point_size = 1
        opt = vis.get_render_option()
        opt.background_color = np.asarray([0, 0, 0])
        vis.add_geometry(pcd)
        # draw chosen points with specified color by sphere
        for i in idx_chosen:
            sphere = o3d.geometry.TriangleMesh.create_sphere(radius=0.005)
            sphere.paint_uniform_color(np.asarray([1, 0, 0]))
            sphere.translate(pcd_array[i])
            vis.add_geometry(sphere)
        
        vis.run()
        vis.destroy_window()
        
        
if __name__ == '__main__':
    config = args_config()
    knn(config)
    
    # device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    # points = torch.randn([20,3], device=device)
    # queries = torch.randn([10,3], device=device)
    # k = 8
    # nsearch = ml3d.layers.KNNSearch(return_distances=True)
    # ans = nsearch(points, queries, k)
    # # returns a tuple of neighbors_index, neighbors_row_splits, and neighbors_distance
    # # Since there are more than k points and we do not ignore any points we can
    # # reshape the output to [num_queries, k] with
    # neighbors_index = ans.neighbors_index.reshape(10,k)
    # neighbors_distance = ans.neighbors_distance.resh
