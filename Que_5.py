def solve(numheads,numlegs):

    for i in range(numheads+1):
        j=numheads-i
        if (2*i)+(4*j)==numlegs:
            return i,j
    return 'no result'

numheads = int(input('Enter total number of heads:'))
numlegs = int(input('Enter total number of legs:'))
number=solve(numheads,numlegs)
print ("Number of rabbits and chickens: ",number)

