# Version_Update

## About project?

This project helps to create versions from input and track them  

## How it's working?

1. Checks if there is file called version. If not - creates new 
2. Checks if in version file have line with patter like 1.0.0. If not - deletes everything from file and add 1.0.0
3. Checks what input came, input should be: major, minor or patch
4. Increment version value depends on input
* if major, then from 1.0.0 to 2.0.0
* if minor, then from 1.0.0 to 1.1.0 
* if patch, then from 1.0.0 to 1.0.1
5. If not exists, create file called version_log and write in it update log like:
![q](https://ibb.co/1tcCdZk1)

## How to use it?

* Download zip file of this project and unwrap it

* Download python from official site https://www.python.org/downloads/. Write this command to make sure it's installed

![q](https://ibb.co/mrYn8BWd)

* Go to the directory with version_up.py file 
 
![q](https://ibb.co/JRQ09bHF)

* Type python version_up.py

![q](https://ibb.co/3Y4Mwkgz)

* Enter update type (major, minor, patch)

![q](https://ibb.co/dvxQLsz)

* Check version and version_log files

![q](https://ibb.co/xKCdgBgH)

![q](https://ibb.co/LzjgLxxm)
