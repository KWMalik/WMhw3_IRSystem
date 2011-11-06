'''
Created on 2011/11/6

@author: EE
'''
class Doc:
    
    docid = ''
    date = ''
    title = ''
    text = '' 
       
    def __init__(self, root):
        doc = root[0]
                        
        self.docid = doc[0].text
        self.date = doc[1].text
        self.title = doc[2].text
        
        text = ''
        paragraphes = doc[3]
        for p in paragraphes:
            text += p.text
        self.text = text
