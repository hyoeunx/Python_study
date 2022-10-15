# if 중첩

exam = True
d_day = 0

if exam:
    d_day += 1
    if d_day == 1:
        print('시험 첫째날')
    elif d_day == 2:
        print('시험 마지막날')
    else:
        print('시험 끝')
else:
    print('이제 곧..')
    
# 시험 첫째날