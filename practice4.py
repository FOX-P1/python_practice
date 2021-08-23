def is_odd(number):
    if number % 2 == 1:
        return True
    else:
        return False

print(is_odd(3))


def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result / len(args)

print(avg_numbers(1, 2))
print(avg_numbers(1,2,3,4,5))


input1 = input("첫번째 숫자를 입력하세요:")
input2 = input("두번째 숫자를 입력하세요:")

total = int(input1) + int(input2)
print("두 수의 합은 %s 입니다" % total)


print(3)


f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("test.txt", 'r')
print(f2.read())


user_input = input("저장할 내용을 입력하세요:")
f3 = open('test1.txt', 'a' )
f3.write(user_input)
f3.write('\n')
f3.close()


f4 = open('test2.txt', 'r')
body = f4.read()
f4.close()

body = body.replace("java", "python")

f4 = open('test2.txt', 'w' )
f4.write(body) 
f4.close()