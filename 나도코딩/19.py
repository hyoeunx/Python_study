# 튜플2
tuple = ('심', '효', '은')  #패킹(값을 넣는 작업)
n1 = '심'
n2 = '효'
n3 = '은'
(n1, n2, n3) = tuple    #언패킹

numbers = (1, 2, 3, 4, 5)
(one, two, *others) = numbers   #one에 1, two에 2, others에 [3, 4, 5]
(*others, four, five) = numbers #others에 [1, 2, 3], four에 4, five에 5