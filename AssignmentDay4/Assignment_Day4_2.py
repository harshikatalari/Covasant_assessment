# Question-6:
# #MaxFile class 
# from pkg.file import File 
# fs = File(".")
# fs.getMaxSizeFile(2) # gives two max file names 
# fs.getLatestFiles(datetime.date(2018,2,1))
# #Returns list of files after 1st Feb 2018 





import glob
import os.path
import datetime


allfiles={}
time=[]
total_time={}
t=[]

date=datetime.date(2025,4,10)  #enter date in format yyyy,m,dd
path=r""



#finding max two files names

def getMaxSizeFile(path):
    files=glob.glob(os.path.join(path,"*"))   #returns all files/folders in a given directory in the form of list
    for f in files:
        if os.path.isfile(f):   
            allfiles[os.path.basename(f)]=os.path.getsize(f) #adding to dictionary
        elif os.path.isdir(f):
            getMaxSizeFile(f)   #if path is a directory then recursive call
getMaxSizeFile(path)

max_file=sorted(allfiles)   #sorting all files ascending by default where key is its size
Two_max_files=max_file[-2:]  #ascessing last two files as they have max size
print(Two_max_files)


#finding all files created after the date given by user
def getLatestFiles(path,date):
    files=glob.glob(os.path.join(path,"*"))   #returns all files/folders in a given directory in the form of list
    for f in files:
        if os.path.isfile(f):
            s=os.path.getmtime(f)       #The method returns a floating-point number of time, when most recent modification is made, measured in seconds 
            d=datetime.date.fromtimestamp(s)  #The fromtimestamp() method is used to create a datetime object from a timestamp measured in seconds
            if date<d:      #date is date specified by user, and d is the date of list of all the files the path specified
                t.append(f)      
        elif os.path.isdir(f):     #if path is a directory then recursive call
            getLatestFiles(f,date)
getLatestFiles(path,date)

print(t)
