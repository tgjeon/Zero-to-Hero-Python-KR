# -*- coding: utf8 -*-

"""
08. 완료될 때 까지 이벤트 반복. (소요시간: 22분 강의)

- Original version (MVA): https://mva.microsoft.com/ko/training-courses/python%EC%9D%84-%EC%82%AC%EC%9A%A9%ED%95%9C-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-%EC%86%8C%EA%B0%9C-8360
- Compact version (Youtube): https://youtu.be/emY34tSKXc4?t=2h35m10s
- 참고:
- 아래 설명은 Compact version 영상을 기준으로 작성되었습니다.
"""

"""
완료될 때 까지 이벤트를 반복해봅시다.
"""
answer = '0'

while answer != '4':
    answer = input('What is 2 + 2 ? ')

# while 문 이후 조건이 참인 경우 계속 반복합니다.
# 위에서는 "answer가 4가 아닌 것"이 (참) 인 경우, 계속 반복 수행합니다


"""
거북이를 다시 소환해봅시다.
"""
import turtle
counter = 0
while counter < 4:
    turtle.forward(100)
    turtle.right(90)
    counter = counter+1

# counter를 이용하여 이전에 설명한 아래의 for loop와 동일하게 동작하도록 할 수 있습니다.
#
# import turtle
# for step in range(4):
#     turtle.forward(100)
#     turtle.right(90)

# for와 while을 이용한 두 반복문 모두 동일하게 동작합니다.
# 개인의 기호에 따라 쓰세요
# 하지만, while의 경우 condition을 직접 다루어야 하기 때문에, 특히 인덱스에 조심해서 사용해야합니다
# 조건문에 들어가는 counter를 변화시키는 것을 꼭! 목적에 맞게 바뀌고 있는지 확인해야 합니다.

# 참고자료: Code Complete - Steve McConnell 책을 읽어보시는 걸 추천드립니다.


import turtle
counter = 0
while counter < 4:
    turtle.forward(100)
    turtle.right(90)
    counter += 1

# counter += 1 은 counter = counter + 1 과 동일하게 동작합니다