# Version_Update

# About project?

This project helps to create versions from input and track them  

# How it's working?

1. Checks if there is file called version. If not - creates new 
2. Checks if in version file have line with patter like 1.0.0. If not - deletes everything from file and add 1.0.0
3. Checks what input came, input should be: major, minor or patch
4. Increment version value depends on input
* if major, then from 1.0.0 to 2.0.0
* if minor, then from 1.0.0 to 1.1.0 
* if patch, then from 1.0.0 to 1.0.1
5. If not exists, create file called version_log and writes in it update log like that:
  
    ![q](https://i.ibb.co/dwZNLBRF/Screenshot-9.png)

# How to use it?

* Download zip file of this project and unwrap it

* Download python from official site https://www.python.org/downloads/. Write this command to make sure it's installed

     ![q](https://i.ibb.co/JWbYQdJ8/Screenshot-10.png)

* Go to the directory with version_up.py file 
 
     ![q](https://i.ibb.co/4Zd9HDpg/Screenshot-12.png)

* Type python version_up.py
 
     ![q](https://i.ibb.co/6Jr12NjB/Screenshot-13.png)

* Enter update type (major, minor, patch)

     ![q](https://i.ibb.co/TGdHbDF/Screenshot-14.png)

* Check version and version_log files

     ![q](https://i.ibb.co/ZRL7gFgm/Screenshot-15.png)

     ![q](https://i.ibb.co/VWnC7ggR/Screenshot-16.png)
