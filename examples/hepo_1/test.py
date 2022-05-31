f = open("ADSOR","r")
atoms_symbol = f.readline().split()
atoms_num = list(map(int,f.readline().split()))

print(atoms_symbol)
print(atoms_num)
f.close()
