#Question:
# Recursively go below a dir and based on filter, dump those files in to  single file 
# (work with only text file)


import glob
import os.path

path=r""
folder=glob.glob(os.path.join(path,"*"))
data=r""

def recursive(folder,data):
    for file in folder:
        if os.path.isfile(file):
            if file.endswith(".txt"):
                with open(file,"rt") as f:
                    lines=f.readlines()
                with open(data,"at") as ft:
                    ft.write("\n******************************\n")
                    ft.write("Data from file"+file+"\n")
                    ft.writelines(lines)
                    ft.write("\n******************************\n")
        else:
            sub=glob.glob(os.path.join(file,"*"))
            recursive(sub,data)
recursive(folder,data)