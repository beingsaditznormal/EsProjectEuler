sumsum =0
sum_ =0 
for i in range(1,101):
    sumsum = sumsum + i*i
    sum_ += i
sum_ = sum_*sum_

print(sum_ - sumsum)