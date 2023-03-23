import numpy as np
import argparse

# 定义旋转矩阵
angle = 15/180 * np.pi
cosval = np.cos(angle)
sinval = np.sin(angle)
rotation_matrix = np.array([[cosval, 0, sinval],
                            [0, 1, 0],
                            [-sinval, 0, cosval]])

def parse_args():
    # PARAMETERS
    parser = argparse.ArgumentParser('Rotation')
    parser.add_argument('--name',type=str,default=None)
    return parser.parse_args()

def main(args):  
    bin_file = args.name
    f = np.fromfile(bin_file,"float32")
    scale = int(len(f[1:]))
    a = f[1:].reshape(int(scale/11),11)
    
    # 对点云数据进行旋转处理，包括法向量
    for i in range(0,int(scale/11)):
        xyz = a[i][0:3]
        normal = a[i][3:6]
        xyz = np.dot(xyz,rotation_matrix)
        normal = np.dot(normal,rotation_matrix)
        a[i][0:3] = xyz
        a[i][3:6] = normal
    a = a.reshape(1,scale)
    f[1:] = a
    # f.tofile(bin_file) # 暂时不需要将文件保存

if __name__ == '__main__':
    args = parse_args()
    main(args)
