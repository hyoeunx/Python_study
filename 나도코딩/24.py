# 자료형 비교

#       리스트    튜플    세트    딕셔너리
# 선언   a=[]    a=()   a={}    a={k:v}
# 순서     o      o      x        o
# 중복     o      o      x        x(key)
# 접근    a[i]   a[i]    x      a[key]  a.get(key)
# 수정     o      x      x        o(value)
# 추가  append()  x     add()   a[key] = value
#      insert()      update()   update()
#      extend()
# 삭제  remove()  x    remove()   pop()
#       pop()        discard()  popitem()
#      clear()        clear()   clear()


# 여러 값을 순서대로 관리 : 리스트
# 값이 바뀔 일이 없거나 바뀌면 안됨 : 튜플
# 값의 존재 여부 중요, 중복 안됨 : 세트
# key를 통해 효율적으로 데이터 관리 : 딕셔너리