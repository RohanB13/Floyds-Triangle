x = input('Insert the number of rows here ') 
def floyd(n):
   count = 1
   string = ""
   for i in range(1,n+2):
       for j in range(1,i):
           string = string + " " + str(count)
           count = count + 1
       print(string)
       string = ""
print floyd(x)
