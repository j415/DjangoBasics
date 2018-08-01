import re



str = '<p>wohenkaixin</p>'
pat = r'<p>.*</p>'

print(re.search(pat, str))





re_test = re.compile(pat)
print(re_test.search())



