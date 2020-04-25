import os.path #for manually locating the module
import types
import sys

module_name = "module1" #typically file name is the module name, but we can change it as well
module_file = "module1_source.py"
module_path = '.' #same directory

module_abs_path = os.path.abspath('.')
module_rel_file_path = os.path.join(module_path,module_file)
module_abs_file_path = os.path.abspath(module_rel_file_path)

#reading source code from file
with open(module_rel_file_path,"r") as code_file:
    source_code = code_file.read()

#creating a module object
mod = types.ModuleType(module_name)
mod.__file__ = module_abs_file_path

#set a ref in sys.modules
sys.modules[module_name] = mod

#compile source code
code = compile(source_code, filename=module_abs_file_path, mode="exec")

#execute compiled source code
exec(code,mod.__dict__) #exec will execute all that compiled code and put it in the global dictionary

#we have successfully created a module

import module1 #even if module1 isn't there python will execute the following call if the above code is present. that is because python stores the module name(module1) in sys.modules and when importing, even when we aren't able to import the module, we are able to execute the function as the module name is present in sys.modules
module1.hello()