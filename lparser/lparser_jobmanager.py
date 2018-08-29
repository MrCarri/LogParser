#!/usr/bin/python

from lparser import lparser_job as job

class manager:

    """

    Interface Class that manages all jobs. Adds new ones, stores them, and collects data about them


    """

    def __init__(self):

        """
        Constructor 
        """

        self.joblist = {}
        self.num_jobs = len(self.joblist.keys())

    def run(self, file_list, POSSIBLE_MESSAGES):

        """
        Manager main method. Opens file, and makes the calls to analyze the line.

        params:
            file list
            POSSIBLE_MESSAGES = all filters setted up in paramethers 
    
        return:

            dictionary with all errors found
        """
        n_files_procesed = 0
        for file in file_list:
            opened_file = open(file, "r")
            job = self.add_newjob(file) # we add a job for each file
            line_before = None
            for line in opened_file:
                msg = job.analyze_line(line, POSSIBLE_MESSAGES, line_before)
                if msg is not None: # message is relevant, not useless
                    job.add_message(msg)
                line_before = line
        
            opened_file.close()
            n_files_procesed += 1
            print(str(n_files_procesed)+ "/" + str(len(file_list)) + " Logs Completed "+ "\r" , end="") # progress bar

        
        self.print_ratios()
        errors = self.analyze_errors()
        return errors

      
    def add_newjob(self, log):

        """
        Function that adds a new job. 

        Params: 
            log = job log to be added
        returns the job
    
        """

        new_job = self.create_job(log)
        new_id = self.num_jobs
        self.joblist[new_id] = new_job
        self.num_jobs += 1
        return new_job

    def print_ratios(self):

        """
        Method that prints the failed and successful jobs

        """
        
        failed = 0
        succeed = 0
        for job in self.joblist.keys():
            if self.joblist[job].success == True:
                succeed += 1
            else:
                failed += 1
        print ("failed = " + str(failed) + " succeed = " + str(succeed))
        

    def get_jobname(self, log):

        """
        Gets job name:
        params:

            log = log that we want the name to be processed

        returns:

            jobname processed
    
        """

        package_name = log.split("/")[-2]
        filename = log.split("/")[-1]

        jobname = package_name + "/" + filename
        return jobname

    def create_job(self, log):

        """
        Calls to job creation using a log of a job

        params:

            job log

        returns:
            new_job = new job created
        
        """

        jobname = self.get_jobname(log)
        new_job = job.create_job(jobname)
        
        return new_job



    def get_joblist(self):

        return self.joblist

    def analyze_errors(self):

        """
        Function that analyzes errors

        returns all failed jobs

        """

        
        failed_jobs = {}

        for job in self.joblist.keys():
            
            # this is shortcutting the variable self.joblist[job], to make less access to dictionary than necessary
            job = self.joblist[job] 

            # If the job has a traceback, it has been marked as failed(has task_error,1) and we have a motive for the crash, it's a failed job.

            if job.traceback is not None and job.success is False and job.crash_culprit is not None:
                
                # if we don't have that case yet, we add it as a new case
                if job.crash_culprit not in failed_jobs.keys():
                    
                    failed_jobs[job.crash_culprit] = [job]
                # else, the case happened before already, we add it to the times it happened
                else:
                    
                    failed_jobs[job.crash_culprit].append(job)
        return failed_jobs

if __name__ == "__main__":
    pass
