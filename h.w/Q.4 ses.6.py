list=[1,5,6]
answer=""

for i in range(len(list)-1):
    if list[i]<list[i+1]:
        continue
    else:
        answer=False
        break
else:
    answer=True
print(answer)