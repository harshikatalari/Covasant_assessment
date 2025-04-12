#question:
# Converts like below 
    # input = [[[ '(0,1,2)' , '(3,4,5)'], ['(5,6,7)' , '(9,4,2)']]]
    # output = [[[[0,1,2],[3,4,5]],[[5,6,7],[9,4,2]]]]



input = [[[ '(0,1,2)' , '(3,4,5)'], ['(5,6,7)' , '(9,4,2)']]]
output=[]

def flatten(input):
    first=[]             #outer first list
    for x in input:
        sec=[]                #inner second list
        for y in x:
            for z in y:
                s=(z.strip("()").split(","))      #strips the tuple and splits each element and returns in the form of list
                num=[int(t) for t in s]      #as the elements in the returned list are 'str' converting them into 'int'
                sec.append(num)         
        first.append(sec)         #adding elements to second list
    output.append(first)             #adding second list to first list
flatten(input)
print(output)





















  
