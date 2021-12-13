import os,json

mu = input('输入倍率,否则为2\n')
if not mu:
    mu = '2'
mu = int(mu)
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
        if name[0:13] == 'unicode_page_':
            l0.append(name[13:15])

for i in range(0,256):
    hx=Hx(i)
    if hx in l0:
        add_unicode(hx)

def newsize(mu,fv):
    for part in fv['providers']:
        if part['height']!=12:
            part['height'] = 8*mu
        if part['ascent'] != 10:
            part['ascent'] = 7*mu

    ft = json.dumps(fv,indent=4)
    ft = ft.replace('utemp', '\\u')
    ft = ft.replace('\\\\u', '\\u')

    f2 = open(f'assets\\size\\font\\{mu}x.json', 'w+', encoding='utf-8')
    f2.write(ft)
    f2.close()

newsize(mu,fv)
# for mu in range(1,33):
#     newsize(mu,fv)
