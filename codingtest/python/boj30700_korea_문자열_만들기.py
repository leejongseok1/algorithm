'''
입력 : k, o, r, e, a 무작위 순서 ex)KEKRORKAKROEKREORKA - 5
사이 문자들을 지워서 만들 수 있는 가장 긴 korea 수
kor 만들 수 있으면 3 korea 5
ko 2 rea 0 (k없음)
'''

s = input()
#KEKRORKAKROEKREORKA

korea = 'KOREA'

cnt = 0

for i in s:
    if i == korea[cnt % 5]:
        cnt += 1

print(cnt)
    


    
