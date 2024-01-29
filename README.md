# DYNAMIC ADAPTATION OF DIGITAL WORKSAPCE
This repository contains the design and implementation of an adaptive system using a Machine Learning model to mutate the digital workspace. It supports dynamic change brought in by predictions made by the ML model to dynamically change your underlying system's low-level functions without your explicit intervention. The goal is to optimise your computational resources and create a more efficient digital workspace for you.



## DESCRIPTION

To create an optimized digital workspace that undergoes adaptation based on the task a user is performing, two basic things are required:
1.	Correct identification of the task- using a tuned Machine Learning Model RANDOM FOREST CLASSIFIER
2.	Implementation of Dynamic Adaptation- interaction with OS APIs using Python programs to change low-level system functionalities using various Python Libraries 

Accurate recognition of human activity by training an ML model allowed me to optimise computational resources by developing a Python script that modified functions such as Battery Plans and Display Settings.

## DATASET USED
My dataset was derived from the dataset provided on Kaggle as supporting evidence for the paper published with the citation mentioned below:

_Srivastava, N., Newn, J., & Velloso, E. (2018). Combining Low and Mid-Level Gaze Features for Desktop Activity Recognition. Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies, 2(4), 189_

[Link to dataset](https://www.kaggle.com/datasets/namratasri01/eye-movement-data-set-for-desktop-activities)

## TECH STACKS USED

**FOR MACHINE LEARNING:**

pandas, sklearn (scikit-learning), imblearn (imbalanced learning)

Special Classes/Methods of imblearn:

SMOTE, RandomUnderSampler, make_pipeline

**FOR PYTHON PROGRAM ENABLING ADAPTIVE FUNCTIONALITY:**

ctypes to access system-level functionality under due control and support of the Windows OS

_Display Settings:_

sbc installed from pypi, user32, gdi32, NumPy

_Battery Plans:_

winreg, subprocess

## !CAUTION
Please be aware that changing display settings can have unintended consequences, such as temporarily disrupting the display or causing compatibility issues with certain applications. Use this script at your own risk, and be sure to understand the potential implications before applying it.

## INSTALLATION
#### CODE WILL WORK FOR ONLY WINDOWS OS SYSTEMS
#### Please run on a Jupyter notebook as it may be unable to render here
The iPython notebook labelled as adaptive_workspace.ipynb must be downloaded onto the local system by the user. You may use a Jupyter Notebook or any IDE to execute this script on. 

Since the program targets better battery health and performance triggered based on the activity being performed by the user, the underlying system functionalities are being accessed and modified. Therefore, please grant administrative privilege to the IDE you work with.

For experiencing the varied changes brought in by use of this program, manual switching of datasets will have to be done since real time-datapoints cannot be fed to the model for the lack of technical hardware to support tracking of eye-movement. 

Please refer to the following table in order to understand the data split and while going through the code make the alterations as specified in the comments after cross-verification.

![image](https://github.com/advikasinha/BYOP_24_END/assets/152763494/34b63ec1-5bd2-4146-adea-bfae3bff6f87)

All six datasets are provided in a folder named as test_datasets in the repository. Please choose the activity from the above table you want to execute the code for and make changes in the code accordingly.

Places to make the change in code at:

1. ![image](https://github.com/advikasinha/BYOP_24_END/assets/152763494/bb3a9c8a-7bca-4170-97a0-e88576a8882c)
2. ![image](https://github.com/advikasinha/BYOP_24_END/assets/152763494/b615d8cd-1ffd-46e6-91cb-308725330d58)
3. ![image](https://github.com/advikasinha/BYOP_24_END/assets/152763494/ebe93364-5e57-4c20-802e-137bd0606495)

## CHALLENGES FACED AND LIMITATION
ML BASED CHALLENGES

The imbalanced nature of the preliminary dataset fed resulted in a lot of time and resource devotion into resampling and hypertuning of the chosen model. At the time of BYOP I do not have a laptop that can bear a lot of computational expense so models like XGBoost were less preferred for training and testing the final dataset.

I manually subjected extra subsets of an n number of participants for the majority classes to processing such that general trend of the activity plot was not lost and these data points could be added to the training dataset to make the classes more balanced and easier for the model to work with. This has fixed issues with minority classes of BROWSE and DEBUG but code defaults to READ when subjected to WRITE targetting dataset due to similar nature of range and scatter of datapoints according to my estimate.

CHALLENGES FACED WHILE WORKING WITH WINDOWS API

For system wide modification of settings, elevated privileges are required. Changing refresh rates or any hardware/sys config is a low level task and with the correct python coding, these settings can be manipulated and modified. But after countless variations of code producing error DISP_CHANGE_BADFLAGS, for the due course of BYOP, the specific config of my graphics hardware is not allowing display or modification of refresh rate for any of the 4 displays my system supports.

Due to underlying system configuration restrictions, I have now ended the BYOP phase by adaptation of brightness and battery plans only. 

The whole application has limited features that it can modify of the underlying system because of time constraints and incomprehensive knowledge of the OS at this time.




