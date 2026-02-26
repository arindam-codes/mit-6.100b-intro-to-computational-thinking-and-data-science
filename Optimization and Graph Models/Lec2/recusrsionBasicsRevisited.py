# import time

# def countdown(n):
#     if n == 0:
#         print("Blastoff!")
#     else:
#         print(n)
#         time.sleep(1)
#         countdown(n - 1)
#         print("calling countdown function at n = ", n)
#     return 2
# print(countdown(3))

def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)
recurse(3, 0)
