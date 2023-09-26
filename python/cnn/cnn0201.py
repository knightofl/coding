import re


s = '/usr/local/bin/python'
print(s.split('/')[1:])
print(s.rsplit('/', 1))



s = """
<html>
    <body style='background-color:#ffff'>
        <h4>Click</h4>
        <a href='http://www.python.org'>Here</a>
        <p>
        	To connect to the most powerful tools in the world.
        </p>
    </body>
</html>"""

# print(re.sub('<.+?>', '', s))
while True:
    index_begin = s.find('<')
    if index_begin == -1:
        break
    
    index_end = s.find('>')
    if index_end != -1:
        s = s[:index_begin] + s[index_end+1:]

print(s)



s = """We encourage everyone to contribute to Python.
If you still have questions after reviewing the material in this guide,
then the Python Mentors group is available to help guide new contributors
through the process."""

s = re.split('[., \n]', s.upper())
print(s)
s = set(s)
print(s)
s.remove('')
print(s)
s = list(s)
s.sort()
print(s)

for i in s:
    print(i)



for i in range(100):
    a, b = divmod(i, 10)
    
    if (a and a%3==0) and (b and b%3==0):
        print(i, '짝짝')
        continue
    if (a and a%3==0) or (b and b%3==0):
        print(i, '짝')
        
      

def sum(*inja):
    sum = 0
    for i in inja:
        sum += i
    return sum

print(sum(2,3,4))