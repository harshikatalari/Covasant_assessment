# fastapi
# Question-18:
# convert helloj of flask to fastapi


from fastapi import FastAPI,Request
from pydantic import BaseModel

app=FastAPI()

    
class details(BaseModel):
    name:str
    formatt:str
    
@app.get("/helloj")
def helloj_details(d:details):
    obj = dict(name=  d.name, formatt=d.formatt)
    return obj



@app.get("/helloj/{name}/{formatt}")
def helloj(name:str, formatt:str):
    obj = dict(name=name, formatt=formatt, details="details were added")
    return obj    