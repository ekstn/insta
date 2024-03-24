num1 = 100
num2 = 200
print(num1, "+", num2, "=", num1 + num2)
print(num1, "-", num2, "=", num1 - num2)
print(num1, "*", num2, "=", num1 * num2)
print(num1, "/", num2, "=", num1 / num2)

print("-------------------------")

result1 = num1 + num2
result2 = num1 - num2
result3 = num1 * num2
result4 = num1 / num2

print(num1, "+", num2, "=", result1)
print(num1, "-", num2, "=", result2)
print(num1, "*", num2, "=", result3)
print(num1, "/", num2, "=", result4)

print("-------------------------")

print(f"{num1} + {num2} = {result1}")
print(f"{num1} - {num2} = {result2}")
print(f"{num1} * {num2} = {result3}")
print(f"{num1} / {num2} = {result4}")

print("-------------------------")

num3 = input("숫자를 입력하세요")  # 입력값 num3로 문자로 받기
num3 = int(num3)  # num3 값을 자연수로 변경
num4 = 300 # num3 = int(input()) => 로 요약 가능
print(num3, "+", num4, "=", num3 + num4)
