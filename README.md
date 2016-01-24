Details
=======

I'm working on a python3 script to download zip files from IEA website. However, i dont know how to clear the pop-up authentication before proceeding to download my zip files. 

The final script only has to do the following:
 1. handle pop-up authentication 
 2. download zip file

login details cant be shared for obvious reason. I will test out the script as soon as it's sent to me.


Installation and usage
======================

1. source `intall.sh`:

 . ./install.sh

2. set up environment variables **IEA_USER** and **IEA_PWD** (or change the default value variable values in the script):

 export IEA_USER=...
 export IEA_PWD=...

3. run `download.py`:

 ./download.py

