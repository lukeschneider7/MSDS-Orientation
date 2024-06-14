last = 0
current = 1
fib_list = list()
fib_list_even = list()

while current < 4000000:
   #summ += fib
   new = current + last
   last = current
   current = new
   
   
   fib_list.append(last)

for num in fib_list:
   if num%2==0:
      fib_list_even.append(num)

print(sum(fib_list_even))
