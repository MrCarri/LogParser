#!/usr/bin/python

import sys
from classes import reader, job_manager, writer
import argparse
import os

def main():

    print("Starting Lparser\n")

    def parse_main_args():
        parser = argparse.ArgumentParser(description="...")

        parser.add_argument("--workdir", "-wdr", required=True, help="Logs folder path")
        parser.add_argument("--output", "-o", required=True, help="Directory  where output files will be stored")
        parser.add_argument('--pattern', "-p", nargs='+', required = True, help="Patterns")
        parser.add_argument('--extraf',"-ex", required = False, default = True, help="Generate Extra information file if true")

        args = parser.parse_args()

        return args

    args = parse_main_args()
        
    
    # Get PATH from the input would be read
    PATH = args.workdir

    # Get PATH where output will be saved
    OUTPUTPATH = args.output
    if os.path.exists(OUTPUTPATH) is not True:
        raise Exception ("OUTPUT Path ' " + OUTPUTPATH + " ' is invalid or doesn't exist")
    
    # Set default output Name for the raw-files

    output_name =  OUTPUTPATH + "output_file.txt" 
    output_name2 =  OUTPUTPATH + "output_file2.txt" 

    # get all patterns config options
   
    POSSIBLE_MESSAGES = args.pattern
    # find all files we will parse.
    if "True" in args.extraf :
    
        extra_file = True
    else:
        extra_file = False

    file_list = reader.find_directiories(PATH) 
    

    n_files_procesed = len(file_list) 
    print("Number of logs will be procesed: " + str(n_files_procesed))
    print("Path of all the logs: " + PATH )
    print("Files that will be written: ")
    print("    "+ output_name)
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