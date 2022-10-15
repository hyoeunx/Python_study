# continue

school = ['어린이집', '유치원', '초등학교', '중학교', '고등학교', '대학교']
for a in school:
    if a == '중학교':
        print(f'{a} 자퇴하겠다.')
        continue
    print(f'{a} 졸업')