# -----
# -- Author:       Ronnie Rahman
# -- Date:         15 July 2014
# -- Description:  Random number generator, Lottery number generator
# --
import random
              
#generate random number

#added 1 at the end of the random range
#as range starts from 0

#Random number 1
n1 = random.randrange(1,9) +1

#Random number 2
n2 = random.randrange(10,19) +1

#Random number 3
n3 = random.randrange(20,29) +1

#Random number 4      
n4 = random.randrange(30,39) +1

#Random number 5
n5 = random.randrange(40,48) +1

#Random star number
s1=random.randrange(1,5)+1
s2=random.randrange(6,9)+1

print ("Your lottery numbers are: ", n1, n2, n3, n4, n5, " Star: ", s1, "-", s2)

