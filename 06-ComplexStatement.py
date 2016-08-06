# -*- coding: utf8 -*-

"""
06. 코드로 복잡한 결정 내리기. (소요시간: 15분 강의)

- Original version (MVA): https://mva.microsoft.com/ko/training-courses/python%EC%9D%84-%EC%82%AC%EC%9A%A9%ED%95%9C-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-%EC%86%8C%EA%B0%9C-8360
- Compact version (Youtube): https://youtu.be/emY34tSKXc4?t=1h48m
- 참고:
- 아래 설명은 Compact version을 기준으로 합니다.
"""

"""
복잡한 결정을 내려봅시다.
"""

team = input("Enter your favourite hockey team: ").upper()

if team == "FLYERS":
    print("Best team ever!!")
elif team == "SENATORS":
    print("Go Sens Go!")
elif team == "RANGERS":
    print("Go Rangers")
else:
    print("I don\'t have anything clever to say here")


"""
여러 조건들을 복합적으로 사용해 봅시다.
"""

