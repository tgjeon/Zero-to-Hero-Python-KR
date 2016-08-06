# -*- coding: utf8 -*-

"""
04. 날짜를 사용해봅시다. (소요시간: 16분 강의)

- Original version (MVA): https://mva.microsoft.com/ko/training-courses/python%EC%9D%84-%EC%82%AC%EC%9A%A9%ED%95%9C-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-%EC%86%8C%EA%B0%9C-8360
- Compact version (Youtube): https://youtu.be/emY34tSKXc4?t=1h17m24s
- 참고:
- 아래 설명은 Compact version을 기준으로 합니다.
"""


"""
날짜 및 시간을 다뤄봅시다.
"""

# datetime 클래스를 이용합니다.
import datetime

today = datetime.date.today()
print(today)

"""
자주 사용되는 날짜들

%b: 월 (약어)
%B: 월
%y: 2자리 연도
%a: 요일 (약어)
%A: 요일

자세한 내용: strftime.org
"""
print(today)
print(today.month)
print(today.year)

print(today.strftime('%d %b, %Y'))



"""
사용자로부터 입력을 받아서 포맷을 바꿔봅시다.
"""

birthday = input("생일이 언제입니까? ")
birthdate = datetime.datetime.strptime(birthday, "%m/%d/%Y")

print(birthdate)



