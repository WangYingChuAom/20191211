word = input()
word = word.split()

for i in range(len(word)):
	new = []
	newword = []
	for j in word[i]:
		new.append(j)
	for k in range(len(new)-1,-1,-1):
		newword.append(new[k])
	for m in range(len(newword)):
		print(newword[m],end='')
	if (i != len(word)-1):
		print(' ',end='')
x = input()