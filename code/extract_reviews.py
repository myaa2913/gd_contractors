#this file extracts only the reviewid and text columns from
#reviews_UCBerkeley.csv and outputs to /tmp/
import csv, sys

csv.field_size_limit(sys.maxsize)


#read in contractor reviewids and assign to a set
contractIDs = set()
with open('/ifs/gsb/mcorrito/gd_contractors/data/contractor_reviewids.csv','r') as csvfile:
    read = csv.reader(csvfile, delimiter = ',')
    for row in read:
        contractIDs.add(row[0])
csvfile.close()        


#extract the rows we need
header = ['reviewID','pro','con','feedback']

masterFile = open("/data/gsb/amirgo/mac/reviews_UCBerkeley.csv",'rU')
newFile = open("/tmp/extract.csv",'w')
write = csv.writer(newFile)
write.writerow(header)

filtered = (line.replace('\0',' ') for line in masterFile)
filtered = (line.replace('\r\n','. ') for line in filtered)
filtered = (line.replace('\n','. ') for line in filtered)
read = csv.reader(filtered,delimiter=",")

next(read)

for row in read:
    if len(row)==57:
        reviewID = row[0]
        if reviewID in contractIDs:
            dataRow = [row[0],row[54],row[55],row[56]]
            write.writerow(dataRow)

masterFile.close()
newFile.close()
    


    


