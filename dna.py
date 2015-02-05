from sys import argv

script, dna_file = argv

f=open(dna_file)

counts = {"A": 0, "G": 0, "T": 0, "C": 0}

for line in f:
	line = line.strip()
	for char in line:
		counts[char] = counts[char] + 1

print counts["A"], counts["C"], counts["G"], counts["T"]

f.close()
