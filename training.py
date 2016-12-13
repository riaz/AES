import csv
import sys
import string
printable= set(string.printable)

a = 'data/'
b = 'fold_0/'

ip = ['train_ids.txt','test_ids.txt','dev_ids.txt']
op = ['train.tsv','test.tsv','dev.tsv']

for j,c in enumerate(ip):
    print c,op[j]
    with open('training_set_rel3.tsv','rb') as tsvin, open(a+b+c) as f, open(op[j], 'wb') as tsvout:
        tsvin = csv.reader(tsvin, delimiter='\t')
        tsvout = csv.writer(tsvout,delimiter='\t')
        lines= f.readlines()
        i=0
        is_header = True
        for row in tsvin:
             if is_header:
                 is_header = False
                 continue
             #print int(row[0])  == int(lines[i]), row[0],lines[i]
             if int(row[0]) == int(lines[i]):
                 row = [ filter(lambda x: x in printable, s) for s in row]
                 tsvout.writerow(row)
                 i+=1
         
