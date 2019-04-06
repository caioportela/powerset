S = input("Insira o conjunto S, separado por espaço: ")
setS = []

for x in S.split():
	if x not in setS:
		setS.append(x)

powerset = [[]]

for x in setS:
	powerset.extend([subset + [x] for subset in powerset])

for sub in powerset:
	print(sub)