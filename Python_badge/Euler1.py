count=0
summ = 0


while count<1000:
    if count%3 == 0 or count%5==0:
        summ+= count
    count += 1

print(summ)