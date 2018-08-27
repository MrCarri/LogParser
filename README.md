# LogParser

LogParser is a software that works as a logging tool for fast analysis of a great quantity of logs.
It's main target are bad terminated jobs, but can also search for user-defined patterns.

Getting Started

Requeriments:

	 Python 3 installed in your system / virtual enviroment

To install the package, just run the setup.py script and it will copy automatically. 

The command for executing the tool is:

  python3 lparser -wdr PATH -o OUTPUT -p PATTERN (OPTIONAL) -ex True / False 
  

Where each argument is

	--workdir -wdr --> folder where we are going to start searching the .log files
	--output -o    --> Where we want to store result files
	--patterns -p  --> what we are looking for. Good examples are, "ERROR" , "WARNING" etc.
  	--extraf -ex   --> If we want an extra info file (True by default)
  
Another thing that should be beared in mind is that the keyword ERROR for the pattern is treated as an special case. 
IF present, one of the output files would be dedicated exclusively to errors that end the execution, and the other one to the rest of info. 

Built With


	- Python 3
	- Glob
	- Sequence matcher (difflib)


Contributing


Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests to us.

Authors


	Alexandre Carrillo - main developer 

License

This project is licensed under the MIT License - see the LICENSE.md file for details
