import sys
import importer #it will print Running importer.py

module1 = importer.import_('module1','module1_source.py','.') #it will import modules from module1_source.py in the same directory(cuz '.')

print(globals()) #this will contain module1 in the globals() dictiionary
module1.hello()

import module2
module2.hello() #if we run this hello function it won't print importing module1.py as module1 is imported only once and then it is registered in sys.modules hence when module1.hello is called in module2, it won't import it again and then just run the hello function in module1