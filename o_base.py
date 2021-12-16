import tkinter as Tr
from basex import BaseX,BASE64_ALPH,BASE32_ALPH,BTC_ALPH
from tkinter.ttk import Combobox,Radiobutton
from tkinter import filedialog
import base64 as Base64
ch_file=""
codes=('auto','ascii', 'big5',
 'big5hkscs',
 'cp037',
 'cp273',
 'cp424',
 'cp437',
 'cp500',
 'cp720',
 'cp737',
 'cp775',
 'cp850',
 'cp852',
 'cp855',
 'cp856',
 'cp857',
 'cp858',
 'cp860',
 'cp861',
 'cp862',
 'cp863',
 'cp864',
 'cp865',
 'cp866',
 'cp869',
 'cp874',
 'cp875',
 'cp932',
 'cp949',
 'cp950',
 'cp1006',
 'cp1026',
 'cp1125',
 'cp1140',
 'cp1250',
 'cp1251',
 'cp1252',
 'cp1253',
 'cp1254',
 'cp1255',
 'cp1256',
 'cp1257',
 'cp1258',
 'cp65001',
 'euc_jp',
 'euc_jis_2004',
 'euc_jisx0213',
 'euc_kr',
 'gb2312',
 'gbk',
 'gb18030',
 'hz',
 'iso2022_jp',
 'iso2022_jp_1',
 'iso2022_jp_2',
 'iso2022_jp_2004',
 'iso2022_jp_3',
 'iso2022_jp_ext',
 'iso2022_kr',
 'latin_1',
 'iso8859_2',
 'iso8859_3',
 'iso8859_4',
 'iso8859_5',
 'iso8859_6',
 'iso8859_7',
 'iso8859_8',
 'iso8859_9',
 'iso8859_10',
 'iso8859_11',
 'iso8859_13',
 'iso8859_14',
 'iso8859_15',
 'iso8859_16',
 'johab',
 'koi8_r',
 'koi8_t',
 'koi8_u',
 'kz1048',
 'mac_cyrillic',
 'mac_greek',
 'mac_iceland',
 'mac_latin2',
 'mac_roman',
 'mac_turkish',
 'ptcp154',
 'shift_jis',
 'shift_jis_2004',
 'shift_jisx0213',
 'utf_32',
 'utf_32_be',
 'utf_32_le',
 'utf_16',
 'utf_16_be',
 'utf_16_le',
 'utf_7',
 'utf_8',
 'utf_8_sig')

def click(event):
    txt2.delete(0, Tr.END)
    if selected.get()==0:
        txt2.insert(Tr.END,B_X(txt.get(),combo.get()).encode())
    elif selected.get()==1:
        txt2.insert(Tr.END,B_X(txt.get(),combo.get()).decode())
def openf(event):
    global ch_file
    file = filedialog.askopenfilename()
    ch_file=file
def fmodify(event):
    name=ch_file[ch_file.rfind("/")+1:]
    file=open(ch_file,'rb')
    btss=file.read()
    file.close()
    encoding=combo.get()
    if encoding=='auto':
            numb=max(tuple(map(ord,name)))
            if numb>4096:
                encoding='utf-16'
            elif numb>127:
                encoding='utf-8'
    if selected.get()==0:
        newname=BaseX.encode(BASE64_ALPH,bytes(name,encoding))
        newbtss=bytes(BaseX.encode(BASE64_ALPH,btss),encoding)
    elif selected.get()==1:
        newname=bytes(BaseX.decode(BASE64_ALPH,name,encoding))
        print(newname)
        newbtss=BaseX.decode(BASE64_ALPH,btss.decode(encoding),encoding)
    file=open(newname,'wb')
    file.write(bytes(newbtss))
    file.close()
#[x for x in dir(st) if '__' not in x] исключаем все элементы из списка со значением __
window=Tr.Tk()
window.title('Программа для кодирования файлов')
window.geometry('240x120')
lblr = Tr.Label(window, text="Кодировка:")  
lblr.grid(column=1, row=0)
combo = Combobox(window)  
combo['values'] = codes  
combo.current(0)  # установите вариант по умолчанию  
combo.grid(column=1, row=1)
selected = Tr.IntVar()
rad1 = Radiobutton(window, text='Кодирование',width=20, value=0, variable=selected)
rad1.grid(column=1,row=2)
rad1 = Radiobutton(window, text='Декодирование',width=20, value=1,variable=selected)
rad1.grid(column=1,row=3)
btn2 = Tr.Button(window, text="Открыть файл", height=7)
btn2.bind("<Button-1>", openf)
btn2.grid(column=0,row=0, rowspan=6)
btn3 = Tr.Button(window, text="Обработать файл")
btn3.bind("<Button-1>", fmodify)
btn3.grid(column=1,row=5)
window.mainloop()
