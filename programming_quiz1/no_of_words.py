def word_count(s):
    if(len(s)==0):
        return 0
    number=1
    checker=True
    for char in s:
        if(char ==' ' and checker ):
            number+=1
            checker=False
        if(not checker):
            if(char!=' '):
                checker=True
    if(s[-1]==' '):
            number-=1            
    return number   