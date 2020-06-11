import urllib.request
count=dict()
fhand=urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
  print(line.decode().strip())
  word=line.decode().split()
  for v in word:
    count[v]= count.get(v,0)+1
print(count)
