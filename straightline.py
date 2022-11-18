"""
The first three functions are just used for testing purposes for this assignment. list_strings gives a list of all
strings of length n, string_to_nat and nat_to_string convert back and forth between binary strings and natural numbers.

IMPORTANT: Note that the order of significance for the bits in our strings matches how we naturally read numbers, so in
the binary string 10 the 1 is the most significant bit and 0 is the least significant. Be aware that this is opposite
from the order of the string indices.
"""
score = 0

def list_strings(n):
    """lists all binary strings of length n, do not modify this function"""
    if n == 0:
        return [""]
    else:
        strings = []
        for b in list_strings(n-1):
            strings.append(b+"0")
            strings.append(b+"1")
        return strings
        
def string_to_nat(b):
    """Given a binary string, converts it into a natural number.  Do not modify this function."""
    if b == "":
        return 0
    else:
        return 2 * string_to_nat(b[:-1]) + int(b[-1])
        

def nat_to_string(x):
    """Given a natural number, converts it into a binary string  Do not modify this function."""
    assert(x >= 0)
    if x == 0:
        return ""
    else:
        return nat_to_string(x//2) + str(x % 2)
        
"""This next block of functions is setting us up to program in AON-Straightline. The is_binary function checks that 
we are only computing on binary inputs/outputs (the only data type that AON-Straightlin can handle). 
The AND, OR, and NOT functions implement the corresponding boolean operators in python. """

def is_binary(b):
    return b == '1' or b == '0'

def AND(a,b):
    assert(is_binary(a) and is_binary(b))
    return str(int(a)*int(b))

def OR(a,b):
    assert(is_binary(a) and is_binary(b))
    return str(int(a)+int(b) - int(a)*int(b))

def NOT(a):
    assert(is_binary(a))
    return str(1-int(a))
    
"""Finally, from here we're programming in AON-Straightline. We start out by implementing some of the functions 
in class in AON-Straightline: XOR, NAND, and MAJ. These give you an idea for how AON-Straightline should be written 
(in general and by you in this assignment). Each line in the program should consist of a new variable declaration on 
the left-hand side and an AND/OR/NOT operation on the right-hand side, or else a return statement. Please note that you 
cannot use any operations besides AND/OR/NOT on the right-hand side (except for one case where you'll be 
directed otherwise), you cannot have multiple operations nested (e.g. NOT(AND(a,b)) is not permitted), and you cannot 
re-assign and already assigned variable (e.g. a = NOT(a) is not permitted)."""
    
def XOR(a,b):
    not_a = NOT(a)
    not_b = NOT(b)
    a_not_b = AND(a, not_b)
    b_not_a = AND(b, not_a)
    return OR(a_not_b, b_not_a)

def NAND(a,b):
    a_and_b = AND(a,b)
    return NOT(a_and_b)
    
def MAJ(a,b,c):
    assert(is_binary(a) and is_binary(b) and is_binary(c))
    first_two = AND(a,b)
    last_two = AND(b,c)
    first_last = AND(a,c)
    temp = OR(first_two, last_two)
    return OR(temp, first_last)

"""Uncomment the code block below to see XOR, NAND, and MAJ in action. Here we're enumerating all possible inputs and 
printing out each function's output for those inputs. This is also how the following asserts will test the code you 
write (except instead of printing it compares the output to the correct answers). Please re-comment all lines before 
submitting."""
    
for i in list_strings(2):
    print('AND', i, AND(i[0], i[1]))
for i in list_strings(2):
    print('OR', i, OR(i[0], i[1]))
for i in list_strings(2):
    print('XOR', i, XOR(i[0], i[1]))
for i in list_strings(2):
    print('NAND', i, NAND(i[0], i[1]))
for i in list_strings(3):
    print('MAJ', i, MAJ(i[0], i[1], i[2]))



"""Now you're ready to start implementing programs in AON straightline for yourself. Implement the function (IMPL) 
described below."""

def IMPL(a,b):
    """TODO: Implement the boolean operator Implies which is true whenever "a implies b" is true."""
    return "0"

"""Checks that your implementation of IMPL is correct. It enumerates all inputs(note there are only finitely many, 
so we can be exhaustive), and checks the answer"""
IMPL_correct = True
for i in list_strings(2):
    IMPL_correct = IMPL_correct and (IMPL(i[0], i[1]) == ['1','1','0','1'][string_to_nat(i)])
    if not IMPL_correct:
        print("IMPL gave incorrect result for IMPL("+i[1]+","+i[0]+")")
        break
if IMPL_correct:
    print("IMPL works! Nicely, done!")
    score += 1


"""Now re-implement XOR in the NAND-Straightline language (follow the same rules as AON-Straightline, but only use 
the NAND operation on the right-hand side)."""
def XOR_nand(a, b):
    """TODO: Implement XOR using only NAND"""
    return '0'

XOR_nand_correct = True
for i in list_strings(2):
    XOR_nand_correct = XOR_nand_correct and (XOR(i[0], i[1]) == XOR_nand(i[0], i[1]))
    if not XOR_nand_correct:
        print("XOR_nand gave incorrect result for XOR_nand("+i[0]+","+i[1]+")")
        break
if XOR_nand_correct:
    print("Hooray!!! XOR_nand is working. You rock!")
    score += 1


def COMP_2(a1, a0, b1, b0):
    """TODO: Implement COMP_2 using AON where COMP_2(a1, a0, b1, b0) is true whenever the natural number represented
    by a1a0 is larger than the natural number represented by b1b0. I.e. COMP_2(1,1,1,0)=1 because 11 represents
    3 and 10 represents 2 and 3>2."""
    return "0"

COMP2_correct = True
for a in list_strings(2):
    a_val = string_to_nat(a)
    for b in list_strings(2):
        b_val = string_to_nat(b)
        COMP2_correct = COMP2_correct and ((COMP_2(a[0], a[1], b[0], b[1]) == "1") == (a_val > b_val))
        if not COMP2_correct:
            print("COMP_2 gave incorrect result for comparison " + str(a_val) + ">" + str(b_val))
            break
    if not COMP2_correct:
        break

if COMP2_correct:
    print("You did it! COMP_2 is correct! Post it to your insta.")
    score += 1

grade = score/3
print("Problem Grade:", grade)

