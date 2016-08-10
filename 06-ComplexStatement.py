# -*- coding: utf8 -*-

"""
06. 코드로 복잡한 결정 내리기. (소요시간: 15분 강의)

- Original version (MVA): https://mva.microsoft.com/ko/training-courses/python%EC%9D%84-%EC%82%AC%EC%9A%A9%ED%95%9C-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-%EC%86%8C%EA%B0%9C-8360
- Compact version (Youtube): https://youtu.be/emY34tSKXc4?t=1h48m
- 참고:
- 아래 설명은 Compact version 영상을 기준으로 작성되었습니다.
"""

"""
복잡한 결정을 내려봅시다.
: 주어진 조건을 만족하면 상응하는 명령 수행.
"""

team = input("Enter your favorite hockey team: ").upper()

if team == "FLYERS":
    print("Best team ever!!")
elif team == "SENATORS":
    print("Go Sens Go!")
elif team == "RANGERS":
    print("Go Rangers")
else:
    print("I don\'t have anything clever to say here")


"""
여러 조건들을 복합적으로 사용해 봅시다. (and)
"""

# 두 개의 조건이 모두 "참" 일 경우: and
wonLottery = True
bigWin = True

if wonLottery and bigWin:
    print("You can retire")




# 입력을 받아서 두 개의 조건을 and 로 비교해 봅시다.
team = input("Enter your favorite hockey team: ").upper()
sport = input("Enter your favorite sport: ").upper()

if sport == 'HOCKEY' and team == 'RANGERS':
    print("I miss Messier")
else:
    print("I don't know that team")



"""
여러 조건을 복합적으로 사용해 봅시다. (or)
"""

# 두 개의 조건중 하나 이상이 "참" 일 경우: or
saturday = True
sunday = False

if saturday or sunday:
    print("I can sleep")


# 입력을 받아서 두 개의 조건을 or 로 비교해 봅시다.
team = input("Enter your favorite hockey team: ").upper()
sport = input("Enter your favorite sport: ").upper()

if sport == 'HOCKEY' and team == 'RANGERS':
    print("I miss Messier")
elif team == 'LEAFS' or team == 'SENATORS':
    print("Good luck getting the cup this year")
else:
    print("I don't know that team")


# 여러가지 "and"와 "or"을 하나의 if 문에 섞어서 사용해봅시다.
# \ 를 이용하여 여러줄로 조건을 연결해서 표현할 수 있습니다
month = "Sep"

if month == "Sep" or month == "Apr" \
    or month == "Jun" or month == "Nov":
    print("There are 30 days in this month")

favMovie = "Star Wars"
favBook = "Lord of the Rings"
favEvent = "ComiCon"

if favMovie == "Star Wars" \
    and favBook == "Lord of the Rings" \
    and favEvent == "ComiCon":
    print("You and I should hang out")

"""
and 와 or 을 하나의 선택문에서 같이 사용한다면 주의해야 합니다.
"""
# and 와 or을 섞어서 사용한다면?

country = "VIETNAM"
pet = "BEAVER"

if country == "CANADA" and \
    pet == "MOOSE" or pet == "BEAVER":
    print("Do you play hockey too?")

# 처음부터 작성된 순서대로 판단됩니다. 원치 않는 상황에서도 작동할 수 있습니다.
# 위 코드는 "CANADA"라는 국가와 "MOOSE" 혹은 "BEAVER"라는 상황에 대해서 작동하도록 의도되었습니다.

if country == "CANADA" and pet == "MOOSE" \
    or pet == "BEAVER":
    print("Do you play hockey too?")




# 만약 스포츠가 하키이고 팀이 senators나 leafs라면 cup 메세제를 보여줍시다
team = input("Enter your favorite hockey team: ").upper()
sport = input("Enter your favorite sport: ").upper()

if sport == 'HOCKEY' and (team == 'SENATORS' or team == 'LEAFS'):
    print("Good luck getting to the cup this year")

# 위와 같이 괄호로 묶어주면, team 부분을 먼저 비교하고, 그 이후 sport 부분을 비교하게 됩니다.