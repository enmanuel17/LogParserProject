# LogParserProject
This is the code for third udacity project. The code allows you to use python to interface with a postgresql database. psycopg2 was the python-db API implemented in this project.

Some of the installing and setting up instructions were provided by udacity.

### Downloads

The code can be downloaded from the following repo:

https://github.com/enmanuel17/LogParserProject.git

## REQUIREMENTS:
### Python 3 ONLY. How to get/install Python https://www.python.org/downloads/
Install the following python libraries:

- psycopg2
```pip3 install psycopg2```
for more info regarding the library look here http://initd.org/psycopg/docs/install.html

The code also needs a backend server that runs the database. To accomplish that, we will need to install and run
the following software on that order:

### How to get/install VirtualBox
We will be using virtual box to create a virtual machine for running our server.
You can download it from https://www.virtualbox.org/wiki/Download_Old_Builds_5_1, here. Install the platform package for your operating system. You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it; Vagrant will do that.

### How to get/install Vagrant
We will be using vagrant to configure the necessary packages for the server to run.
Download Vagrant from https://www.vagrantup.com/downloads.html and install the version for your operating system.
Once that is completed, git clone the vagrant configuration file we are going to use https://github.com/udacity/fullstack-nanodegree-vm.git
cd into the clone and hange to this directory in your terminal with cd. Inside, you will find another directory called vagrant. Change directory to the vagrant. Once in there, run vagrant up. (This will take a while the OS is download, install and configured.)
When vagrant up is finished running, you will get your shell prompt back. At this point, you can run vagrant ssh. Now you are in your db server.

### How to get the database
Download the database data from here https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip . You can use the wget command to download zip file from within the VM. Once dowloaded, use the unzip command to extract the contents in the /vagrant directory inside the VM. The file inside is called newsdata.sql.
use the command psql -d news -f newsdata.sql inside the VM to populate the database server with the database.

## Views needed
Please create this view before running the code:
```create view dates as```
```select cast(time as date) as date from log group by cast(time as date);```



## How to Use:

The application can be run with the following ways:
- Typing ```python dbParselog.py``` from the linux command line.

## LICENSE
MIT License

Copyright (c) 2017 Enmanuel Hernandez

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

