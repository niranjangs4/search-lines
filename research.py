import re
START = "some"
END = "Hello"
test = "this is some\nsample .-text\nthat has the\nwords Hello World\n"
m = re.compile(r'%s.*?%s' % (START,END),re.S)
print m.search(test).group(0)
