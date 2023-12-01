def easy_print(**x):
    for key, value in x.items():
        print('The value of ' + 
              str(key) + " is " + 
              str(value))
        
        
easy_print(a=18), easy_print(b=32)