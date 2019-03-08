# DeepRL_Banana
DRL Agent to collect Bananas in Unity environment


# Project: Navigation in a banana world

### Intro

[//]: # (Image References)

[image1]: https://user-images.githubusercontent.com/10624937/42135619-d90f2f28-7d12-11e8-8823-82b970a54d7e.gif "Trained Agent"


This projects goal is to utilize Deep Reinforcement Learning (DRL) to train an agent to navigate through 2 dimensional environment and collect yellow bananas, while avoiding to collect blue bananas.

A trained agent will can be seen in below image: 

![Trained Agent][image1]
(source: https://github.com/udacity/deep-reinforcement-learning/blob/master/p1_navigation/README.md)

### Environment
In RL the environment defines what the agent will learn. In this case the environment allows the agent to choose between 4 actions in each timesequence:

- **`0`** - move forward.
- **`1`** - move backward.
- **`2`** - turn left.
- **`3`** - turn right.

The state space in contrast is not discrete, but continuous and is perceived by the agent in 37 dimensions. (37 continuous input features)

The rewards of the environment, which serve as reinforcement for the agent to learn, are assigned when its rules are fullfilled:

A reward of +1 is provided for collecting a yellow banana, and a reward of -1 is provided for collecting a blue banana.  Thereby the agent will learn to avoid blue bananas while collecting yellow bananas.

The task is episodic. To solve the problem the average score must exceed +13 for at least 100 episodes.

### How to use this Github repository to train an agent to solve the banana world

The following system prerequisites are required to get it running with my instructions:

- Windows 10 64-Bit.
- Anaconda for Windows.
- GPU with CUDA support(this will not run on CPU only, as its explicitly disabled).
    Cudatoolkit version 9.0.

#### Setting up the Anaconda environment

- Set up conda environment with Python >=3.6
	- Conda create –name <env_name> python=3.6
- Install Jupyter Kernel for this new environment.
    - python -m ipykernel install --user --name <Kernel_name> --display-name "<kernel_name>".
- Download ML-Agents Toolkit beta 0.4.0a.
   - https://github.com/Unity-Technologies/ml-agents/releases/tag/0.4.0a
- install it by running following command, with activated conda environment in the directory of ml-agents, that contains the setup.py.
   - pip install -e . .
- install PyTorch.
    - conda install pytorch torchvision cudatoolkit=9.0 -c pytorch.
- Get Unity Environment designed for this Banana project.
   -  Windows (64-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86_64.zip).
    - Place the file in the DRLND GitHub repository, in the `p1_navigation/` folder, and unzip (or decompress) the file. 

### Instructions

Follow the instructions in `Navigation.ipynb` to get started with training your own agent!  

### (Optional) Challenge: Learning from Pixels

After you have successfully completed the project, if you're looking for an additional challenge, you have come to the right place!  In the project, your agent learned from information such as its velocity, along with ray-based perception of objects around its forward direction.  A more challenging task would be to learn directly from pixels!

To solve this harder task, you'll need to download a new Unity environment.  This environment is almost identical to the project environment, where the only difference is that the state is an 84 x 84 RGB image, corresponding to the agent's first-person view.  (**Note**: Udacity students should not submit a project with this new environment.)

You need only select the environment that matches your operating system:
- Linux: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/VisualBanana_Linux.zip)
- Mac OSX: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/VisualBanana.app.zip)
- Windows (32-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/VisualBanana_Windows_x86.zip)
- Windows (64-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/VisualBanana_Windows_x86_64.zip)

Then, place the file in the `p1_navigation/` folder in the DRLND GitHub repository, and unzip (or decompress) the file.  Next, open `Navigation_Pixels.ipynb` and follow the instructions to learn how to use the Python API to control the agent.

(_For AWS_) If you'd like to train the agent on AWS, you must follow the instructions to [set up X Server](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Training-on-Amazon-Web-Service.md), and then download the environment for the **Linux** operating system above.
