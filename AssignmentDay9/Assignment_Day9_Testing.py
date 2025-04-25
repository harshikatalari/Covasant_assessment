# fastapi
# Question-18:
# convert helloj of flask to fastapi


import requests

def sync_post1(url):
    return requests.get(url)
    
def sync_post2(url,obj):
    return requests.get(url,json=obj)
    
if __name__=='__main__':
    url1="http://localhost:8000/helloj/harshika/json"
    resp1=sync_post1(url1)
    print(resp1.json())
    url2="http://localhost:8000/helloj"
    obj=dict(name='shreya', formatt='json')
    resp=sync_post2(url2,obj)
    print(resp.json())