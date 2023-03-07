value = 56

if value > 75:
    print("wombat")
    print("wallaby")
elif 50 < value <= 75:
    print("mango")
elif value > 50:  # else if
    print("quokka")
    print("platypus")
elif value > 25:
    print("kangaroo")
    print("blue-ringed octopus")
else:
    print("koala")
    print("kookaburra")


print("ALL DONE")

"""
match number:
    case 0:
        print("Nothing")
    case 1:
        print("Just one")
    case 2:
        print("A couple")
    case -1:
        print("One less than nothing")
    case 1-1j:
    
import constants

match config:
    case {"route": route}:
        process_route(route)
    case {constants.DEFAULT_PORT: sub_config, **rest}:
        process_config(sub_config, rest)    
    
"""


# if X is a number
#   X == 0  -> False
#   X != 0  -> True

# if X is a container (i.e., has a length)
#  len(X) == 0  -> False
#  len(X) > 0   -> True

# All other Xs are True, excepting user-defined objects that
#  implement a boolean value

#   A ? B : C

#  B if A else C

DEBUG = True

color = "purple" if DEBUG else "green"


#  ==  != > < >= <=

#  obj and obj
#  obj or obj

import os
if not  os.path.exists("wombats.txt"):
    print("Sorry, file does not exist")























