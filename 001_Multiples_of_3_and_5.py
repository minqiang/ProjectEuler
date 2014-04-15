answer = [x for x in range(1000) if (x%3==0 or x%5==0)]
result = 0
for i in answer: 
    result += i
print result