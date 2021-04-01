# #1
# def is_odd(num):
#     if(num%2==0):
#         print("%d은 짝수입니다. "%num)
#     else:
#         print("%d은 홀수입니다. "% num)

# num=int(input("자연수를 입력하시오"))
# is_odd(num)

#2
num_list = [1, 3, 5, 7, 9]

def average(nums_list):
    sum=0.0
    for num in nums_list:
        sum+=num
    return sum / len(num_list)

print(average(num_list))
