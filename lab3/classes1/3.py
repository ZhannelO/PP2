def solve(numheads, numlegs):
    for i in range(1,numheads):
        for k in range(1,numheads):
            legs=i*4+k*2
            if legs==numlegs:
                print(str(i)+" " +"rabbits"+" "+str(k)+" "+"chicken")
solve(35,94)


