# What this code can do?
1. merge .nessus 2 files at a time
2. For example
 - file1.nessus -> ip 192.168.88.2, 192.168.88.3, 192.168.88.4
 - file2.nessus -> ip 192.168.88.5, 192.168.88.6
 - output is "merged.nessus" -> ip 192.168.88.2, 192.168.88.3, 192.168.88.4, 192.168.88.5, 192.168.88.6

# How to Merge
1. Export the nessus that you wanna merge
2. set your export file name to "file1.nessus" and "file2.nessus"
3. then run with "py merge_nessus.py" #use Python 3.11.4
