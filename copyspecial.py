#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def get_special_paths(dir):
    filenames = os.listdir(dir)
    filelist = []
    for file in filenames:
        match = re.search(r'__\w+__', file)
        if match:
            filelist.append(os.path.abspath(os.path.join(dir, file)))
    return filelist


def copy_to(paths, todir):
    if not os.path.exists(todir):
        os.makedirs(todir)
    for file in paths:
        fname = os.path.basename(file)
        shutil.copy(file, os.path.join(todir, fname))


def zip_to(paths, zippath):
    allfile = ' '.join(paths)
    thiscmd = 'zip -j '+ zippath + ' ' + allfile
    print 'Command I\'m going to do:', thiscmd
    (status, output) = commands.getstatusoutput(thiscmd)
    if status:  
       sys.stderr.write(output)
       sys.exit(1)
    

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  filelist = []
  for arg in args:
      filelist.extend(get_special_paths(arg))
      
  if (todir == '') and (tozip == ''):
      print "\n".join(filelist) + '\n'
      
  if todir:
     copy_to(filelist, todir)

  if tozip:
     zip_to(filelist, tozip) 
  
if __name__ == "__main__":
  main()
