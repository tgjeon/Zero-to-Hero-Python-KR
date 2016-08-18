# -*- coding: utf8 -*-

"""
07. 이벤트 반복. (소요시간: 6분 강의)

- Original version (MVA): https://mva.microsoft.com/ko/training-courses/python%EC%9D%84-%EC%82%AC%EC%9A%A9%ED%95%9C-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-%EC%86%8C%EA%B0%9C-8360
- Compact version (Youtube): https://youtu.be/emY34tSKXc4?t=2h29m7s
- 참고:
- 아래 설명은 Compact version 영상을 기준으로 작성되었습니다.
"""

"""
반복적인 일을 해봅시다.
"""

import turtle
for step in range(4):
    turtle.forward(100)
    turtle.right(90)

# step: 반복된 상태에 대한 변수로 사용됩니다.
# in 이후 선언된 숫자만큼 반복 합니다.
# 들여쓰기로 된 구문들을 반복합니다.

turtle.color('red')
turtle.forward(200)

# 들여쓰기를 벗어나면 반복할 구간에서 벗어납니다.
# 위 구문도 반복해서 실행하고 싶다면 for loop 아래 구문들과 같은 들여쓰기로 바꿔보세요.

"""
아래 코드에서 틀린 부분을 찾아봅시다
"""

# improt turtle
# for steps in range(4)
#       turtle.forward(100)
# turtle.right(90)

