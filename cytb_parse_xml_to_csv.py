
import os, Bio, glob
os.chdir('C:\\Users\\asmit\\Desktop\\Cytb_Desktop') ##change directory to location of .xml file
print("Current folder:   " + os.getcwd())
from Bio.Blast import NCBIXML
from Bio import SearchIO
                        
for filename in glob.iglob("*.xml"):
        xml = str(filename)
        text_file = str((xml.rstrip(".xml")) + "_results.csv") ##rename csv as desired
        with open(text_file, "w") as f:
                  result_handle = open(xml)
                  blast_qresult = SearchIO.parse(result_handle, "blast-xml")
                  f.write(str("Animal ID,Top Species Hit" + "\n"))
                  for hit in blast_qresult:
                          f.write(str(("%s" % (hit.id[0:3].rstrip("-_"))) + ",")) ##takes the first 3 characters of hit id (what was submitted to genewiz), alter [0:3] and rstrip as needed
                          for info in hit.hits[:1]: #takes info from the first hit only
                                  species = " ".join(info.description.split(" ")[0:2])
                                  f.write(str(species) + "\n")
                  result_handle.close()
                  f.close()


        

