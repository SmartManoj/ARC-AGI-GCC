def p(j):A=sum(j,[]);c=max(A,key=A.count);E=c or max(A,key=lambda k:A.count(k)if k else-1);return[[E,E],[E,E]]
