'''
Creating a bed file of array probe coordinates.

Need: xmltocsv tool (http://xmltocsv.codeplex.com/)
Need: agilent design file xml spec (http://xml.coverpages.org/GEMLPattern-dtd.txt) - rename to .dtd

Run xmltocsv tool on the agilent design file and output the reporter csv
Open csv in excel 
Sort on control_type column descending
Delete rows that are control_type pos, neg or ignore
Delete columns: reporter_Id, control_type, active_sequence, start_coord, pattern_Id
Save as csv

Edit script below to update file paths (input and output)
Run
Add bed header as appropriate

python3
'''

import sys
with open('C:/Array/TMP/CGH3.25.txt', encoding='utf-8') as probesfile:
    import csv
    import re
    readprobesfile = csv.reader(probesfile, delimiter = '\t')
    line = 0
    for row in readprobesfile:
        print(line)
        if line < 1:
            #print(row)
            row[1] = re.findall(r"[\w]+", row[1])
            newcolumns = row[1]
            row.append(newcolumns[0])
            row.append(newcolumns[1])
            row.append(newcolumns[2])
            #print(row)
            row = (row[2], row[3], row[4], row[0])
            #print(row)
            with open('C:/Array/TMP/CGH3.25.bed.txt', mode='w', encoding='utf-8', newline='\n') as splitfile:
                splitfilewriter = csv.writer(splitfile, delimiter='\t')
                splitfilewriter.writerow(row)
        if line > 0:
            row[1] = re.findall(r"[\w]+", row[1])
            newcolumns = row[1]
            row.append(newcolumns[0])
            row.append(newcolumns[1])
            row.append(newcolumns[2])
            row = (row[2], row[3], row[4], row[0])
            with open('C:/Array/TMP/CGH3.25.bed.txt', mode='a', encoding='utf-8', newline='\n') as splitfile:
                splitfilewriter = csv.writer(splitfile, delimiter='\t')
                splitfilewriter.writerow(row)
        line += 1

