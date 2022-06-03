import sys

n = int(input())

st_list=[]
for _ in range(n):
    st_list.append(sys.stdin.readline().split())

def func_name(data):
    return data[0]

def func_korean(data):
    return int(data[1])

def func_english(data):
    return int(data[2])

def func_math(data):
    return int(data[3])

st_list.sort(key=func_name)
st_list.sort(key=func_math, reverse=True)
st_list.sort(key=func_english)
st_list.sort(key=func_korean, reverse=True)

for i in st_list:
    print(i[0])