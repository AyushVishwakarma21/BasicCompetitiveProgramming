n =  int(input())
marks = list(map(int,input().split()))
passed = 0
failed =0
if len(marks)!=n:
    print("404")
else:
    for i in marks:
        if i>=35:
            passed = passed+1
        else:
            failed = failed+1

    print(passed,failed)