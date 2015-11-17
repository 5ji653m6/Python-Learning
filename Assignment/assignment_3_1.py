hrs = raw_input("Enter Hours:")
h = float(hrs)
if h > 40:
    re = float(h-40)
    h_new = h - re
rt = raw_input("Enter Rate:")
r = float(rt)
rph = h_new * r +  re *r* 1.5
print rph