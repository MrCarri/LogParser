#!/usr/bin/python


import os

from glob import glob

from difflib import SequenceMatcher

import sys


def find_directiories(start_dir):

    """
    Function that Gets all files in a folder using glob and os.walk.

    params:
        - start_dir: Directory where we start searching recursively
    
    returns:

        - list with all files, including absolute PATHS

    """

    files = []
    
    pattern   = "*.log"

    for dir,_,_ in os.walk(start_dir):
        files.extend(glob(os.path.join(dir,pattern))) # MAGIC!

    return files



