t=int(input())
for _ in range(t):
    n=int(input())
    team1=list(map(int,input().split()))
    team2=list(map(int,input().split()))

    team1.sort( reverse=True)
    team2.sort(reverse=True)
    temp = 0
    count=0
    for i in team1:

        for j in range(temp,n):

            if i>team2[j]:
                count+=1
                temp=j+1
                break

    print(count)