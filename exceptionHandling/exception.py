

try:
    print(23/0)  # for this code except part willl run  
    print(23/2)# else part will run for this code 
    
except ZeroDivisionError:  # ZeroDivisionError this is the keyword 
    print("you try to divide with zero ")

else:
    print("if try code is correct then it will run ")


finally:                      # finally code will run always doesn't depend on the above code  
    print("now you are out of the DB ")




