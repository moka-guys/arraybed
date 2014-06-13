arraybed
========
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



python3
