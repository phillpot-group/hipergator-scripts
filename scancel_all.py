#!/usr/bin/env python

import os
import subprocess


if __name__ == "__main__":
    args = "squeue -u CUSTOM"           # replace CUSTOM with your hipergator username
    output = subprocess.getoutput(args) # get the text output of the prior command
    lines = output.split("\n")          # split the output into a list of lines
    for line in lines[1:]:              # ignore the first header line
        segments = line.split()         # split by spaces
        jobid = segments[0].strip()     # get the jobid from the output
        cmd = ["scancel", jobid]        # construct the cancellation command
        subprocess.Popen(cmd).wait()    # execute the command and await completion
