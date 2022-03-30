def computepay(hours, rate):
    if hours > 40:
        ns = hs * rs
        es = (hs - 40) * (rs * 0.5)
        pay = ns + es
    else:
        pay = hs * rs
    return pay
        
hours = input("Enter hours:")
rate = input("Enter rate:")
hs = float(hours)
rs = float(rate)
ep = computepay(hs, rs)
print(ep)
