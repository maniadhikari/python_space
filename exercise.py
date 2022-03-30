hrs = input("Enter hours: ")
rate = input("Enter rate: ")
hr = float(hrs)
ra = float(rate)
if hr > 40:
    pa = hr * ra
    ext = (hr - 40) * (ra * 0.5)
    ov = pa + ext
else:
    ov = hr * ra
    print(ov)
print(ov)





