import tkinter as Tr
from basex import BaseX,ALPHS
from tkinter.ttk import Combobox,Radiobutton
from tkinter import filedialog

ch_file=""
codes=(
 'auto',
 'ascii',
 'big5',
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
        newname=BaseX.encode(CURRALPH(),bytes(name,encoding))
        newbtss=bytes(BaseX.encode(CURRALPH(),btss),encoding)
    elif selected.get()==1:
        newname=bytes(BaseX.decode(CURRALPH(),name,encoding)).decode(encoding)
        print(newname)
        newbtss=BaseX.decode(CURRALPH(),btss.decode(encoding),encoding)
    file=open(newname,'wb')
    file.write(bytes(newbtss))
    file.close()

def radio_swithced(event,nm):
    print(nm)
    if nm:
        txt['state'] = 'normal'
        combo2['state'] = 'disabled'
    else:
        combo2['state'] = 'normal'
        txt['state'] = 'disabled'

def CURRALPH():
    print(combo2.get())
    print(combo2['state'])
    if combo2['state'] == 'normal':
        return ALPHS[combo2.get()]
    if txt['state'] == 'normal':
        return txt.get()

window=Tr.Tk()
window.title('Программа для кодирования файлов')
window.geometry('320x240')

lblr = Tr.Label(window, text="Кодировка:")  
lblr.grid(column=1, row=0, columnspan=2)

combo = Combobox(window)  
combo['values'] = codes  
combo.current(0)  # вариант по умолчанию 
combo.grid(column=1, row=1, padx=10, columnspan=2)

selected = Tr.IntVar()

selected_a = Tr.IntVar()

rad1 = Radiobutton(window, text='Кодирование',width=20, value=0, variable=selected)
rad1.grid(column=2,row=2)
rad1 = Radiobutton(window, text='Декодирование',width=20, value=1,variable=selected)
rad1.grid(column=2,row=3)

btn2 = Tr.Button(window, text="Открыть файл", height=7,width=20)
btn2.bind("<Button-1>", openf)
btn2.grid(column=0,row=0, rowspan=6,pady=2,padx=2)

btn3 = Tr.Button(window, text="Обработать файл")
btn3.bind("<Button-1>", fmodify)
btn3.grid(column=1,row=5, columnspan=2)

lblr = Tr.Label(window, text="Алфавит:")  
lblr.grid(column=0, row=6, columnspan=3)

alph=list(ALPHS.keys())

combo2 = Combobox(window, width=20)  
combo2['values'] = alph  
combo2.current(0)  # вариант по умолчанию 
combo2.grid(column=0, row=7, columnspan=2)

rad2_0 = Radiobutton(window, text='Стандартный',width=20, value=0, variable=selected_a)
rad2_0.grid(column=2,row=7)
rad2_0.bind('<Button-1>',lambda x:radio_swithced(x,0))

rad2_1 = Radiobutton(window, text='Свой',width=20, value=1,variable=selected_a)
rad2_1.grid(column=2,row=8)
rad2_1.bind('<Button-1>',lambda x:radio_swithced(x,1))

txt = Tr.Entry(window,width=23)  
txt.grid(column=0, row=8, columnspan=2)
txt['state'] = 'disabled'

window.mainloop()
