import string
import random

if __name__ == "__main__":


    s1 = string.ascii_lowercase
    #S1 takes all Small Letters

    # print(s1)
    s2 = string.ascii_uppercase
    #s2 takes All Capital Letters

    # print(s2)
    s3 = string.digits
    #S3 Takes All Digits In String

    # print(s3)
    s4 = string.punctuation
    #s4 it takes all punctuations

    # print(s4)

    #Plen Interact With User For Password Length
    plen = int(input("Enter The Password Length : "))


    s=[]

    #We Take all The Letters ,digits,Punctuation In One List
    s.extend(s1)
    s.extend(s2)
    s.extend(s3)
    s.extend(s4)

    #Finally We Shuffel It For a Strong Password
    random.shuffle(s)


    print("Your Password is : ")

    #Finally We Create A Strong Password
    print("".join(s[0:plen]))