# 문제
# 알파벳 소문자, 대문자, 숫자 0-9중 하나가 주어졌을 때, 주어진 글자의 아스키 코드값을 출력하는 프로그램을 작성하시오.

# 입력
# 알파벳 소문자, 대문자, 숫자 0-9 중 하나가 첫째 줄에 주어진다.

# 출력
# 입력으로 주어진 글자의 아스키 코드 값을 출력한다.

#구글링으로 찾았던 내 풀이
# word = input()

# print(ascii(word))

#이건 잘 안되는것 같음

# Python program to print 
# ASCII Value of Character
  
# In c we can assign different
# characters of which we want ASCII value 
  
word =input()
# print the ASCII value of assigned character in c
print("The ASCII value of '" + word + "' is", ord(word))

#ord함수가 쓰인다는건데, ord함수는 매개변수로 입력된 변수를 unicode로 바꾸어준다.