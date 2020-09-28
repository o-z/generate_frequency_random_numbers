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

    print("0="+str(score0))
    print("1="+str(score1))
    print("fitness"+str(abs(score0-score1)))

    """score * 100 / len(password)"""
def generateABinary():
    i = 0
    result = ""
    x=0
    xn=0.9999999999799954

    r=0.5
    a=3.99999999999992



    while i < 1000000:
        xn=a*xn*(1-xn)

        if xn<r :
            x=0
        elif xn>r or xn==r:
            x=1

        letter = str(x)

        result += letter
        i +=1
    text_file = open("Outputbits.txt", "w")
    text_file.write("Purchase Amount: %s" % (result))
    text_file.close()
    return result
    pass
binary=generateABinary()
fitness(binary)
