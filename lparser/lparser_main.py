#!/usr/bin/python

import sys
from lparser import lparser_reader as reader
from lparser import  lparser_jobmanager as job_manager
from lparser import lparser_writer as writer
import argparse
import os

def main():

    print("Starting Lparser\n")

    
    def parse_main_args():
        parser = argparse.ArgumentParser(description="...")

        parser.add_argument("--workdir", "-wdr", required=False, default = os.getcwd(), help="Logs folder path")
        parser.add_argument("--output", "-o", required=False, default = os.getcwd(), help="Directory  where output files will be stored")
        parser.add_argument('--pattern', "-p", nargs='+', required = False, default=None, help="Patterns")
        parser.add_argument('--extraf',"-ex", required = False, action="store_true", help="Generate Extra information file if true")

        args = parser.parse_args()

        return args
    
    args = parse_main_args()
        
    
    # Get PATH from the input would be read
    PATH = args.workdir
    print(PATH)

    # Get PATH where output will be saved
    OUTPUTPATH = args.output
    if os.path.exists(OUTPUTPATH) is not True:
        raise Exception ("OUTPUT Path ' " + OUTPUTPATH + " ' is invalid or doesn't exist")
    
    # Set default output Name for the raw-files

    output_name = os.path.join(OUTPUTPATH, "output_file.txt")
    output_name2 = os.path.join(OUTPUTPATH, "output_file2.txt")
   
    # get all patterns config options

    POSSIBLE_MESSAGES = []
    if args.pattern is None:
        POSSIBLE_MESSAGES =["ERROR"]
    else:
        for pattern in args.pattern:
            POSSIBLE_MESSAGES.append(str(pattern.upper()))
    
    
    # find all files we will parse.

    extra_file = args.extraf
    print(extra_file)
    file_list = reader.find_directiories(PATH) 
    

    n_files_procesed = len(file_list) 
    print("Number of logs will be procesed: " + str(n_files_procesed))
    print("Path of all the logs: " + PATH )
    print("Files that will be written: ")
    print("    "+ output_name)
    if extra_file == True:
        print("    "+ output_name2)
    print("\nResults! \n")


    if n_files_procesed == 0:
        raise Exception("No files found!")
    # create job manager
    
    manager = job_manager.manager()

    # run job manager and get everything to be written in the files

    errors = manager.run(file_list, POSSIBLE_MESSAGES)
    joblist = manager.get_joblist()
    writer.print_errors(errors, output_name, joblist)
    
    if extra_file == True:
        
        writer.print_rest(joblist ,output_name2)



    print("Ended successfully")
main()
