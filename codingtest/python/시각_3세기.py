'''
00시 00분 00초 ~ N시 59분 59초 까지
3이 하나라도 포함되어 있으면 세기
'''
# my
n = int(input())

cnt = 0

hour = range(n+1)
min = range(60)
sec = range(60)
            
for h in hour:
    h_str = str(h)
    for m in min:
        m_str = str(m)
        for s in sec:
            s_str = str(s)

            if '3' in h_str or '3' in m_str or '3' in s_str:
                cnt += 1

print(cnt)


# solution
'''
n = int(input())

cnt = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                cnt += 1
'''
