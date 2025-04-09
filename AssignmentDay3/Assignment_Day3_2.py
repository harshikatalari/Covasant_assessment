#question:
# Flattens the list 
    # input = [1,2,3, [1,2,3,[3,4],2]]
    # output = [1,2,3,1,2,3,3,4,2]


input = [1,2,3, [1,2,3,[3,4],2]]
output=[]

def f_ip(input):
    for f in input:
        if isinstance(f,list):
            f_ip(f)
        else:
            output.append(f)
f_ip(input)
print(output)