text = "X-DSPAM-Confidence:    0.8475"
flt_start = text.find('0')
print float(text[flt_start:])