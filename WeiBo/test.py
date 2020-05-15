import random

def createId(num):
    chars = 'a0v1c2d3e4f5g6h7i8j9k0l1m2n3o4p5q6r7s8t9u0v1w2x4y5z6'
    salt = ''
    for i in range(num):
        salt += random.choice(chars)
    return salt
if __name__ == '__main__':
    id1 = "topic" + createId(10)
    id2 = "dicu" + createId(10)
    print(id1)
    print(id2)
