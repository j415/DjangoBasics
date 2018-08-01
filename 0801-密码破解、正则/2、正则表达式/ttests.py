import re



str = '<p>zheshiyiduanzppppifuchuang</p>'

#
# print(re.search(r'([^</p>])', str))

def test(str):
    pat = r'<p>.*?</p>'
    res = re.findall(pat, str)
    print(res)


print(test(str))