'''
Created on 2011/11/12

@author: EE
'''
import sys
import codecs
import os
from elementtree.ElementTree import parse
from model.Query import Query

if len(sys.argv) == 3:
    
    #Retrieve the file list
    filelist = os.listdir(sys.argv[1])
    
    for filename in filelist:
        path = sys.argv[1] + '\\' + filename
        newpath = sys.argv[2] + '\\' + filename
        uni = newpath + '_unigram '
        bi = newpath + '_bigram '
        tri = newpath + '_trigram '        
        
        os.system('create-ngram.exe -vocab vocab.all -n 1 -o ' + uni + ' -encoding utf8 ' + path) 
        os.system('create-ngram.exe -vocab vocab.all -n 2 -o ' + bi + ' -encoding utf8 ' + path)
        os.system('create-ngram.exe -vocab vocab.all -n 3 -o ' + tri + ' -encoding utf8 ' + path)        
        os.system('merge-ngram.exe -o ' +newpath+'_ngram ' + uni + bi + tri)
        
else:
    print "Usage: python GetDocText [dir] [output dir]"
