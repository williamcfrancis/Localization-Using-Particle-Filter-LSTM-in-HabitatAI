# Group ID: 66
# Rashmi Phadnis, William C. Francis, Harshini Vikram

# Setup
1. To install required libraries, run the 'pip install -r requirements.txt' command to setup on local machine

# Training
## Generating dataset
For the Habitat AI part of the code, we have a 'Trajectory_Generation.ipynb' file. You will need to run that on Google Colab to interface with the simulator and generate 2 files - train_data.npy, val_data.npy
These files are already provided in the folder
## Changing Configurations
Currently, the number of epochs is set as 800 for training. To change that, go to configs/train.conf and edit the default parameters.
## Train Loop
To run the train loop, run the following command on terminal:
python main.py -c ./configs/train.conf


# Inference
For running inference, run the following command:
python evaluate.py -c ./configs/eval.conf

This will save the generated particle tensors in ./eval


# Plotting
Run the following command:
python plt2.py --traj_num 0 
(You can put any number from 0 to 499 since there are 500 eval trajectories)


# Contribution Distribution
Report: Equal contribution
0. Exploring Habitat AI - Harshini
1. Map generation and landmark insertion - William
2. Trajectory Generation - Rashmi
3. PF-LSTM - Equal Contribution
 
