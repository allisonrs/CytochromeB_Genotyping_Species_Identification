import os
os.chdir('C:\\Users\\asmit\\Desktop\\Cytb_Desktop')
print("Current folder:   " + os.getcwd())
import Bio, glob
from Bio import SeqIO
from Bio.Blast import NCBIWWW

for filename in glob.iglob('*mergesort.fasta'):
        name = str(filename)
        newname = str(filename.strip(".fasta") + ".xml")
        print("Running BLAST on " + name)
        record = open(name).read()
        result_handle = NCBIWWW.qblast("blastn", "nt", record, hitlist_size=1)
        print("BLAST on " + name + " is complete.")
        with open(newname, "w") as out_handle: 
                out_handle.write(result_handle.read())
                out_handle.close()
                result_handle.close()
print("All files BLASTed")
