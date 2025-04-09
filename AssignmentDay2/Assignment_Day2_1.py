#Question:
# Given a directory, find out the file Name having max size recursively 

import glob
import os.path

path=r""
maxfiles={}

def recursive(path):
    files=glob.glob(os.path.join(path,"*"))
    for f in files:
        if os.path.isdir(f):
            recursive(f)
        elif os.path.isfile(f):
            maxfiles[os.path.basename(f)]=os.path.getsize(f)
recursive(path)
maxsize=sorted(maxfiles.values())[-1]
for f in maxfiles:
    size=maxfiles[f]
    if size==maxsize:
        print(f"{f}"+ "and size is : "+f"{maxsize}")
