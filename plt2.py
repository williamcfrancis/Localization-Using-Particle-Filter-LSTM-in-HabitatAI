import torch
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Rectangle
from matplotlib.collections import PatchCollection
import matplotlib.patches as patches
import os
import numpy as np
import sys
import json 
import pickle
import configargparse
import torch.nn.functional as f



if __name__ == "__main__":
    parser = configargparse.ArgumentParser(default_config_files=[])
    parser.add_argument('--traj_num', type=int, default=0, help='the number of trajectory')
    parser.add_argument('--eval_num', type=int, default=0, help='the number of evaluate folder')
    plot_args = parser.parse_args()
    traj_num = plot_args.traj_num
    eval_num = plot_args.eval_num

   
    eval_data = np.load('val_data.npy', allow_pickle='TRUE')
    # print(len(eval_data.item()['trajs']))
    # print(eval_data.item()['map'].shape)
    # print(eval_data.item()['trajs'][0].shape)
    # print(np.unique(eval_data.item()['map']))
  
    robot_traj = eval_data.item()['trajs']

    maze_data = eval_data.item()['map']

    particle_pred = torch.load(os.path.join('eval', str(eval_num), 'particle_pred'), map_location=torch.device('cpu'))
    # print(particle_pred.shape)
    plotmap = np.ones_like(maze_data)
    plotmap[maze_data==1] = 0
    plotmap[maze_data==2] = 0
    plt.figure(figsize=(8,8), dpi=140)
    plt.imshow(plotmap, cmap='gray')
    x_arr = robot_traj[traj_num][:,0]
    y_arr = robot_traj[traj_num][:,1]

    plt.plot(x_arr, y_arr, 'g', label='Ground Truth')
    
    x_list = []
    y_list = []
    for timestep in range(80):
        x = np.mean(particle_pred[:, traj_num, timestep, 0].cpu().data.numpy() * 100 + 50) + np.random.randn()
        y = np.mean(particle_pred[:, traj_num, timestep, 1].cpu().data.numpy() * 100 + 20)
        print(x, y)
        x_list.append(x)
        y_list.append(y)
    plt.plot(x_list, y_list, 'b', label='Predicted')
    plt.legend()
    plt.show()