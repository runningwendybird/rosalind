from sys import argv

script, rna_file = argv

f=open(rna_file)

dna = f.read()

rna = ""

placeholder = 0

for i in range(len(dna)):
	if dna[i] != "T":
		rna = rna + dna[i]
	else:
		rna = rna + "U"

print rna

