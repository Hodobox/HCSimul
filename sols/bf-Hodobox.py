file = input()

datastr = file + ".in"
outputstr = file + ".out"

def isvalid(row,col,rec,pizza,taken,r,c,l):

    #print(row,col,rec,"?")

    if row+rec[0] >= r or col+rec[1]>=c:
        return False

    #print("ok size")

    toppings = {'T':0,'M':0}

    for R in range(row,row+rec[0]):
        for C in range(col,col+rec[1]):
            toppings[ pizza[R][C] ] += 1
            if taken[R][C]:
                return False

    #print(toppings)

    return toppings['T'] >= l and toppings['M'] >= l

with open(datastr,'r') as data:
    with open(outputstr,'w+') as output:
        pizza = [line.strip() for line in data.readlines()]
        r,c,l,h = [int(x) for x in pizza[0].split()]
        pizza = pizza[1:]

        slices = []

        taken = [ [False for _ in range(c)] for _ in range(c)]

        rectangles = {x:[] for x in range(2*l,r*c+1)}
        for row in range(1,r+1):
            for col in range(1,c+1):
                area = row*col
                if area < 2*l or area > h:
                    continue

                rectangles[area].append((row,col))

        for row in range(r):
            for col in range(c):
                for size in range(2*l,h+1):
                    for rec in rectangles[size]:
                        canbe = isvalid(row,col,rec,pizza,taken,r,c,l)
                        #print(canbe)
                        if canbe:
                            slices.append((row,col,row+rec[0]-1,col+rec[1]-1))
                            for R in range(row,row+rec[0]):
                                for Y in range(col,col+rec[1]):
                                    taken[R][Y] = True

        print(len(slices),file=output)
        for piece in slices:
            print(*piece,file=output)