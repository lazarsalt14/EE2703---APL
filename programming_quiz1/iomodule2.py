import io
from collections import defaultdict
def circuit_count(msg):
    sfp = io.StringIO(msg)
    ans_dict=defaultdict(int)
    x=sfp.readline().strip()

    while(".circuit" not in x):
        x=sfp.readline().strip()
    while(x!=''):
        if(".circuit" in x):
            x=sfp.readline().strip()
            continue 
        if(".end" in x):
            break
        else:
            ans_dict[x[0]]+=1
        x=sfp.readline().strip()  
        
    
    return ans_dict
