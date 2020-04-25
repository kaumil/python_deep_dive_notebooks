#the name of the file is kept like this specifically to understand that Python doesn't really care about the name of the file, it just cares about the ModuleType object via which the module is created

print("Running module1.py")

def hello():
    print("{0} says hello".format(__name__))