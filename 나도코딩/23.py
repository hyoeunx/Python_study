# 딕셔너리 2

hyoeun = {'이름':'심효은', '나이':'17', '키':'162'}

print(hyoeun.get('학교'))   #없는 key에 접근하면 None 출력

hyoeun['학교'] = '부산소마고'   #새로운 데이터 추가
print(hyoeun)   #{'이름': '심효은', '나이': '17', '키': '162', '학교': '부산소마고'}

hyoeun['키'] = '180'   #특정 key의 value 변경

hyoeun.update({'이름':'김정우', '나이':'18'})   #여러 key의 value 변경

hyoeun.pop('학교')  #특정 key:value 삭제

hyoeun.clear()  #모든 데이터 삭제

hyoeun = {'이름':'심효은', '나이':'17', '키':'162'}

print(hyoeun.keys())    #어떤 key들이 있는지

print(hyoeun.values())  #어떤 value들이 있는지

print(hyoeun.items())   #어떤 key:value들이 있는지  #dict_items([('이름', '심효은'), ('나이', '17'), ('키', '162')])
