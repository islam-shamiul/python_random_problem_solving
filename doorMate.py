n,m = map(int,input().split(' '))

s = ".|."
text = "welcome"
size = int(n/2)
for i in range (0, int(n/2)):
    print((s*(2*i+1)).center(m,"-"))

print(text.center(m,"-"))

for i in range (int(n//2)-1,-1,-1):
    print((s*(2*i+1)).center(m,"-"))
