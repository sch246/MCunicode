import os,json

height = input('输入高度,否则为8')
if not height:
    height = '8'
print('高度设为',height)
ascent = input('输入偏移,否则为7')
if not ascent:
    ascent = '7'
print('偏移设为', ascent)
rootpath = input(r'输入要遍历的\minecraft\textures\font文件夹路径,否则选定textures\font'+'\n')
if not rootpath:
    rootpath = r'textures\font'
print('遍历路径设为', rootpath)
savepath = input(r'输入要保存json的文件夹路径,否则选定default.json'+'\n')
if not savepath:
    savepath = r'default.json'
print('保存路径设为', savepath)
# f1 = open(r'assets\minecraft\font\default.json',encoding='utf-8')
# fv = json.loads(f1.read())
# f1.close()

fv = json.loads('{"providers": []}')
def add_unicode(hx):
    fv['providers'].append({
        "type": "bitmap",
        "file": f"minecraft:font/unicode_page_{hx}.png",
        "height": height,
        "ascent": ascent,
        "chars": []})
    for line in range(0, 16):
        fv['providers'][-1]['chars'].append('')
        for ihx in range(0, 16):
            fv['providers'][-1]['chars'][-1] += r'\u%s%x%x' % (hx, line, ihx)

l0=[]
for root, dirs, files in os.walk(rootpath):
    for name in files:
        if name[0:13] == 'unicode_page_':
            l0.append(name[13:15])
            # print(name)
# l1=[]
def Hx(i):
    if i<16:
        return "0%x" % (i)
    else:
        return "%x" % (i)

for i in range(0,256):
    hx=Hx(i)
    if hx in l0:
        # l1.append(hx)
        add_unicode(hx)

ft = json.dumps(fv,indent=4)
# print(ft.find('\\\\'))
ft = ft.replace('\\\\', '\\')
# print(ft.find('\\\\'))

f2 = open(savepath,'w+', encoding='utf-8')
f2.write(ft)
f2.close()
