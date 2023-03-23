# Add rotation transformation for modelnet40

# reference:
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.transform.Rotation.html
# reference: http://www.open3d.org/docs/latest/tutorial/Basic/transformation.html

import os
import numpy as np
import argparse
from tqdm import tqdm
import copy
import math
from pathlib import Path

np.random.seed(2021)

def rotation(severity):
    """
        Follow ModelNet40-C config https://github.com/jiachens/ModelNet40-C/blob/master/data/generate_c.py#L19
    """
    c = [2.5, 5, 7.5, 10, 15][severity - 1]
    theta = np.random.uniform(c - 2.5, c + 2.5) * np.random.choice([-1, 1]) * np.pi / 180.
    gamma = np.random.uniform(c - 2.5, c + 2.5) * np.random.choice([-1, 1]) * np.pi / 180.
    beta = np.random.uniform(c - 2.5, c + 2.5) * np.random.choice([-1, 1]) * np.pi / 180.

    matrix_1 = np.array([[1, 0, 0], [0, np.cos(theta), -np.sin(theta)], [0, np.sin(theta), np.cos(theta)]])
    matrix_2 = np.array([[np.cos(gamma), 0, np.sin(gamma)], [0, 1, 0], [-np.sin(gamma), 0, np.cos(gamma)]])
    matrix_3 = np.array([[np.cos(beta), -np.sin(beta), 0], [np.sin(beta), np.cos(beta), 0], [0, 0, 1]])

    r = np.matmul(matrix_1, matrix_2)
    r = np.matmul(r, matrix_3).astype('float32')

    flag = math.isclose(np.linalg.det(r), 1, rel_tol=1e-06)
    if not flag:
        print(np.linalg.det(r))
    assert flag

    return r

def generate_modelnet_rotation(level, root='dataset/modelnet40_normal_resampled'):
    """
        Follow ModelNet40-C config https://github.com/jiachens/ModelNet40-C/blob/master/data/generate_c.py#L19
    """
    severity = level
    save_folder = root + '_rotation' + str(severity)
    SAVE_PATH = Path(save_folder)
    SAVE_PATH.mkdir(exist_ok=True)

    cp_txt = "cp " + root + "/*.txt " + save_folder
    os.system(cp_txt)

    split_type = ['train', 'test']
    for split in split_type:
        shape_ids = {}

        shape_ids['train'] = [line.rstrip() for line in open(os.path.join(root, 'modelnet40_train.txt'))]
        shape_ids['test'] = [line.rstrip() for line in open(os.path.join(root, 'modelnet40_test.txt'))]

        shape_names = ['_'.join(x.split('_')[0:-1]) for x in shape_ids[split]]
        datapath = [(shape_names[i], os.path.join(root, shape_names[i], shape_ids[split][i]) + '.txt') for i
                    in range(len(shape_ids[split]))]
        for index in tqdm(range(len(datapath)), total=len(datapath)):
            fn = datapath[index]
            # print(fn)
            # ('airplane', 'data/modelnet40_normal_resampled/airplane/airplane_0001.txt')
            point_set = np.loadtxt(fn[1], delimiter=',').astype(np.float32)

            # ModelNet-C
            R = rotation(severity)

            point_set[:, :3] = np.matmul(point_set[:, :3], R)
            # [BUG] normal maybe BUG, not sure
            point_set[:, 3:6] = np.matmul(point_set[:, 3:6], R)

            savepath = fn[1].replace(root, save_folder)

            shape_folder = Path(savepath.rsplit('/', 1)[0])
            shape_folder.mkdir(exist_ok=True)

            np.savetxt(savepath, point_set, delimiter=',', fmt='%.6f')

def generate_modelnet_rotationz(name_postfix, angle=60, root='data/modelnet40_normal_resampled'):
    """
        Follow ModelNet40-C config https://github.com/jiachens/ModelNet40-C/blob/master/data/generate_c.py#L19
    """
    severity = name_postfix
    save_folder = root + '_rotation' + str(severity)
    SAVE_PATH = Path(save_folder)
    SAVE_PATH.mkdir(exist_ok=True)

    cp_txt = "cp " + root + "/*.txt " + save_folder
    os.system(cp_txt)

    split_type = ['train', 'test']
    for split in split_type:
        shape_ids = {}

        shape_ids['train'] = [line.rstrip() for line in open(os.path.join(root, 'modelnet40_train.txt'))]
        shape_ids['test'] = [line.rstrip() for line in open(os.path.join(root, 'modelnet40_test.txt'))]

        shape_names = ['_'.join(x.split('_')[0:-1]) for x in shape_ids[split]]
        datapath = [(shape_names[i], os.path.join(root, shape_names[i], shape_ids[split][i]) + '.txt') for i
                    in range(len(shape_ids[split]))]
        for index in tqdm(range(len(datapath)), total=len(datapath)):
            fn = datapath[index]
            # print(fn)
            # ('airplane', 'data/modelnet40_normal_resampled/airplane/airplane_0001.txt')
            point_set = np.loadtxt(fn[1], delimiter=',').astype(np.float32)

            # ModelNet-C
            # R = rotation(severity)
            
            beta = angle * np.pi / 180
            R = np.array([[np.cos(beta), -np.sin(beta), 0], [np.sin(beta), np.cos(beta), 0], [0, 0, 1]])

            point_set[:, :3] = np.matmul(point_set[:, :3], R)
            # [BUG] normal maybe BUG, not sure
            point_set[:, 3:6] = np.matmul(point_set[:, 3:6], R)

            savepath = fn[1].replace(root, save_folder)

            shape_folder = Path(savepath.rsplit('/', 1)[0])
            shape_folder.mkdir(exist_ok=True)

            np.savetxt(savepath, point_set, delimiter=',', fmt='%.6f')


if __name__ == '__main__':
    # Generate ModelNet40-C rotation dataset
    severity = [1, 2, 3, 4, 5]
    for i in severity:
       print(f'Severtity {i}')
       generate_modelnet_rotation(i)

    # generate_modelnet_rotationz("z_60_degree")

    #generate_modelnet_rotationz("z_180_degree", angle=180)
    
    # generate_modelnet_rotationz("z_90_degree", angle=90)
    
    # generate_modelnet_rotationz("z_30_degree", angle=30)

