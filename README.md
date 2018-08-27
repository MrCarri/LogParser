# LogParser

LogParser is a software that works as a logging tool for fast analysis of a great quantity of logs.
It's main target are bad terminated jobs, but can also search for user-defined patterns.

## Getting Started

### Requeriments:

	 Python 3 installed in your system / virtual enviroment

To install the package, just run the setup.py script and it will copy automatically. 

The command for executing the tool is:

 	python3 lparser -wdr PATH -o OUTPUT -p PATTERN -ex True / False (OPTIONAL) 
  

Where each argument is

	--workdir -wdr --> folder where we are going to start searching the .log files
	--output -o    --> Where we want to store result files
	--patterns -p  --> what we are looking for. Good examples are, "ERROR" , "WARNING" etc.
  	--extraf -ex   --> If we want an extra info file (True by default)
 
### About outputFiles:

2 files are created unless specified otherwhise:

* outputfile 1 is the exclusive file for fatal errors and execution-time issues with the code 
* outputfile 2 is a more detailed information about every job, the good ones and the bad ones and it depends on the patterns.


### About patterns:

Any keyword might be used, but the keyword  **"ERROR"** is the most important (not case sensitive). If set as a pattern, aall **Fatal Errors** will appear in the outputfile 1. The rest of the errors (possible controlled exceptions and other) will appear in output file 2, wich is optional, so -ex flag should be ommited or set to True.

### About extraf argument:

This argument is optional, it's main purpose is to not generate the optional textfile if we don't  have much space in disk, because It would be bigger than the main output file. 

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
