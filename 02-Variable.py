"""
02. 변수를 사용해봅시다. (19분)

- Original version (MVA): https://mva.microsoft.com/ko/training-courses/python%EC%9D%84-%EC%82%AC%EC%9A%A9%ED%95%9C-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-%EC%86%8C%EA%B0%9C-8360
- Compact version (Youtube): https://youtu.be/emY34tSKXc4?t=20m1s
- 참고: 점프 투 파이썬 (02-2 문자열 자료형) https://wikidocs.net/13
- 아래 설명은 Compact version을 기준으로 합니다.
"""

# 사용자로 부터 입력을 받아봅시다.
name = input("이름이 뭔가요? ")
country = input("어느 나라에 살고 있나요? ")
country = country.upper()  # 예) kr => KR
# 이름을 출력해봅시다.
print(name)

# 친절하게 이름을 불러볼까요
print('\n안녕하세요, ' + name + ". 당신은 " + country + "에 살고 있군요.")

# 이름을 바꿔볼까요?
name = "Taegyun Jeon"
print(name)

"""
이야기를 전해주는 프로그램을 만들어 볼까요?
"""

animal = input("가장 좋아하는 동물이 뭔가요? ")
building = input("유명한 건물의 이름: ")
color = input("가장 좋아하는 색상은 무엇인가요? ")
print("Hickory Dickory Dock!")
print(color+" "+animal+"이 "+building+" 위로 올라갑니다.")


"""
변수 내용을 고쳐봅시다.
"""
message = 'Hello world'
print(message.lower())  # 소문자로
print(message.upper())  # 대문자로
print(message.swapcase())  # 대소문자를 서로 변경 (대문자->소문자, 소문자->대문자)


"""
아래 함수들이 어떻게 동작할까요?
정답은 맨 아래로 내려가서 찾아보세요.
(문자열 퀴즈 #01)
"""
message = 'Hello world'
print(message.find('world'))
print(message.count('o'))
print(message.capitalize())
print(message.replace('Hello', 'Hi'))
print(message)


"""
프로그래머는 모든 함수들을 기억하기 힘듭니다.
"""
# 프로그래밍 도구의 IntelliSense (자동완성) 기능을 사용하세요
# 해당 언어의 Decumentation을 참고하세요. 링크를 꼭 챙겨두기! https://www.python.org/doc/
# 인터넷 검색! Google God!


"""
아래 표현들중 어디가 틀렸는지 생각해봅시다.
(문자열 퀴즈 #02)
"""
# Q1) message = Hello world
# Q2) 23message = 'Hello world'
# Q3) New message = 'Hi there'
# Q4) print(message.upper)
# Q5) print(messge.lower())
# Q6) print(message.count())







"""
중간 문제의 힌트
"""
# (문자열 퀴즈 #01)
# Hint 1. 'world'의 문자열이 있는지 찾고, 있다면 시작 위치를 알려줍니다. 파이썬은 0부터 시작. 그래서 world의 시작위치는 6
# Hint 2. 'o'라는 문자열이 몇개 있는지 세어봅니다. 각자 세어보고 확인해보세요.
# Hint 3. 해당 문자열의 첫 글자만 대문자로 바꿔줍니다. 첫 글자를 소문자로 바꿔보고 확인해보세요.
# Hint 4. 'Hello'를 찾아서 'Hi'로 바꿔줍니다.
# 모든 함수들은 변수의 원래 문자열에 영향을 주지 않습니다.


# (문자열 퀴즈 #02)
# Hint 1. 문자열 변수는 따옴표를 사용해야 합니다.
# Hint 2. 변수명은 숫자로 시작할 수 없습니다.
# Hint 3. 변수명에 공백을 포함할 수 없습니다.
# Hint 4. 함수를 사용할 때 ()를 써야합니다.
# Hint 5. 변수명을 정확히 써야겠죠?
# Hint 6. 함수의 인자가 필요한 때 꼭 인자를 작성해야 합니다.

