l = []
n = int(input("Enter a number of elements to be inserted: "))
print("Enter ",n," elements :")
for i in range(n):
    l.append(int(input()))
l.sort()
print("The sorted list is:",l)
s = int(input("Enter a number to be searched for : "))

low = 0
high = len(l)-1
mid = 0
while low <= high:
    mid = (low+high)//2
    if l[mid] == s:
        print(s," is found at position",mid+1)
        break
    elif l[mid] > s:
        high = mid - 1
    else:
        low = mid + 1
else:
    print(s," is not found")
