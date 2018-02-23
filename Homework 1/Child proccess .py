import os

print("pid before forking")
print(os.getpid())

newpid = os.fork()
if newpid == 0:
    print("first forking succesfull")
    print("I am the child one !!!")
    print(os.uname())
    print("killed 1st chilled")
print(newpid)

newpid2 = os.fork()
print("making second child.")
if newpid2 == 0:
    print("second forking succesfull")
    print("I am the second child.")
    print(newpid2)
    print("killed 2nd child")
