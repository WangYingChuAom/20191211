word = input()
new = []
newword = []
for i in word:
	new.append(i)
for j in range(len(new)-1,-1,-1):
	newword.append(new[j])

for k in range(len(newword)):
	print(newword[k], end= '')

