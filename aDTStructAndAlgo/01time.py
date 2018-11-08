import time
start_time = time.time()

# for a in range(1001):
#     for b in range(1001):
#         for c in range(1001):
#             if 1000 == a+b+c and a**2+b**2==c**2:
#                 print("a,b,c:%d,%d,%d"%(a,b,c))
# #  [Finished in 84.2s]

# for a in range(1001):
#     for b in range(1001):
#         c = 1000 -a-b
#         if 1000 == a+b+c and a**2+b**2==c**2:
#             print("a,b,c:%d,%d,%d"%(a,b,c))               
#  [Finished in 0.4s]

for a in range(1001):
    for b in range(1001-a):
        c = 1000 -a-b
        if a**2+b**2==c**2:
            print("a,b,c:%d,%d,%d"%(a,b,c)) 

#  [Finished in 0.1s]

end_time = time.time()
cost = (end_time-start_time)
print(cost)
