# flask
# Question-16:
# Sharing of content 
# @app.route("/updatefortoday", methods=['GET','POST'])#http://localhost:5000/updatefortoday
# @app.route("/share", methods=['GET'])#http://localhost:5000/share
# @app.route("/clearnotepadtxt", methods=['GET'])#http://localhost:5000/clearnotepadtxt


from flask import Flask
from flask import render_template,request
import os 

app=Flask(__name__)

Notepad_path="data/Data.txt"

@app.route("/updatefortoday", methods=['GET','POST'])   #http://localhost:5000/updatefortoday
def update_for_today():              
    if request.method == 'POST':
        content=request.form.get('updatearea')       #getting the content from index.html textarea
        if content :
            with open(Notepad_path,'at') as f:        
                f.writelines(content +'\n')           #reading the data from textarea and appending data inside textfile
            return "content updated succesfully"
        return "no content here"
    return render_template("index.html")  
    
@app.route("/share", methods=['GET'])    #http://localhost:5000/share
def share_content():
    if request.method == 'GET':
        if os.path.exists(Notepad_path):         #if path and content exists then reads the lines
            with open(Notepad_path,'rt') as f:
                lines=f.read()
    else:
        return ("nothing to share")
    return render_template("share.html", text=lines)     #adding the read lines inside share.html file
    
@app.route("/clearnotepadtxt", methods=['GET'])    #http://localhost:5000/clearnotepadtxt
def clear_notepad():
    if request.method == 'GET':
        with open(Notepad_path, 'w') as f:             #clearing the data 
            f.write('')
        return ("notepad cleared sucesfully")
        

if __name__=='__main__':
    #http://localhost:5000
    os.makedirs('data',exist_ok=True)      
    app.run()
    
