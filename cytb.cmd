@echo off
cd C:\Python36\
C:\Python36\python.exe cytb_trim_downloaded_fasta.py
cd C:\Users\asmit\Desktop\Cytb_Desktop
copy *trim.fasta mergeall.fasta
cd C:\Python36\
C:\Python36\python.exe cytb_sort_trimmed_fasta.py
echo Take sorted fasta file (mergesort.fasta) and run NCBI BLAST directly online. Download all the results as a single .xml file. 
timeout /t 600
pause
echo Ensure .xml file is in working folder.
pause
C:\Python36\python.exe cytb_parse_xml_to_csv.py
exit

