import math,warnings
'''
Project_BASEX
Developed by Kazaryan Maxim, Russia, Rostov-na-Donu, DSTU, VKB43
'''

ALPHS={
"BTC":'123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz',
"RIPPLE":'rpshnaf39wBUDNEGHJKLM4PQRST7VWXYZ2bcdeCg65jkm8oFqi1tuvAxyz',
"BASE32":"abcdefghijklmnopqrstuvwxyz234567",
"BASE64":"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
}

class BaseX(object):
    '''Кодирование Base'''
    def __init__(self):
        pass

    def encode(kb,text_l):
        '''Кодировать'''
        global deb
        deb=''
        def symbc(x,op=8):
            t=''
            if len(x)%op!=0:
                for i in range(op-len(x)%op):
                    t=t+'0'
            return t+x
        if len(kb)!=2**math.ceil(math.log2(len(kb))): #Для алфавита длиной не 2^n
            #text_l=bytes(text,code)
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
            #print(kp,"--")
            #text_l=bytes(text,code)
            text_o="".join([symbc(bin(i)[2:]) for i in text_l])
            l_text=len(text_o)
            len_t=l_text
            while ((l_text)%kp)!=0:
                text_o +='00000000'
                l_text+=8
            newpos=[]
            print(text_o)
            text_o=int('0b'+text_o,2)
            cel_ch=text_o
            is_zero_byte=1 #Флаг работы с добавленными нулевыми битами
            while cel_ch!=0:
                cel_ch,ost=divmod(cel_ch,2**kp)
                if ost==0 and is_zero_byte:
                    newpos.append("=")
                elif ost!=0:
                    is_zero_byte=0
                    newpos.append(kb[ost])
            newpos=newpos[::-1]
            '''
            while len(text_o)>0:
                if len(text_o)>kp:
                    ekp=kp
                else:
                    ekp=len(text_o)
                ost=text_o[:ekp]
                #print(symbc(ost))
                print('progress',int((1-len(text_o)/len_t)*100),'%')
                index_a=int('0b'+ost,2)
                if index_a!=0:
                    newpos.append(kb[index_a])
                else:
                    newpos.append('=')
                text_o=text_o[ekp:]
            '''
            newpos="".join(newpos)
        return newpos

    def decode(kb,text,code='UTF-8'):
        '''Раскодировать'''
        #kb=[i for i in bytes(kb,code)]
        #text=[i for i in bytes(text,code)]
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
            #print(kp)
            tmp=["".join(['0' for u in range(kp-len(bin(kb.index(i))[2:]))])+bin(kb.index(i))[2:] if i!='=' else "".join(['0' for e in range(kp)]) for i in text]
            tmp="".join(tmp)
            l_tmp=len(tmp)
            while '1' not in tmp[l_tmp-8:l_tmp]:
                tmp=tmp[:l_tmp-8]
                l_tmp -=8
            debuger=[tmp[i*8:i*8+8] for i in range(l_tmp//8)]
            newpos=[int('0b'+tmp[i*8:i*8+8],2) for i in range(l_tmp//8)]
        return newpos
