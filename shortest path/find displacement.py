# Find displacement: Given a long route containing N,S,W,E directions,find the shortest path to
# reach the location .Sample i/p: SNNNEWE. O/P: NNE

input = input()
def displacementshotestpath(input):
    x=y=0
    for i in input:
        if i == 'N':
            y += 1
        elif i == 'E':
            x += 1
        elif i == 'S':
            y -= 1
        elif i == 'W':
            x -= 1

    print("x and y values are :", x, y)

    while(y>0):
        print("N")
        y = y-1
    while (x>0):
        print("E")
        x -= 1



displacementshotestpath(input)

