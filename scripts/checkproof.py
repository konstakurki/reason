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

# I N N <A>
def ax_1(x):
    return split(x)[0][:4] == "N N "

# I <A> I <B> <A>
def ax_2(x):
    B = 0
    pair = split(x)
    if pair != ["",""]:
        B = pair[0] == split(pair[1])[1]
    return B

# I I <A> I <B> <C> I I <A> <B> I <A> <C>
def ax_3(x):
    B = 0
    pair    = split(x)
    pair_0  = split(pair[0])
    pair_01 = split(pair_0[1])
    pair_1  = split(pair[1])
    pair_10 = split(pair_1[0])
    pair_11 = split(pair_1[1])
    if pair_01[0] != "" and pair_10[0] != ""  and pair_11 != "":
        if pair_0[0] == pair_10[0] and pair_0[0] == pair_11[0]:
            if pair_01[0] == pair_10[1]:
                if pair_01[1] == pair_11[1]:
                    B = 1
    return B
    
def axiom(x):
    return ax_1(x) or ax_2(x) or ax_3(x)

def steps(x):
    x = "\n" + x
    stp = []
    n = 0
    for i in range(len(x)):
        if x[i] == "\n":
            stp.append(x[n+1:i])
            n = i
    stp = stp[1:]
    return stp

def proof(x):
    B = 1
    if x != []:
    for i in x:
        if 



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
