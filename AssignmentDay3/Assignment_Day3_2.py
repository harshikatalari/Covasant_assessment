#question:
# Flattens the list 
    # input = [1,2,3, [1,2,3,[3,4],2]]
    # output = [1,2,3,1,2,3,3,4,2]


input = [1,2,3, [1,2,3,[3,4],2]]
output=[]

def f_ip(input): 
    for f in input:               #iteration of given list
        if isinstance(f,list):      #if the element f is list recursive call
            f_ip(f)
        else:
            output.append(f)       #if the element is not a list then appending it to list named 'output'
f_ip(input)
print(output)
