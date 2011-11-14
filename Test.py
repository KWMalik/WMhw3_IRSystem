'''
Created on 2011/11/14

@author: EE
'''
from model.Doc import Doc
from elementtree.ElementTree import parse
import sys
import os
import codecs
from elementtree.ElementTree import parse
from model.Query import Query
from model.Doc import Doc
import string
from util.ReadFiles import getAnswerList
import math

#Get query
xml = parse(sys.argv[1]) #argv[1] = query.xml
q = Query(xml.getroot()[4])
print q.title
    
#Create ngram and count mapping for a query
q.createNGram()

if len(sys.argv) == 2:
    
        filename = 'cdn_foc_0008072'
        d=Doc('cirb010\\' + filename)
        d.createNGram(filename)

        #Calculate probability            
        p = 1.0
        mu = 150.0
        d_size = 150.0
        
        for key in q.wordcount.keys():            
            p1 = 0.0  
            p2 = 0.0001          
            if d.wordcount.has_key(key):                                
                p1 = (d_size / (d_size + mu)) * (float(d.wordcount[key]) / float(d.totalcount))                        
            print p1 + p2
            p *= (p1 + p2)            
        
        d.prob = p
        print 'd.prob', d.prob
        print d.wordcount
        
        
        

        filename = 'cdn_foc_0008536'
        d=Doc('cirb010\\' + filename)
        d.createNGram(filename)

        #Calculate probability            
        p = 1.0
        mu = 150.0
        d_size = 150.0

        for key in q.wordcount.keys():            
            p1 = 0.0  
            p2 = 0.0001          
            if d.wordcount.has_key(key):                                
                p1 = (d_size / (d_size + mu)) * (float(d.wordcount[key]) / float(d.totalcount))                        
            print p1 + p2
            p *= (p1 + p2)            
        
        d.prob = p
        print 'd.prob', d.prob
        print d.wordcount

        filename = 'cdn_foc_0008072'
        d=Doc('cirb010\\' + filename)
        d.createNGram(filename)

        #Calculate probability            
        p = 1.0
        mu = 150.0
        d_size = 150.0
        
        for key in q.wordcount.keys():            
            p1 = 0.0  
            p2 = 0.0001          
            if d.wordcount.has_key(key):                                
                p1 = (d_size / (d_size + mu)) * (float(d.wordcount[key]) / float(d.totalcount))                        
            print p1 + p2
            p *= (p1 + p2)            
        
        d.prob = p
        print 'd.prob', d.prob
        print d.wordcount
