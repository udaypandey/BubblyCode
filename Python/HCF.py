def hcf_old(a, b):  
   if a > b:  
       lesser = b  
   else:  
       lesser = a
       
   for c in range(1, lesser + 1):
       #print(f"calculating {c}")
       if((a % c == 0) and (a % c == 0)):  
           hcf = c
           
   return hcf

def hcf(a, b):
    if a > b:  
       lesser = b
       bigger = a
    else:  
       lesser = a
       bigger = b
       
    while lesser > 1:
        #print(f"Check for lesser:{lesser} bigger:{bigger}")
        if bigger % lesser == 0:
            return lesser
        else:
            rem = bigger % lesser
            bigger = lesser
            lesser = rem
    
    return lesser
  
num = int(input("Enter first number: "))  
num2 = int(input("Enter second number: "))
print(f"The HCF of {num} and {num2} is", hcf (num , num2))




        

         
