n, s = map(int, input().split())
num_list = list(map(int, input().split()))

count=0
def sum_func(index, sum):
    global count
    if index > n-1:
        return False
    sum = sum+num_list[index]
    sum_func(index+1, sum)
    sum_func(index+1, sum - num_list[index])
    if sum == s:
        count +=1
        return False
      

sum_func(0, 0)
print(count)
