import os
os.chdir('C:\\Users\\asmit\\Desktop\\Cytb_Desktop') ##change directory to file location
print("Current folder:   " + os.getcwd())
import Bio, glob
from Bio import SeqIO

for filename in glob.iglob('*download.fasta'):
        name = str(filename)
        newname = str(filename.strip("_download.fasta") + "_trim.fasta")
        print("File procesing: " + name)
        with open(newname, "w") as f: 
                for seq_record in SeqIO.parse(open(name, mode = 'r'), "fasta"):
                        f.write(str(">" + seq_record.id + "\n"))
                        x = 31 ## trim sequence at desired points 
                        while x < 411:
                                f.write(str(seq_record.seq[x:x+50])+ "\n")
                                x = x + 50
                f.close()
print("All files trimmed.")
