import sys

file = input()

datastr = file + ".in"
outputstr = file + ".out"

with open(datastr,'r') as data:
    with open(outputstr,'r') as output:
        pizza = [line.strip() for line in data.readlines()]
        r,c,l,h = [int(x) for x in pizza[0].split()]
        pizza = pizza[1:]
        
        result = [line.strip() for line in output.readlines()]

        num_slices = int(result[0])
        slices = []

        for piece in result[1:]:
            piece = piece.split()
            slices.append([int(x) for x in piece])
        
        answer = 0
        for piece in slices:
            answer += (abs(piece[0]-piece[2])+1) * (abs(piece[1]-piece[3])+1)

        print(str(num_slices) + " slices with " + str(answer) + " cells")

        for piece in slices:
            area = abs(piece[0]-piece[2]+1) * abs(piece[1]-piece[3]+1)
            if area > h:
                print("ERR: Slice with area " + str(area), file = sys.stderr)

            toppings = {'T':0, 'M':0}

            rows = list(sorted([piece[0],piece[2]]))
            cols = list(sorted([piece[1],piece[3]]))

            for row in range(rows[0],rows[1]+1):
                for col in range(cols[0],cols[1]+1):
                    toppings[ pizza[row][col] ] += 1

            if toppings['T'] < l:
                print('Only ' + str(toppings['T']) + ' tomatoes',file = sys.stderr)

            if toppings['M'] < l:
                print('Only ' + str(toppings['M']) + ' mushrooms',file = sys.stderr)

        taken = [ [0 for _ in range(c)] for _ in range(r)]
        for piece in slices:
            rows = list(sorted([piece[0],piece[2]]))
            cols = list(sorted([piece[1],piece[3]]))

            for row in range(rows[0],rows[1]+1):
                for col in range(cols[0],cols[1]+1):
                    taken[row][col] += 1

        for row in range(r):
            for col in range(c):
                if taken[row][col] > 1:
                    print(str(row)+','+str(col)+' in ' + str(taken[row][col]) + ' slices',file = sys.stderr)