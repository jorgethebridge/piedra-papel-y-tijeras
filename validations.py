## Import libreries
import re
## Function Email validation
 
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
 
def checkEmail (email):
    
    ## Valid Email
    if(re.fullmatch(regex, email)):
        return True
 
    else:
        return False   

 
# Validate max number of words

def validateWords (string, maxWords):
    cleanString = string.strip()
    x = re.split("[,;.]\s*|\s+", cleanString)
    
    if len(x) <= int(maxWords):
        return True
    else:
        return False