#Question:
# Recursively go below a dir and based on filter, dump those files in to  single file 
# (work with only text file)


import glob
import os.path

path=r""
folder=glob.glob(os.path.join(path,"*"))
data=r""

def recursive(folder,data):
    for file in folder:          #folder is list of all the paths in a given directory obtained by glob.glob method
        if os.path.isfile(file):     #if file is a file 
            if file.endswith(".txt"):     #and ends with .txt extension
                with open(file,"rt") as f:      #then reading the file
                    lines=f.readlines()
                with open(data,"at") as ft:        #data is the path of a file given by user where we want to append the textlines 
                    ft.write("\n******************************\n")     #writing the data
                    ft.write("Data from file"+file+"\n")          #writing the data read from the .txt extension file which is 'lines'
                    ft.writelines(lines)       
                    ft.write("\n******************************\n")
        else:
            sub=glob.glob(os.path.join(file,"*"))        #if the file is not a file but a directory recursive call
            recursive(sub,data)
recursive(folder,data)
