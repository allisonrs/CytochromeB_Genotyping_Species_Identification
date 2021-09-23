# CytochromeB_Genotyping_Species_Identification
Generate a .csv file containing the exact species of an organism as determined by cytochrome b genotyping. 

The program trims numerous multifasta files (generated from sanger sequencing or elsewhere) and merges the trimmed files to generate one multifasta file with all sequences. 
The trimmed file is run manually on NCBI BLAST and the XML file downloaded. The program continues, parsing the XML file return the species name from top hit for each entry.

  This program uses a combination of CMD and Python.  
The script to run NCBI BLAST via Biopython is included, but runs too slowly to be worth automating. 
It is significantly faster to pause the program, upload the merged .fasta file, run BLAST manually on https://blast.ncbi.nlm.nih.gov/Blast.cgi?PROGRAM=blastn&PAGE_TYPE=BlastSearch&LINK_LOC=blasthome, and download the resulting XML file. 

Prior to running the program, ensure the following:

  all .fasta files named such it ends with "_download" , i.e. sanger1_download.fasta.
  
  all .fasta files are in a dedicated folder. Manually set the folder location in each of the scripts (Python and CMD)
  
  all python scripts are located in working Python folder, and that the Python folder is correctly set in the CMD script.     
