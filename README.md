<img src="https://github.com/allexlima/WavaImageDatasetProcessing/blob/master/img/pinwheel.png?raw=true" width="64">
### Welcome to Wava Image Dataset Processing

This software was designed to improve the time of manual digital images processing of big image datasets

![](https://github.com/allexlima/WavaImageDatasetProcessing/blob/master/img/hsv_settings.png?raw=true)  

### Requirements [not pip-installable]

1. **Python 2.7.x** 

    Download Python 2.7.x interpreter [here](https://www.python.org/).

2. **OpenCv**

    You can use [this](http://milq.github.io/install-opencv-ubuntu-debian/) or [this](http://www.pyimagesearch.com/2015/06/22/install-opencv-3-0-and-python-2-7-on-ubuntu/) tutorial to install OpenCv in your unix-like system.

3. **PyQt4** 

    * If you are using a Debian-like system, you can install it using the following command:

        ```bash
        $ sudo apt-get install python-qt4
        ```
     
    * If you are using OS X:
    
        ```bash
        $ brew install pyqt
        ```
    * You can also find a compatible version for your system in [oficial PyQt website](https://www.riverbankcomputing.com/software/pyqt/download).
    
### Pip-installable Libraries

  ```bash
  $ pip install numpy scipy
  ```
  
#### Setup

1. Clone the repo
            
    ```bash
    $ git clone https://github.com/allexlima/WavaImageDatasetProcessing.git
    $ cd WavaImageDatasetProcessing/
    ```

2. Run **WavaImageDatasetProcessing**
   
   - You can **install** WavaImageDatasetProcessing in your Unix-like system running `setup.sh` file as sudo or root:
   
        ```bash
        $ sudo ./setup.sh
        ```   
        
        and type `i` to proceed installation. If you want to remove WavaImageDatasetProcessing, you just need run the `setup.sh` file and type `r` to uninstall from your PC.
   
   - Or **just run** it:
   
        ```bash
        $ python app.py
        ```
            
