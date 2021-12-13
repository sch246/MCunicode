import os,json

is_plus = 'font'
while 1:
    s=input('是否载入高度为256的图片,这可能需要设置更特殊的高度和偏移\n(y/n),直接enter默认为n\n')
    if not s or s=='n': 
        break
    if s == 'y':
        is_plus = 'font_plus'
        break
    print('请输入y或者n,要么直接enter')

height = input('输入高度,否则为8\n')
if not height:
    height = '8'
ascent = input('输入偏移,否则为7\n')
if not ascent:
    ascent = '7'
name0 = input(f'输入文件名,否则为{height}_{ascent}\n')
if not name0:
    name0 = height+'_'+ascent
height = int(height)
ascent = int(ascent)
f1 = open(r'1x.json',encoding='utf-8')
ft = f1.read()
ft = eval(repr(ft).replace('\\\\u','utemp'))
fv = json.loads(ft)
for k in list(range(len(fv['providers'])))[::-1]:
    if 'unicode_page_' in fv['providers'][k]['file']:
        del fv['providers'][k]
f1.close()

# fv = json.loads('{"providers": []}')
def add_unicode(hx):
    fv['providers'].append({
        "type": "bitmap",
        "file": f"minecraft:font/unicode_page_{hx}.png",
        "height": 8,
        "ascent": 7,
        "chars": []})
    for line in range(0, 16):
        fv['providers'][-1]['chars'].append('')
        for ihx in range(0, 16):
            fv['providers'][-1]['chars'][-1] += r'\u%s%x%x' % (hx, line, ihx)


def Hx(i):
    if i < 16:
        return "0%x" % (i)
    else:
        return "%x" % (i)


l0=[]
for root, dirs, files in os.walk(r'textures\font'):
    for name in files:
        if name[:13] == 'unicode_page_':
            l0.append(name[13:15])

for i in range(0,256):
    hx=Hx(i)
    if hx in l0:
        add_unicode(hx)

def newsize(fv,name,height,ascent):
    for part in fv['providers']:
        if part['height']!=12:
            part['height'] = height
        if part['ascent'] != 10:
            part['ascent'] = ascent
        if is_plus=='font_plus':
            part['file']=part['file'].replace('font', 'font_plus')
    ft = json.dumps(fv,indent=4)
    ft = ft.replace('utemp', '\\u')
    ft = ft.replace('\\\\u', '\\u')

    f2 = open(f'assets\\size\\font\\{name}.json', 'w+', encoding='utf-8')
    f2.write(ft)
    f2.close()

newsize(fv,name0,height,ascent)
