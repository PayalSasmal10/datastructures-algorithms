import threading

def print_cube(num):
    print("cube:", num*num*num)

def print_square(num):
    print("square:", num*num)


t1 = threading.Thread(target=print_cube, args=(10,))
t2 = threading.Thread(target=print_square, args=(10,))
t1.start()
t2.start()
