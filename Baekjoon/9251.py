seq1=input()
seq2=input()

dp = [[0]*(len(seq1)) for _ in range(len(seq2))]

for i in range(len(dp)):        # i means row length seq2
    for j in range(len(dp[i])): # j means col length seq1
        if i >= 1 and j >= 1:
            if seq1[j]==seq2[i]:
                dp[i][j] = (dp[i-1][j-1]+1) 
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        elif i==0 and j==0:
            if seq2[i]==seq1[j]:
                dp[i][j] = 1
        elif i == 0:
            if seq2[i]==seq1[j]:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i][j-1]
        elif j == 0:
            if seq1[j]==seq2[i]:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j]

print(dp[len(seq2)-1][len(seq1)-1])