import theater_module as tm
tm.price(3)
tm.price_morning(4)
tm.price_soldier(5)

# from theater_module import * #모듈 안의 모든 함수를 들고와서 여기서 선언한 것처럼 만들어 줌
# price(3)
# price_soldier(5)

from theater_module import price    #price만

import theater_module as mv
mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)

from theater_module import *
price_morning(4)
price_soldier(5)

from theater_module import price, price_morning
price(3)
price_morning(4)
price_soldier(5)

from theater_module import price_soldier as price
price(5)