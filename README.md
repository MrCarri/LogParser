# LogParser

LogParser is a software that works as a logging tool for fast analysis of a great quantity of logs.
It's main target are bad terminated jobs, but can also search for user-defined patterns. The idea is to make a summary of python Logs making the debugging easier. 

## Getting Started

### Requeriments:

	 Python 3 installed in your system / virtual enviroment

First, clone the repository in your system or go to releases and download the .zip with all the package prepared.

To install the package, just run the setup.py script inside the .zip and it will copy automatically.
		
	python3 setup.py install

The example command for executing the tool is:

 	python3 PATH_TO_LPARSER -wdr PATH -o OUTPUT -p PATTERN -ex True / False  

Where each argument is

	--workdir -wdr --> folder where we are going to start searching the .log files
	--output -o    --> Where we want to store result files
	--patterns -p  --> what we are looking for. Good examples are, "ERROR" , "WARNING" etc.
  	--extraf -ex   --> If we want an extra info file 


## About the different arguments:

Every execution argument is optional. If --output or --workdir are not specified, the current directory would be taken. If pattern is empty, it will use the default, which is "ERROR". If -ex, it will generate outputfile 2

### About patterns:

The important pattern is "ERROR" in order to detect fatal errors, but others can be specified (whatever you want to search, for example "WARN" "CITICAL" or "EXCEPTION"). If its the case, remember to add -ex, for generating a second file for the non fatal error patterns we are looking for. It's not case sensitive.


### About outputFiles:

2 files can be created, depending on --extraf argument

* outputfile 1 is the exclusive file for fatal errors and execution-time issues with the code 
* outputfile 2 is a more detailed information about every job, the good ones and the bad ones and it depends on the patterns.





## Built With:


	- Python 3
	- Glob
	- Sequence matcher (difflib)


## Contributing:


Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests to us.

## Authors:


	Alexandre Carrillo - main developer 

## License:

This project is licensed under the MIT License - see the LICENSE.md file for details
