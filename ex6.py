text = "X-DSPAM-Confidence:    0.8475"
proc= text.find('0')
print(proc)
nr=text[proc+1:]
print(float(nr))
