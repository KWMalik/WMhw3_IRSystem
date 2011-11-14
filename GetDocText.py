'''
Created on 2011/11/6

@author: EE
'''
import sys
import codecs
import os
from elementtree.ElementTree import parse
from model.Doc import Doc

if len(sys.argv) == 3:
    
    #Retrieve the file list
    filelist = os.listdir(sys.argv[1])
    
    for filename in filelist:        
        #Parse a file as an xml object
        #Need to be modified
        d = Doc(sys.argv[1] + "\\" + filename)       
        
        #Output as a pure text
        fout = codecs.open(sys.argv[2]+ "\\" + filename, encoding='utf-8', mode='w')
        fout.write(d.title)
        fout.close()
        
else:
    print "Usage: python GetDocText [dir] [output dir]"
