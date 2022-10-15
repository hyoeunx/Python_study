# 기본값

def get_if(jw=False):
    if jw == True:
        return 486
    else:
        return 0
    
lv = get_if(True)
print(lv)