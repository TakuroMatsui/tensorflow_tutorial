# TensorFlow Tutorial
These codes are based on TensorFlow Tutorial  
https://www.tensorflow.org/tutorials/  
There are ways with Ubuntu 16.04 LTS and Windows 10.


これらのコードはTensorFlowのチュートリアルを基にしました  
https://www.tensorflow.org/tutorials/  
Ubuntu 16.04LTSとWindows 10で実行する方法を説明します。


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
source [created environment name]/bin/activate  
cd [Directory where the code is located]  
python FCNN.py  
python CNN.py

### python 3.6.x  
Execute following commands  
source [created environment name]/bin/activate  
cd [Directory where the code is located]  
python3 FCNN.py  
python3 CNN.py


## Ubuntu 16.04LTS 64bitで実行
Python 2.7.x または 3.6.x 64bit  
TensorFlow 1.4.0

## 始め方
### python 2.7.x
次のコマンドを実行  
sudo apt-get install libcupti-dev  
sudo apt-get install python-pip python-dev python-virtualenv  
virtualenv --system-site-packages [作成する環境の名前]  
source [作成した環境の名前]/bin/activate  
easy_install -U pip  
pip install --upgrade tensorflow

### python 3.6.x
次のコマンドを実行  
sudo apt-get install libcupti-dev  
sudo apt-get install python3-pip python3-dev python-virtualenv  
virtualenv --system-site-packages -p python3 [environment name]  
source [environment name]/bin/activate  
easy_install -U pip  
pip3 install --upgrade tensorflow


## 使い方
### python 2.7.x  
次のコマンドを実行  
source [created environment name]/bin/activate  
cd [Directory where the code is located]  
python FCNN.py  
python CNN.py

### python 3.6.x  
次のコマンドを実行  
source [created environment name]/bin/activate  
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
virtualenv tensorflow  
tensorflow/Scripts/activate  
pip install numpy  
pip install scipy  
pip install tensorflow

## Usage
Execute following commands (administrator authority is not needed)  
tensorflow/Scripts/activate  
cd [Directory where the code is located]  
python FCNN.py  
python CNN.py


## Windows 10 64bitで実行
Python 3.6.x 64bit  
TensorFlow 1.4.0

## 始め方
Pythonのインストール  
https://www.python.org/downloads/ からダウンロード

環境変数のpathに"Python36/" と "Python36/Scripts/"を追加する

次のコマンドを管理者権限付きで実行  
pip install virtualenv  
virtualenv tensorflow  
tensorflow/Scripts/activate  
pip install numpy  
pip install scipy  
pip install tensorflow

## 使い方
次のコマンドを実行する(管理者権限は必要なし)  
tensorflow/Scripts/activate  
cd [コードが配置されているディレクトリ]  
python FCNN.py  
python CNN.py