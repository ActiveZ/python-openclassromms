import os
from random import choices, randint, shuffle


os.system('cls') # windows
os.system('clear') # linux


######################## exercice 1 ####################################

def exo1():
    # c = choices(["un","deux","trois","quatre","cinq","six"], k=10000)
    c = choices(["un","deux","trois","quatre","cinq","six"], k=10000)
    # shuffle (c)
    # print("len c:", len(c))
    # six = c.count("six")/10000
    # print (six)

    # # c = c[:1000]
    # # print("len:", len(c))   
    # # quatre = c[:1000].count("quatre")/1000
    # # print (quatre)
    # # return (six,quatre)
    return (c.count("six")/10000, c[:1000].count("quatre")/1000)
# print ("un:", c.count("six")/10000)
# print ("deux:", c.count("deux")/1000)
# print ("trois:", c.count("trois")/1000)
# print ("cinq:", c.count("cinq")/1000)
# print("six:",choices(["un","deux","trois","quatre","cinq","six"], weights=[1,1,1,1,1,1], k=10000).count('six')/10000)

six = 0
quatre = 0
# res = (x,y) = (0,0)
for i in range(5):
    a = exo1()
    six += a[0]
    quatre += a[1]
    # res = tuple(map(sum,zip(res, (a[0],a[1]))))
    # print(res[0]/(i+1),res[1]/(i+1))


# x = sum(exo1()[0] for i in range (5))/5


print("six:", six/5)
print("quatre:",quatre/5)
# exit()


######################## exercice 2 #######################################

os.system('cls') # windows
os.system('clear') # linux

def tirage_A():
    return choices([1,-1], cum_weights=(0.49,1))[0]

# x = sum(tirage_A() for i in range(10_000)) / 10_000
# print('A:',x)
# print(tirage_A())


def tirage_B(k):
    if k%3:
        return choices([1,-1], cum_weights=(0.74,1))[0] # pas multiple de 3
    else:
        return choices([1,-1], cum_weights=(0.09,1))[0] # multiple de 3
# k = 0        
# for i in range(10_000): k += tirage_B(k)
# print('B:',k)
# print(tirage_B(1))


k = 0
# méthode naive
# for i in range(1000000):
#     if randint(0,1) == 0: 
#         k += tirage_A()
#     else:
#         k += tirage_B(k)

# méthode ternaire
for i in range(1000000):
    k += tirage_A() if randint(0,1) == 0 else tirage_B(k)
print(k)

print("le ciel est", "bleu" if randint(0,1) == 0 else "gris")

