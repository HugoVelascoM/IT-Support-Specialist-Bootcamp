#Just Importing. This code doesn't execute anything by itself
#from test_module import my_first_module
#calling the function
#my_first_module()

import test_module
#help(test_module)
test_module.my_first_module()


#________________________

#from modules_folder.test_module2 import my_second_module
#my_second_module()

from modules_folder import test_module2
test_module2.my_second_module()