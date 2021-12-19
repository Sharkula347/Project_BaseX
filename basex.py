import math,warnings
'''
Project_BASEX
Developed by Kazaryan Maxim, Russia, Rostov-na-Donu, DSTU, VKB43
'''

ALPHS={
"BASE16":"0123456789ABCDEF",
"BASE32":"ABCDEFGHIJKLMNOPQRSTUVWXYZ234567",
"BASE58(BTC)":'123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz',
"BASE58(RIPPLE)":'rpshnaf39wBUDNEGHJKLM4PQRST7VWXYZ2bcdeCg65jkm8oFqi1tuvAxyz',
"BASE64":"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/",
"BASE85":"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%&()*+-;<=>?@^_`{|}~"
}

class BaseX(object):
    '''Кодирование Base'''
    def __init__(self):
        pass

    def encode(kb,text_l):
        '''Кодировать'''

        def symbc(x,op=8):
            t=''
            if len(x)%op!=0:
                for i in range(op-len(x)%op):
                    t=t+'0'
            return t+x
        
        if len(kb)!=2**math.ceil(math.log2(len(kb))): #Для алфавита длиной не 2^n
            op=math.ceil(math.log2(max(text_l)))#Число бит на символ в исходном тексте
            text_l=[symbc(bin(i)[2:]) for i in text_l]
            text_o="".join(text_l)
            to_num=int('0b'+text_o,2)
            newpos=''
            while to_num>0:
                e=divmod(to_num,len(kb))
                ost=e[1]
                to_num=e[0]
                newpos=newpos+kb[ost]
            newpos=newpos[::-1]
        else:                                   #Для алфавитов мощностью 2^n
            kp=math.ceil(math.log2(len(kb)))    #Число бит на символ в алгоритме
            text_o="".join([symbc(bin(i)[2:]) for i in text_l])
            l_text=len(text_o)
            len_t=l_text
            while ((l_text)%kp)!=0:
                text_o +='00000000'
                l_text+=8
            newpos=[]
            text_o=list(map(int,[i for i in text_o]))
            text_o=[text_o[i]*2**(kp-i%kp-1) for i in range(len(text_o))]
            text_o=[sum(text_o[i*kp:i*kp+kp]) for i in range(len(text_o)//kp)]
            is_zero_byte=1 #Флаг работы с добавленными нулевыми битами
            lpos=-1
            cnt_bytes=[]
            while is_zero_byte:
                if (text_o[lpos-1]!=0) and (text_o[lpos]==0) or (text_o[lpos]!=0):
                    is_zero_byte=0
                else:
                    text_o.pop()
                    cnt_bytes.append("=")
            newpos=[kb[i] for i in text_o]
            newpos.extend(cnt_bytes)
            newpos="".join(newpos)
        return newpos

    def decode(kb,text,code='UTF-8'):
        '''Декодировать'''
        for i in text:
            if (i not in kb) and (i!='='):
                warnings.warn('Обнаружено несоответствие закодированного текста и алфавита кодировки. Операция будет отменена!', category=BytesWarning, stacklevel=1, source=None)
                exit()
        if len(kb)!=2**math.ceil(math.log2(len(kb))): #Для алфавитов мощностью не 2^n
            to_num=0
            for i in text:
                ost=kb.index(i)
                to_num=to_num*len(kb)+ost
            newpos=[]
            while to_num>0:
                e=divmod(to_num,256)
                ost=e[1]
                to_num=e[0]
                newpos.append(ost)
            newpos=newpos[::-1]
        else:               #Для алфавитов мощностью 2^n
            kp=math.ceil(math.log2(len(kb)))
            tmp=["".join(['0' for u in range(kp-len(bin(kb.index(i))[2:]))])+bin(kb.index(i))[2:] if i!='=' else "".join(['0' for e in range(kp)]) for i in text]
            tmp="".join(tmp)
            l_tmp=len(tmp)
            while '1' not in tmp[l_tmp-8:l_tmp]:
                tmp=tmp[:l_tmp-8]
                l_tmp -=8
            debuger=[tmp[i*8:i*8+8] for i in range(l_tmp//8)]
            newpos=[int('0b'+tmp[i*8:i*8+8],2) for i in range(l_tmp//8)]
        return newpos
