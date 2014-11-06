__author__ = 'muyuan.lxr'

tmp = '''zxcvzxcv
zxcvzxcv );
xzcvzxcv
var wanInfoArr = new Array(
    "1",
    "123.1.123.2",
    "255.255.255.0",
    "123.1.123.1"
);
zxcvzxcv
zxcvzxcv
zcxvzxcv'''

keyword = "var wanInfoArr = new Array("

def ectract(html_content):
    start_index = html_content.index(keyword) + len(keyword)
    end_index = html_content.index(");", start_index)
    content = html_content[start_index: end_index]
    content = content.replace('\n','').replace('"','')
    contents = content.split(",")
    ip = contents[1].strip()
    return ip
