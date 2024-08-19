import io
def countfruits(msg):
    sfp = io.StringIO(msg)
    fruit_counts = dict()

    x = sfp.readline().strip()  
    if(not x):
        x = sfp.readline().strip()
    while x != '':
        fruit, count = x.split(' ')  
        count = int(count)  
        
        if fruit not in fruit_counts:
            fruit_counts[fruit] = count  
        else:
            fruit_counts[fruit] += count 
        x = sfp.readline().strip()  
    
    return fruit_counts 