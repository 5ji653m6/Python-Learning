def computepay(h,r):
    h = raw_input("Enter hours:")
    r = raw_input("Enter rate:")
    if float(h) > 40:
        hr_extra = float(h) - 40
        hr_re = float(h) - hr_extra
    else:
        hr_re = h
    pph = 10.50*(hr_re + hr_extra*1.5)
    return pph
p = computepay(raw_input, raw_input)
print p
