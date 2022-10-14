# 문자열 메소드 1

letter = 'how are YOU?'

# 모든 내용 소문자로
print(letter.lower()) # how are you?

# 첫 글자만 대문자로
print(letter.capitalize()) # How are you?

# 각 단어들의 첫 글자만 대문자로
print(letter.title()) # How Are You?

# 대소문자를 뒤바꿈
print(letter.swapcase()) # HOW ARE you?

# 문자열을 나눔
print(letter.split()) # ['how', 'are', 'YOU?']

# 'how'가 몇 번 쓰였는지?
print(letter.count('how')) # 1