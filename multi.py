print("hello python")

# 100 미만 정수를 차례대로 i에 입력하기
for i in range(100):
    if i % 7 ==0:
        print(i)



# round() 함수 사용법
 round((50+45+33+39+29+30) / 6 , 1) 
       

# for 문과 리스트로 2단 출력하기
number = [1,2,3,4,5,6,7,8,9]
for item in number:
    print(2*item)


# range() 함수 사용법
for item in range(10):
    print(item)

#  2부터 20 미만의 정수를 가져오기
 for item in range(2,20):
     print(item)   

# 19단 곱셈표 
 for item in range(2,20):
     for each in range(2,20):
         print(item, 'X' , each, '=', item * each)    

# 문자열 포매팅으로 print()함수 사용
for item in range(2,20):
    for each in range(2,20):
        print('%d X %d = %d' %(item,each,item * each))         