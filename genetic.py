import random
import operator
import time
import matplotlib.pyplot as plt
from numpy import zeros
import numpy as np

def generateABinary (length):
    i = 0
    result = ""
    x=0
    a=random.uniform(3.5, 4.0)
    xn=random.uniform(0.0,1.0)
    r=0.5




    while i < length:
        xn=a*xn*(1-xn)

        if xn<r :
            x=0
        elif xn>r or xn==r:
            x=1

        letter = str(x)

        result += letter
        i +=1
    return result,a,xn,r
def generateAChildBinary (a,xnn,length):
    i = 0
    result = ""
    x=0
    xn=xnn
    r=0.5

    while i < length:
        xn=a*xn*(1-xn)

        if xn<r :
            x=0
        elif xn>r or xn==r:
            x=1

        letter = str(x)

        result += letter
        i +=1
    return result,a,xnn,r

def fitness (test_word):
    score0 = 0
    score1 = 0
    i = 0
    test_word=list(test_word)
    while (i < len(test_word)):
        if test_word[i] == "0" :

            score0+=1
        elif test_word[i] == "1" :

            score1+=1


        i+=1
    return abs(score0-score1)
    """score * 100 / len(password)"""

def generateFirstPopulation(sizeGen,sizePopulation):
    population = []
    number_of_a = []
    number_of_xn = []
    number_of_r = []
    i = 0
    while i < sizePopulation:
        result,a,xn,r=generateABinary(sizeGen)
        population.append(result)
        number_of_a.append(a)
        number_of_xn.append(xn)
        number_of_r.append(r)

        i+=1
    return population,number_of_a,number_of_xn,number_of_r



def sortingfitness(fitnessorted):
    n = len(fitnessorted)
    for i in range(n):
        for j in range(0, n-i-1):
            if int(fitnessorted[j][0]) > int(fitnessorted[j+1][0]) :
                fitnessorted[j][0], fitnessorted[j+1][0] = fitnessorted[j+1][0], fitnessorted[j][0]
                fitnessorted[j][1], fitnessorted[j+1][1] = fitnessorted[j+1][1], fitnessorted[j][1]
                fitnessorted[j][2], fitnessorted[j+1][2] = fitnessorted[j+1][2], fitnessorted[j][2]
                fitnessorted[j][3], fitnessorted[j+1][3] = fitnessorted[j+1][3], fitnessorted[j][3]
                fitnessorted[j][4], fitnessorted[j+1][4] = fitnessorted[j+1][4], fitnessorted[j][4]
    return fitnessorted
    pass


def Print_of_Data(size,fitnessorted):
    for i in range(size):
        print("------------------------")

        print("Fitness Degeri;",fitnessorted[i][0])
        print(i,". DNA--->")
        print("\n")
        print("a degeri:",fitnessorted[i][2],"-")
        print("xn degeri:",fitnessorted[i][3],"-")
        print("eşik degeri:",fitnessorted[i][4],"-")
        print("\n")
        pass
    pass



sizePopulation=50
sizeGen=100000
fitnessorted=np.zeros((sizePopulation,5,), dtype=object)

population,number_of_a,number_of_xn,number_of_r=generateFirstPopulation(sizeGen,sizePopulation)
for i in range(len(population)):

    fitnessorted[i][0]=str(fitness(population[i]))
    fitnessorted[i][1]=population[i]
    fitnessorted[i][2]=number_of_a[i]
    fitnessorted[i][3]=number_of_xn[i]
    fitnessorted[i][4]=number_of_r[i]

    pass
fitnessorted=sortingfitness(fitnessorted)

Print_of_Data(sizePopulation,fitnessorted)


def mutation(fitnessorted_mutation):
    for value in range(len(fitnessorted_mutation)):
        a=str(fitnessorted_mutation[value][2])
        xn=str(fitnessorted_mutation[value][3])
        a=list(a)
        xn=list(xn)
        i = 2
        rand_a1=int(random.uniform(i, (len(a)-1)))
        rand_xn1=int(random.uniform(i, (len(xn)-1)))
        while i < len(a):


            rand_a2=int(random.uniform(0, 9))
            rand_xn2=int(random.uniform(0, 9))
            temp=a[rand_a1]
            a[rand_a1]=a[rand_a2]
            a[rand_a2]=temp
            temp=xn[rand_xn1]
            xn[rand_xn1]=xn[rand_xn2]
            xn[rand_xn2]=temp
            i = i + 1
        a=''.join(a)
        a=float(a)
        xn=''.join(xn)
        xn=float(xn)

        fitnessorted_mutation[value][2]=a
        fitnessorted_mutation[value][3]=xn
        pass
    return fitnessorted_mutation
    pass

def generateChildrenPopulation(mutation_do,fitnessorted,sizePopulation,sizeGen):

    deger1=random.uniform(0.0, 1.0)
    deger2=random.uniform(0.0, 1.0)
    for value in range(sizePopulation):

        fitnessorted[value][1],fitnessorted[value][2],fitnessorted[value][3],fitnessorted[value][4]=generateAChildBinary(fitnessorted[int(deger1*4)][2],fitnessorted[int(int(deger2*4))][3],sizeGen)
        fitnessorted[value][0]=fitness(fitnessorted[value][1])



        pass

    if int(fitnessorted[0][0]<100):
        Print_of_Data(1,fitnessorted)
        return
        pass

    fitnessorted=sortingfitness(fitnessorted)
    if not fitnessorted[0][0]==mutation_do :
        Print_of_Data(1,fitnessorted)


        mutation_do=fitnessorted[0][0]

        generateChildrenPopulation(mutation_do,fitnessorted,sizePopulation,sizeGen)
        pass
    elif fitnessorted[0][0]==mutation_do :
        print("MUTATION STARTING")
        fitnessorted=mutation(fitnessorted)
        generateChildrenPopulation(mutation_do,fitnessorted,sizePopulation,sizeGen)
        pass

    pass
mutation_do=5
generateChildrenPopulation(mutation_do,fitnessorted,sizePopulation,sizeGen)
