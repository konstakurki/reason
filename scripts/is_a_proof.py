import sys

alphabet = ("abcdefghijklmnopqrstuvwxyz"
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            "0123456789_")

def is_in_alphabet(x):
    in_abc = 0
    for i in alphabet:
        if x == i:
            in_abc = 1
    return in_abc

def is_a_word(x):
    is_wd = 1
    if x == "" or x == "I" or x == "N":
        is_wd = 0
    else: 
        for i in x:
            if is_in_alphabet(i) != 1:
                is_wd = 0
    return is_wd

def is_st_space_st(x):
    is_stspst = 0
    n = 0
    while n < len(x) and is_stspst == 0:
        if x[n] == " " and is_a_statement(x[:n]) and is_a_statement(x[n+1:]):
            is_stspst = 1
        n = n + 1
    return is_stspst

def is_a_statement(x):
    is_st = 0
    if is_a_word(x) or ( x[0:2] == "N "
        and is_a_statement(x[2:]) ):
        is_st = 1
    elif x[0:2] == "I " and is_st_space_st(x[2:]):
        is_st = 1
    return is_st

#def main():
    #if len(sys.argv) == 2:
        #string = sys.argv[1]
        #if is_a_statement(string):
            #message = "I get it."
        #else: 
            #message = "Nonsense."
    #else:
        #message = "I need exactly on argument."
    #print(message)
#
#if __name__ == "__main__":
    #main()


def is_ax_1(x):
    return x[0:3] == "I N N " and is_st_space_st(x[6:])












