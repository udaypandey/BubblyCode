def hcf(a, b):  
   if a > b:  
       lesser = b  
   else:  
       lesser = a  
   for c in range(1,lesser + 1):  
       if((a % c == 0) and (a % c == 0)):  
           hcf = c 
   return hcf  
  
num = int(input("Enter first number: "))  
num2 = int(input("Enter second number: "))
print(f"The HCF of {num} and {num2} is", hcf (num , num2))




        

         
