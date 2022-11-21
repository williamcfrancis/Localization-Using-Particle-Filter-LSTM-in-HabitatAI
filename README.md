## Robot Localization using Particle Filter LSTM with Habitat AI

This project explores the use of a new family of Long Short Term Memory networks applied to the problem of robot localization in the AI Habitat simulator. The LSTM used is a Particle Filter-LSTM which employs particle filtering as the embedded algorithmic prior. Several experiments are conducted to test the PF-LSTM by generating trajectories and collecting observations in Habitat simulator. The 3D-World in Habitat AI is converted to a 2D map to use as an input. Landmarks were introduced to provide 2D observations instead of 3D sensors. The results are evaluated by comparing the deviation of the resulting trajectories from PF-LSTM and the ground truth trajectories from the simulation. The estimated trajectories averaged an MSEof 0.4 from the ground truth, for a justifiable trade-off of reduction in training data by almost 460 times.
![image](https://user-images.githubusercontent.com/38180831/203159744-506b3550-71d3-4ef6-9059-92a1a6a1a9b5.png)
![image](https://user-images.githubusercontent.com/38180831/203159866-3b578832-7369-48ca-82ce-d4c66250cded.png)

## Setup
1. To install required libraries, run the `pip install -r requirements.txt` command to setup on local machine

## Training
### Generating dataset
For the Habitat AI part of the code, we have a 'Trajectory_Generation.ipynb' file. You will need to run that on Google Colab to interface with the simulator and generate 2 files - train_data.npy, val_data.npy
These files are already provided in the folder
### Changing Configurations
Currently, the number of epochs is set as 800 for training. To change that, go to configs/train.conf and edit the default parameters.
### Train Loop
To run the train loop, run the following command on terminal:\
`python main.py -c ./configs/train.conf`


### Inference
For running inference, run the following command:\
`python evaluate.py -c ./configs/eval.conf`

This will save the generated particle tensors in ./eval


### Plotting
Run the following command:\
`python plt2.py --traj_num 0`\
(You can put any number from 0 to 499 since there are 500 eval trajectories)
 
## Qualitative Results

![image](https://user-images.githubusercontent.com/38180831/203160003-f3626f0d-98af-4ef7-ad54-dd4022c38d3c.png)


## Quantitative Results

![image](https://user-images.githubusercontent.com/38180831/203160120-9cfc2a90-51f4-4598-a4f3-b681bbf71775.png)
