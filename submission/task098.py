def p(g):C,D=len(g),len(g[0]);return[[g[A][B]if g[A][B]and any(A<0 or A>=C or B<0 or B>=D or g[A][B]==0 for(A,B)in[(A-1,B),(A+1,B),(A,B-1),(A,B+1)])else 0 for B in range(D)]for A in range(C)]
