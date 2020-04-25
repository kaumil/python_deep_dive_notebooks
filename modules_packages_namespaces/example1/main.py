print("===============================")

print("Running main.py - module name: {0}".format(__name__))

import module1
print(module1)

module1.pprint_dict("main.globals",globals())

print("IMPORTING module1 again..") #it wont import module1 again, it would first look into sys.modules
import module1

print("===============================")