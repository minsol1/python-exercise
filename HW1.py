#shirt 

# #2
# i=0
# sum=0
# while(i<100):
#     i+=1
#     if(i%4==0):
#         sum+=i
# print(sum)

# #3
# sum=0
# for i in range(1,101):
#     if(i%5==0):
#         sum+=i
# print(sum)

# #4
# py_score = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
# sum=0
# n=0
# for i in py_score:
#     if(i>=60):
#         sum+=i
#         n+=1
# avg=sum/n
# print(avg)

# #5
# for j in range(2,10):
#     for i in range(1,10):
#     	print(j, "*", i, '=', j*i) 


#6

def wordcount(sentence):
    wordlist=sentence.split()
    wordcnt={}
    for word in wordlist:
        wordcnt[word]=wordcnt.get(word,0)+1
    keys = sorted(wordcnt.keys())
    for word in keys:
        print(word + '=' + str(wordcnt[word]))
    

sentence = '다들 파이썬은 어떠신가요 파이썬은 나중에 다른 곳에서도 많이 쓰인답니다 파이썬은 다른 언어보다 코딩 하기 쉬워요 멋사 멋사 화이팅'
wordcount(sentence)