twoDmatrix=[[10,20,30],
            [40,50,60],
            [70,80,90]]
transpose=[[i[j] for i in twoDmatrix] for j in range(len(twoDmatrix[0]))]
print(transpose)