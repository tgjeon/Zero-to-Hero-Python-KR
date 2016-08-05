"""
02. 변수를 사용해봅시다.
Youtube link: https://youtu.be/emY34tSKXc4?t=20m1s
점프 투 파이썬 (02-2 문자열 자료형) https://wikidocs.net/13
"""

# 사용자로 부터 입력을 받아봅시다.
name = input("이름이 뭔가요?")
# 이름을 출력해봅시다.
print(name)

# 친절하게 이름을 불러볼까요
print('안녕하세요, ' + name)

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
print(message.swapcase()) # 대소문자를 서로 변경 (대문자->소문자, 소문자->대문자)


