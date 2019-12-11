num = int(input())
count = 0
for i in range(num):
	if i % 3 == 0 or i % 5 == 0:
		if i % 15 == 0:
			count = count + 1
	else:
		count = count + 1
print(count)