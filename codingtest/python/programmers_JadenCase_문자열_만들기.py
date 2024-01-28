def solution(s):
    
    s = s.split(' ')
    
    # s2 = [word[0].upper() + word[1:].lower() for word in s] 런타임에러
    s2 = [word.capitalize() for word in s]
    return ' '.join(s2)
        
    

s = "3people unFollowed me"
print(solution(s)) # "3people Unfollowed Me"