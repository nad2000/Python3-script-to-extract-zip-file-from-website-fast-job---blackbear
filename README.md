# Python3 Sripts for File Download and Handling

Table of Contents
=================

  * [Python3 Sripts for File Download and Handling](#python3-sripts-for-file-download-and-handling)
    * [Original Desctipions](#original-desctipions)
      * [Task #1: Python3 script to extract zip file from website (fast job)](#task-1-python3-script-to-extract-zip-file-from-website-fast-job)
  * [Details](#details)
      * [Task #2: Python3 script to download XLS workbooks](#task-2-python3-script-to-download-xls-workbooks)
    * [Installation and usage](#installation-and-usage)
  * [Usage with MS Windows](#usage-with-ms-windows)


## Original Desctipions

### Task #1: Python3 script to extract zip file from website (fast job)

> Details
> =======
> 
> I'm working on a python3 script to download zip files from IEA website. However, i dont know how to clear the pop-up authentication before proceeding to download my zip files. 
> 
> The final script only has to do the following:
>  1. handle pop-up authentication 
>  2. download zip file
> 
> login details cant be shared for obvious reason. I will test out the script as soon as it's sent to me.

### Task #2: Python3 script to download XLS workbooks

> need python script to extract all the xls and compile into workbooks from "http://www.eppo.go.th/info/cd-2015/index.html". 
> workbooks will be titled "CHAPTER 1 : ENERGY SITUATION IN 2014" ... "CHAPTER 9 : AIR POLLUTION EMISSION IN THE ENERGY SECTOR"

## Installation and usage

1. source `intall.sh`:
```
. ./install.sh
```

2. set up environment variables **IEA_USER** and **IEA_PWD** (or change the default value variable values in the script):

```
export IEA_USER=...
export IEA_PWD=...
```

3. run `download.py` to download ZIP file:

```
 ./download.py
```

4 to download XLS workbooks:

```
 ./download_xls.py
```

## Usage with MS Windows

1. set up environment variables **IEA_USER** and **IEA_PWD** (or change the default value variable values in the script):

```
set IEA_USER=...
set IEA_PWD=...
```

2. run `download.py`:

```
python3 ./download.py
```
