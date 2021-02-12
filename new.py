def func(x):
  res = 0
  for i in range(x):
     res += i
  return res

print(func(4))
print("hello world")
print(func(3))

for i in range(5):
    print(i)
    
n = 0
while(n<8):
  print(n)
  n = n +1
  
# Multiplication table

# To take input from the user
num = int(input("Display multiplication table of? "))

# Iterate 10 times from i = 1 to 10
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)
