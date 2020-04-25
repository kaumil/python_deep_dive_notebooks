print("RUNNING ----{0}----".format(__name__))

def pprint_dict(header,d):
    """
        Pretty printing a dictionary
    """
    print("\n\n---------------------------")
    print("******** {0} **********".format(header))
    for key, value in d.items():
        print(key,value)
    print("---------------------------\n\n")

pprint_dict("module1.globals",globals())

print("------------- END OF {0} -------------".format(__name__))