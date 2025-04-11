#Question:
# Given a directory, find out the file Name having max size recursively 

import glob
import os.path

path=r""                  #specify the directory
maxfiles={}

def recursive(path):                      
    files=glob.glob(os.path.join(path,"*"))            #to find all the individual files in a directory
    for f in files:
        if os.path.isdir(f):                #if directory then recursive call
            recursive(f)
        elif os.path.isfile(f):
            maxfiles[os.path.basename(f)]=os.path.getsize(f)              #adding filename as key and path of file a directory {}
recursive(path)
maxsize=sorted(maxfiles.values())[-1]     #sorting file size default ascending and gives file which has max size
for f in maxfiles:
    size=maxfiles[f]
    if size==maxsize:
        print(f"{f}"+ "and size is : "+f"{maxsize}")
