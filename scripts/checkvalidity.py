import sys

alphabet = ("abcdefghijklmnopqrstuvwxyz"
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            "0123456789_")

def in_alphabet(x):
    B = 0
    for i in alphabet:
        if x == i:
            B = 1
            break
    return B

def word(x):
    wd = 1
    if x == "" or x == "I" or x == "N":
        wd = 0
    else: 
        for i in x:
            if in_alphabet(i) != 1:
                wd = 0
                break
    return wd

def split(x):
    spl = ["",""]
    B = 0
    n = 0
    if x[:2] == "I ":
        while n < len(x) and B == 0:
            if x[n] == " " and sentence(x[2:n]) and sentence(x[n+1:]):
                spl = [x[2:n],x[n+1:]]
                B = 1
                break
            n = n + 1
    return spl

def sentence(x):
    B = 0
    if word(x) or ( x[0:2] == "N "
        and sentence(x[2:]) ):
        B = 1
    elif split(x) != ["",""]:
        B = 1
    return B

def truth(x,ws):
    if x[:2] == "N ":
        B = not truth(x[2:])
    elif x[:2] == "I ":
        spl = split(x)
        B = not truth(spl[0]) or truth(spl[1])
    else: B = ws(x)
    return B












def main():
    if len(sys.argv) == 2:
        stuff = open(sys.argv[1],"r").read()
        print(steps(stuff))
        #if proof(stuff):
            #message = "Nice proof :)"
        #else:
            #message = "Crap."
    #else:
        #message = "lkhj"
#print(message)

if __name__ == "__main__":
    main()
