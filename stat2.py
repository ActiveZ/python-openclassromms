import os
from random import choices, randint, shuffle


os.system('cls') # windows
os.system('clear') # linux


######################## exercice 1 ####################################

def exo1():
    c = choices(["un","deux","trois","quatre","cinq","six"], k=10000)
    # shuffle (c)
    print("len c:", len(c))
    six = c.count("six")/10000
    print (six)

    c = c[:1000]
    print("len:", len(c))   
    quatre = c.count("quatre")/1000
    print (quatre)
    return (six,quatre)
# print ("un:", c.count("six")/10000)
# print ("deux:", c.count("deux")/1000)
# print ("trois:", c.count("trois")/1000)
# print ("cinq:", c.count("cinq")/1000)
# print("six:",choices(["un","deux","trois","quatre","cinq","six"], weights=[1,1,1,1,1,1], k=10000).count('six')/10000)

six = 0
quatre = 0
for i in range(5):
    a = exo1()
    six += a[0]
    quatre += a[1]

print("six:", six/5)
print("quatre:",quatre/5)
exit()


######################## exercice 2 #######################################
def tirage_A():
    return choices('PF', cum_weights=(0.49,1), k=1000000).count('P')/1000000

# x = sum(tirage_A() for i in range(10_000)) / 10_000
# print(x)
print(tirage_A())


def tirage_B():
    p1 = choices('PF', cum_weights=(0.09,1), k=1000000).count('P')/1000000
    p2 = choices('PF', cum_weights=(0.74,1), k=1000000).count('P')/1000000
print(tirage_B())

k = 0
if randint(0,1) == 0: pass
print(choices('PF', cum_weights=(0.5,1), k = 1000000).count('P'))
# operator.add(n,1)
print(k)