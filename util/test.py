'''
Created on 2011/11/6

@author: EE
'''
from model.Query import Query 
from elementtree.ElementTree import parse
import sys

#print sys.argv[1]

"""
#Parse an article
tree = parse('cirb010/cdn_chi_0000001')
d = tree.getroot()[0]
doc = Doc(d)
"""

"""
#Parse queries
tree2 = parse('query.xml')
topics = tree2.getroot()
queries = []
for t in topics:
    queries.append(Query(t))
"""