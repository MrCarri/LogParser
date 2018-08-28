#!/usr/bin/python


def create_job(jobname):

    """
    Dummy function that creates a job. 

    """
    return job(jobname)


class job:

    """
    Job class. Every try of each package is considered a different job. 
    Contains all methods relative to the jobs.

    Never call it directly, use lparser_jobmanager instead.

    """

    class message:

        """
        Class for messages, it has 3 attributes:

            category : type of message
            line: message per se, the line as it appears in the log
            id: assigned unique id

        """

        def __init__(self, category, line, id):
            self.id = id
            self.category = category
            self.line = line

    def __init__(self, jobname):

        """
        
        job constructor

        params: 

            jobname: name of the job that is assigned by manager

        """

        self.jobname = jobname
        self.messages = [] # different msg storage
        self.success = True # by default, a job always will be successful unless proved otherwise
        #self.traceback = None # same as above
        self.traceback = []
        self.crash_culprit = None # same as above above



    def add_message(self, msg):

        """
        Add a message function. Gets a message, splits it into the interesting parts, check if we already
        have it (we might) and then joins it again formated and after that is stored

        params: 

            message

        """
        splitted_msg = msg.line.split(" ")[1:]
        splitted_msg = " ".join(splitted_msg)
        if not self.already_got_message(splitted_msg):
            self.messages.append(splitted_msg)

    def already_got_message(self, msg):

        """

        checks if we already have the message in self.messages

        """
        if msg in self.messages:
            return True
        else:
            return False

    def analyze_line(self, line, POSSIBLE_MESSAGES, line_before):


        """
        Function that analyzes a line. Special cases (ERRORS that made the job end) are treated differently
        as special cases.

        params:
            line : to analyze
            POSSIBLE_MESSAGES: options / filters / patterns we are looking for
            line_before: Line that was processed last iteration, its for traceback setting

        """


        # Start of special case 1 
        # This is for setting where the job has crashed (if It has)
        # Tries to find tracebacks, the line that has generated it
        # and if the message "task_error" appears

        if "error".upper() in POSSIBLE_MESSAGES: # we are monitoring the job crashes
            if "task_error,1" in line: # This string demostrates job failed.
                self.success = False
            elif "file" and "line" in line: 
                #self.traceback = line # this should get us last traceback line, that where the job has failed
                self.traceback.append(line)

            # if we find a traceback line, we use the line that was executed just before, which is the one 
            # that says how happened (traceback line is not useful per se, but the line before it IS)    
            elif "Traceback" in line: 
                self.crash_culprit = line_before.split(" ")[1:]
                self.crash_culprit = " ".join(self.crash_culprit)
                self.traceback = []
            

        # End of special case 1

        # If its not a fatal error, we check if the line is one of the message we are looking for
        # such as WARNINGS, CRITICAL, or whatever we want

        for category in POSSIBLE_MESSAGES:
            if category.lower() in line.lower():
            
                msg = self.message(category, line, len(self.messages)) # stores the message if its relevant, and assigns an id

                return msg
       
        return None # if its irrelevant, we simply return None


if __name__ == "__main__":
    pass
