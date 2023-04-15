lambda s1,s2:(l1:=len(s1),l2:=len(s2),print(len([1for i in range(min(l1,l2))if s1[i]!=s2[i]])+abs(l1-l2)))
