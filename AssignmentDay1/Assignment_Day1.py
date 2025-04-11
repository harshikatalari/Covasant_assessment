# Question-2: 
# Given:D1 = {'ok': 1, 'nok': 2}
# D2 = {'ok': 2, 'new':3 }
# Create below:
# # union of keys, #value does not matter
# D_UNION = { 'ok': 1, 'nok': 2 , 'new':3  } 
# # intersection of keys, #value does not matter
# D_INTERSECTION = {'ok': 1}
# D1- D2 = {'nok': 2 }
# #values are added for same keys
# D_MERGE = { 'ok': 3, 'nok': 2 , 'new':3  }


D1={'ok':1,'nok':2}
D2={'ok':2,'new':3}

D_UNION={**D1,**D2}      
print(D_UNION)

D_INTERSECTION={}
for k in D1.keys()&D2.keys():
    D_INTERSECTION[k]=D1[k]
print(D_INTERSECTION)

D_DIFFERENCE={}
for k in D1.keys()-D2.keys():
    D_DIFFERENCE[k]=D1[k]
print(D_DIFFERENCE)

D_MERGE={}
for k in D1.keys()|D2.keys():
    D_MERGE[k]=D1.get(k,0)+D2.get(k,0)
print(D_MERGE)
