# -*- coding: utf8 -*-

"""
03. 숫자형을 사용해봅시다. (소요시간: 38분 강의)

- Original version (MVA): https://mva.microsoft.com/ko/training-courses/python%EC%9D%84-%EC%82%AC%EC%9A%A9%ED%95%9C-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-%EC%86%8C%EA%B0%9C-8360
- Compact version (Youtube): https://youtu.be/emY34tSKXc4?t=38m56s
- 참고: 점프 투 파이썬 (02-1 숫자형) https://wikidocs.net/12
- 아래 설명은 Compact version을 기준으로 합니다.
"""

"""
문자열을 다뤘던것 처럼, 숫자를 변수에 할당해서 써봅시다.
"""
area = 0
height = 10
width = 20

# 삼각형의 밑변과 높이를 이용하여 면적을 계산해봅시다.
area = width * height / 2

print(area)

"""
숫자를 보여줄 때, 양식에 맞춰서 보여줄 필요가 있습니다.
"""
# 아래 라인을 코멘트 제거하고 실행해보세요.
# print("the area of the triangle would be " + area)
# 에러 발생!!
# 문자열과 숫자는 단순히 합쳐지지 않는군요.

# Placeholder: %d와 같이 숫자가 들어갈 "위치"를 지정해줍니다.
# Value: % 뒤에 숫자, 혹은 숫자형 "값"을 지정해줍니다.
print("the area of the triangle would be %d" % area)

# "위치" 부분에 양식을 같이 지정할 수 있습니다.
print("the area of the triangle would be %d" % area)  # 정수로 표현
print("the area of the triangle would be %4d" % area)  # 몇칸을 쓸것인가?
print("the area of the triangle would be %04d" % area)  # 빈칸은 0으로 채우자
print("the area of the triangle would be %f" % area)  # 실수로 표현
print("the area of the triangle would be %.2f" % area)  # 소수점 자리수 지정


# 다른 형태로 양식을 지정할 수 있습니다.
# Placeholder: {0:d} 0번째 값은 정수
# Value: .format(값)
print("\nBracelet syntax")
print("the area of the triangle would be {0:d}".format(100))  # 정수로 표현
print("the area of the triangle would be {0:4d}".format(100))  # 몇칸을 쓸것인가?
print("the area of the triangle would be {0:04d}".format(100))  # 빈칸은 0으로 채우자
print("the area of the triangle would be {0:f}".format(area))  # 실수로 표현
print("the area of the triangle would be {0:.2f}".format(area))  # 소수점 자리수 지정

# 여러개를 양식을 이용하여 써봅시다.
print("\n여기 숫자 3개가 있습니다. 첫째, {0:d}. 두번째, {1:4d}. 그리고 {2:d}.".format(7, 8, 9))

# 들여쓰기 (indent) 를 이용하여 이전줄과 연결된다는 것을 표현합니다.
print("\n여기 숫자 3개가 있습니다. " +
      "첫째, {0:d}. 두번째, {1:4d}. 그리고 {2:d}.".format(7, 8, 9))


"""
숫자를 입력 받아서 사용해봅시다.
"""
salary = input("please enter your salary ")
bonus = input("please enter your bonus ")

paycheckAmount = salary + bonus
print(paycheckAmount)

# 엉뚱한 결과가 나옵니다.
# hint. input() 함수는 문자형을 반환합니다.

# 그래서 문자형 대신 숫자형으로 사용하는 방법을 찾아야합니다.
# 데이터 타입을 바꿔주는 함수들이 있습니다.
# int(value), long(value), float(value), str(value)

# 이제 데이터 타입을 바꿔서 해봅시다.
paycheckAmount = float(salary) + float(bonus)
print(paycheckAmount)

# 이제 + 연산자가 문자열끼리 연결이 아니라, 숫자형의 덧셈 연산으로 동작합니다.

# 하지만 숫자형을 입력할 것이라고 예측했지만, 누군가 salary에 문자형 값을 입력하면 어떻게 될까요?
# 각자 해봅시다.


"""
도전과제!
: 대출 계산기를 만들어봅시다.
1. 사용자가 "대출금액", "대출이자", "대출기간(년)"을 입력합니다.
2. 매달 상환금을 아래와 같은 식으로 계산해 보세요.

 M = L[i(1+i)n] / [(1+i)n-1]

 M = 매달 상환금
 L = 대출금
 i = 대출이자 (이자가 5%라면, i=0.05로 표시)
 n = 상환 횟수
"""