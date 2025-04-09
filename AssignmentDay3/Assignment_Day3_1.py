#question:
# Converts like below 
    # input = [[[ '(0,1,2)' , '(3,4,5)'], ['(5,6,7)' , '(9,4,2)']]]
    # output = [[[[0,1,2],[3,4,5]],[[5,6,7],[9,4,2]]]]



input = [[[ '(0,1,2)' , '(3,4,5)'], ['(5,6,7)' , '(9,4,2)']]]
output=[]

def flatten(input):
    first=[]
    for x in input:
        sec=[]
        for y in x:
            for z in y:
                s=(z.strip("()").split(","))
                num=[int(t) for t in s]
                sec.append(num)
        first.append(sec)
    output.append(first)
flatten(input)
print(output)





















  
