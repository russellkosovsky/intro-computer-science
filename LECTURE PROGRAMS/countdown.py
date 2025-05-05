def countdown(n):
    print(n)
    if n == 0:
        print("end of chapter")
    else:
        countdown(n-1)

countdown(20)
