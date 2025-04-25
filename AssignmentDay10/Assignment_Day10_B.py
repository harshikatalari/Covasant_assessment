# Can you infer who has survived ?

# 1. Load the data

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

url=r"C:\Users\Harshika\handson\code\data\titanic_train.csv"
data=pd.read_csv(url)
data

# 2. Which gender survived more 

max_survived_gender=data.groupby('sex')['survived'].agg('sum').reset_index()
max_survived_gender.sort_values('survived',ascending=False)
max_survived_gender.head(1)

# 3. Does it depend on pclass?

depend=data.groupby('pclass').agg({'survived':'sum'})
depend

# 4. can we see % of survival of each gender and pclass 

#based on GENDER:-
d_s=data.groupby('sex').agg({'sex':'count','survived':'sum'})
d_s['percentage']=d_s['survived']/d_s['sex']
d_s

#based on PCLASS:-
d_p=data.groupby('pclass').agg({'pclass':'sum','survived':'sum'})
d_p['percentage']=d_p['survived']/d_p['pclass']
d_p



