# -*- coding: utf8 -*-

"""
05. 코드로 결정 내리기. (소요시간: 15분 강의)

- Original version (MVA): https://mva.microsoft.com/ko/training-courses/python%EC%9D%84-%EC%82%AC%EC%9A%A9%ED%95%9C-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-%EC%86%8C%EA%B0%9C-8360
- Compact version (Youtube): https://youtu.be/emY34tSKXc4?t=1h33m1s
- 참고:
- 아래 설명은 Compact version을 기준으로 합니다.
"""

"""
입력을 받아서 결정을 내려봅시다.
"""

favouriteTeam = input("선호하는 하키팀은? ")
if favouriteTeam == "Senators":
    print("Yeah Go Sens Go")
    print("But I miss Alfredsson")
print("It's okay if you prefer football/soccer")


"""
실제 프로그래밍의 경우 다양하게 입력되는 경우를 고려해야 합니다.
변수로 미리 정의 해두고 사용한다면,
그 변수 값이 사용자가 직접 입력하던지, 혹은 파일에서 불러오거나, DB에서 불러오던지 상관하지 않아도 됩니다.
"""

bestTeam = "SENATORS"

favouriteTeam = input("선호하는 하키팀은? ")
if favouriteTeam.upper() == bestTeam.upper():
    print("Yeah Go Sens Go")
    print("But I miss Alfredsson")
print("It's okay if you prefer football/soccer")


"""
여러가지 선택을 해봅시다.
"""

country = input("Where are you from? ").upper()

if country == "CANADA":
    print("Hello")
elif country == "GERMANY":
    print("Guten Tag")
elif country == "FRANCE":
    print("Bonjour")

