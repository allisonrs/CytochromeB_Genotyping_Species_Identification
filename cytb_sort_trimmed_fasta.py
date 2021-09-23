import os, Bio, glob, natsort
os.chdir('C:\\Users\\asmit\\Desktop\\Cytb_Desktop') ##change directory to file location
print("Current folder:   " + os.getcwd())
from Bio import SeqIO, SearchIO
from natsort import natsorted,ns

with open("mergesort.fasta", "w") as f:
    l = SeqIO.parse("mergeall.fasta", "fasta")
    sortedList = [f for f in natsorted(l, key=lambda x : x.id)]
    for s in sortedList:
        f.write(str(">" + s.description)+ "\n")
        for x in range(0, len(s.seq), 50):
            f.write(str((s.seq[x:x+50]+ "\n")))
    f.close()
print("Sorted")
