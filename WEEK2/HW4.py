a = "ABCDCBA"
b = len(a)
c = True

if b % 2 == 0:
    print("Polindrome degildir")
else:
    ort = round(b/2)
    for i in range (0,ort):
        if a[i] == a[0-(i+1)]:
            print("Polindrome değildir")
            c = False
            break
        print("Polindrome dir")