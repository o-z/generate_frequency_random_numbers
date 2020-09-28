def fitness (test_word):
    score0 = 0
    score1 = 0
    score2 = 0
    score3 = 0
    score4 = 0
    score5 = 0
    score6 = 0
    score7 = 0
    score8 = 0
    score9 = 0
    score10 = 0
    score11 = 0
    score12 = 0
    score13 = 0
    score14 = 0
    score15 = 0
    i = 0
    test_word=list(test_word)
    while (i < (len(test_word)/4)):
        if test_word[i*4] == "0" and test_word[i*4+1]=="0" and test_word[i*4+2]=="0" and test_word[i*4+3]=="0" :

            score0+=1
        elif test_word[i*4] == "0" and test_word[i*4+1]=="0" and test_word[i*4+2]=="0" and test_word[i*4+3]=="1" :

            score1+=1
        elif test_word[i*4] == "0" and test_word[i*4+1]=="0" and test_word[i*4+2]=="1" and test_word[i*4+3]=="0" :
            score2+=1
        elif test_word[i*4] == "0" and test_word[i*4+1]=="0" and test_word[i*4+2]=="1" and test_word[i*4+3]=="1" :
            score3+=1
        elif test_word[i*4] == "0" and test_word[i*4+1]=="1" and test_word[i*4+2]=="0" and test_word[i*4+3]=="0" :
            score4+=1
        elif test_word[i*4] == "0" and test_word[i*4+1]=="1" and test_word[i*4+2]=="0" and test_word[i*4+3]=="1" :
            score5+=1
        elif test_word[i*4] == "0" and test_word[i*4+1]=="1" and test_word[i*4+2]=="1" and test_word[i*4+3]=="0" :
            score6+=1
        elif test_word[i*4] == "0" and test_word[i*4+1]=="1" and test_word[i*4+2]=="1" and test_word[i*4+3]=="1" :
            score7+=1
        elif test_word[i*4] == "1" and test_word[i*4+1]=="0" and test_word[i*4+2]=="0" and test_word[i*4+3]=="0" :
            score8+=1
        elif test_word[i*4] == "1" and test_word[i*4+1]=="0" and test_word[i*4+2]=="0" and test_word[i*4+3]=="1" :
            score9+=1
        elif test_word[i*4] == "1" and test_word[i*4+1]=="0" and test_word[i*4+2]=="1" and test_word[i*4+3]=="0" :
            score10+=1
        elif test_word[i*4] == "1" and test_word[i*4+1]=="0" and test_word[i*4+2]=="1" and test_word[i*4+3]=="1" :
            score11+=1
        elif test_word[i*4] == "1" and test_word[i*4+1]=="1" and test_word[i*4+2]=="0" and test_word[i*4+3]=="0" :
            score12+=1
        elif test_word[i*4] == "1" and test_word[i*4+1]=="1" and test_word[i*4+2]=="0" and test_word[i*4+3]=="1" :
            score13+=1
        elif test_word[i*4] == "1" and test_word[i*4+1]=="1" and test_word[i*4+2]=="1" and test_word[i*4+3]=="0" :
            score14+=1
        elif test_word[i*4] == "1" and test_word[i*4+1]=="1" and test_word[i*4+2]=="1" and test_word[i*4+3]=="1" :
            score15+=1


        i+=1

    print("0="+str(score0))
    print("1="+str(score1))
    print("2="+str(score2))
    print("3="+str(score3))
    print("4="+str(score4))
    print("5="+str(score5))
    print("6="+str(score6))
    print("7="+str(score7))
    print("8="+str(score8))
    print("10="+str(score9))
    print("11="+str(score10))
    print("12="+str(score11))
    print("13="+str(score12))
    print("14="+str(score13))
    print("15="+str(score14))
    print("16="+str(score15))

    """score * 100 / len(password)"""
def generateABinary():
    i = 0
    result = ""
    x=0
    xn= 0.8404129869541441

    r=0.5
    a= 3.87010643043095



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
