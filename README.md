# TensorFlow Tutorial
These codes are based on TensorFlow Tutorial  
https://www.tensorflow.org/tutorials/  
There are ways with Ubuntu 16.04 LTS and Windows 10.  
If you want to use GPU, execute "pip install --upgrade tensorflow-gpu" instead of "pip install --upgrade tensorflow."  

## For Ubuntu 16.04LTS 64bit
Python  2.7.x or 3.6.x 64bit  
TensorFlow 1.4.0

## Starting
### python 2.7.x  
Execute following commands  
sudo apt-get install libcupti-dev  
sudo apt-get install python-pip python-dev python-virtualenv  
virtualenv --system-site-packages [environment name]  
source [environment name]/bin/activate  
easy_install -U pip  
pip install --upgrade tensorflow


### python 3.6.x  
Execute following commands  
sudo apt-get install libcupti-dev  
sudo apt-get install python3-pip python3-dev python-virtualenv  
virtualenv --system-site-packages -p python3 [environment name]  
source [environment name]/bin/activate  
easy_install -U pip  
pip3 install --upgrade tensorflow


## Usage
### python 2.7.x  
Execute following commands  
source [environment name]/bin/activate  
cd [Directory where the code is located]  
python FCNN.py  
python CNN.py

### python 3.6.x  
Execute following commands  
source [environment name]/bin/activate  
cd [Directory where the code is located]  
python3 FCNN.py  
python3 CNN.py


## For Windows 10 64bit
Python 3.6.x 64bit  
TensorFlow 1.4.0

## Starting
Install Python  
Download from https://www.python.org/downloads/

Add "Python36/" and "Python36/Scripts/" into your environment variable path

Execute following commands with administrator authority  
pip install virtualenv  
virtualenv [environment name]  
[environment name]/Scripts/activate  
pip install numpy  
pip install scipy  
pip install tensorflow

## Usage
Execute following commands (administrator authority is not needed)  
[environment name]/Scripts/activate  
cd [Directory where the code is located]  
python FCNN.py  
python CNN.py