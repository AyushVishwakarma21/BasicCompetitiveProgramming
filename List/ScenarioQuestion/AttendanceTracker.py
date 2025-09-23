n = int(input())
attends= list(map(int,input().split()))
# 1 matlab present 0 mane absent
longest_streak = 0
absentees_streak = 0

for x in attends:
    if x==0:
        absentees_streak = absentees_streak+1
        if absentees_streak>longest_streak:
            longest_streak=absentees_streak
    else:
        absentees_streak=0

print(longest_streak)