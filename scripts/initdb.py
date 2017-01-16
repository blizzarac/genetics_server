#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys


def parseGenomeFile():
    result = []
    f = open(sys.argv[2], 'r')
    with f:
        data = f.readlines()
        for line in data:
            snp = line.split('\t')
            if len(snp) == 4 and not ('#' in snp[0]):
                rsid = snp[0];
                chromosome = snp[1];
                position = snp[2];
                genotype = snp[3].rstrip();
                result.append('INSERT INTO SNP VALUES(' + '\''+ rsid +'\''+ ',' +'\''+ chromosome +'\''+ ',' + position + ',' +'\''+ genotype+'\''+');')
    return result


con = None

try:
    con = lite.connect(sys.argv[1])
    with con:
        cur = con.cursor()  
        snps = parseGenomeFile()
        for snpc in snps:
            cur.execute(snpc)
        con.commit

except lite.Error, e:
    print "Error %s:" % e.args[0]
    sys.exit(1)
    
finally:
    
    if con:
        con.close()




