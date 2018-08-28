#!/usr/bin/python

"""

File with functions for writing the output to the files


"""


def print_errors(errors, output_file, joblist):

    """
    
    Prints the fatal errors, grouped by job, and all the tries for each pkg

    """

    output = open(output_file, "w")
    output.write("List of all jobs / tries that have failed \n")

    failed = 0
    succeed = 0
    for job in joblist.keys():
        if joblist[job].success == True:
            succeed += 1
        else:
            failed += 1
    output.write("failed = " + str(failed) + " succeed = " + str(succeed))
    output.write("\n")

    for i in errors.keys():
        output.write("____________________________________________________________________________________________")
        output.write("\n")
        output.write("\n")
        output.write(i + "\n")
       
        value_anterior = None

        output.write("Traceback of the error: >>> \n\n")
       
        #print(errors[first_key])

        
        
        first = True
        for value in errors[i]:

            if first == True:
                for  msg in value.traceback:
                    output.write("  " + str(msg))
                output.write("\n Jobs affected by the Traceback >>> \n\n")
                first = False

            if value_anterior == None:
                output.write("    " +value.jobname.split("/")[0] + "\n")
                output.write("\n")
                output.write("    " + value.jobname.split("/")[1]+ "\n")
                output.write("\n")


            elif value_anterior.jobname.split("/")[0] == value.jobname.split("/")[0]:

                output.write("    " + value.jobname.split("/")[1]+ "\n")
                output.write("\n")

                output.write("\n")

            else:
                
                output.write("    "+value.jobname.split("/")[0]+ "\n")
                output.write("\n")
                output.write("    " + value.jobname.split("/")[1]+ "\n")
                output.write("\n")



            value_anterior = value



        output.write("\n")
    output.close()

def print_rest(rest, output_file):

    """
    Writes the rest of the messages that are not errors

    """

    output = open(output_file, "w")
    for job in rest.keys():
        job = rest[job]
        output.write("____________________________________________________________________________________________")
        output.write("\n")
        output.write("\n")
        output.write(job.jobname + "\n")
        output.write("Job ended successfully: " + str(job.success) + "\n")
        

        for msg in job.messages:
            output.write(msg + "\n")
        


    output.close()

if __name__ == "__main__":
    pass
