#module2.py

print("Running module2.py")

import module1

def hello():
    print("{0} says hello".format(__name__))
    module1.hello()