'''
Created on 2011/11/6

@author: EE
'''
import sys
import codecs
import os
from elementtree.ElementTree import parse
from Doc import Doc

if len(sys.argv) == 3:
    
    #Retrieve the file list
    filelist = os.listdir(sys.argv[1])
    
    for filename in filelist:        
        #Parse a file as an xml object
        xml = parse(sys.argv[1] + "\\" + filename)
        d = Doc(xml.getroot())
        
        #Output as a pure text
        fout = codecs.open(sys.argv[2]+ "\\" + filename, encoding='utf-8', mode='w')
        fout.write(d.text)
        fout.close()
        
else:
    print "Usage: python GetDocText [dir] [output dir]"
