import bitcoin
import hashlib
from tkinter import *

# Generate a random private key as a root seed********************************************************
try:
    backup = open('backup','r',encoding='utf-8')
    (prompt_mess,private_key_seed) = backup.readline().split('：')
    private_key_seed = private_key_seed.strip()
    print ("你的随机种子（删除此备份文件后将会重新生成新数据）： ", private_key_seed)
    backup.close()
except:
    print('哎呦欸！！当前目录的备份文件出现了奇怪的问题！！现已生成了新钱包 :)')
    valid_private_key_seed = False
    while not valid_private_key_seed:
        private_key_seed = bitcoin.random_key()
        decoded_private_key_seed = bitcoin.decode_privkey(private_key_seed, 'hex')
        valid_private_key_seed =  0 < decoded_private_key_seed < bitcoin.N
    print ("你的随机种子（删除此备份文件后将会重新生成新数据）： ", private_key_seed)
    backup = open('backup','w',encoding='utf-8')
    print ("你的随机种子（删除此备份文件后将会重新生成新数据）： ", private_key_seed, file=backup)
    backup.close()

#定义一个列表，里面存放由种子生成的所有私钥
bitcoinwallet_LIST = []

# 由种子生成主私钥、主公钥、比特币地址
hash512_sequence = hashlib.sha512(private_key_seed.encode('utf-8')).hexdigest()
master_private_key = hash512_sequence[:64]
main_chain_code = hash512_sequence[64:]
master_public_key = bitcoin.encode_pubkey(bitcoin.fast_multiply(bitcoin.G,bitcoin.decode_privkey(master_private_key, 'hex')),'hex')
master_address = bitcoin.pubkey_to_address(master_public_key)
bitcoinwallet_LIST.append(master_private_key)
print ("主私钥（十六进制）：           ", master_private_key)
print ("主公钥（非压缩十六进制）：     ", master_public_key)
print ("相应比特币地址(b58check)：     ", master_address)

# 分层确定性钱包使用CKD（child key derivation）方程去从母密钥衍生出子密钥
# 生成10个子密钥
index_tuple = ('00000000','00000001','00000002','00000003','00000004',
               '00000005','00000006','00000007','00000008','00000009')
for i,index in enumerate(index_tuple):
    child_hash512_sequence = hashlib.sha512((master_public_key + main_chain_code + index).encode('utf-8')).hexdigest()
    child_private_key = child_hash512_sequence[:64]
    child_chain_code = child_hash512_sequence[64:]
    child_public_key = bitcoin.encode_pubkey(bitcoin.fast_multiply(bitcoin.G,bitcoin.decode_privkey(child_private_key, 'hex')),'hex')
    child_address = bitcoin.pubkey_to_address(child_public_key)
    bitcoinwallet_LIST.append(child_private_key)
    print ("索引%d子私钥（十六进制）：       %s" % (i,child_private_key))
    print ("索引%d子公钥（非压缩十六进制）： %s" % (i,child_public_key))
    print ("相应比特币地址(b58check)：     ", child_address)

#print(bitcoinwallet_LIST)
temp_key = bitcoinwallet_LIST[0]

#定义一个函数用来判断公钥Y坐标的奇偶性
def number_function():
    if (bitcoin.fast_multiply(bitcoin.G,bitcoin.decode_privkey(temp_key, 'hex'))[1] % 2) == 0:
        return '02' + bitcoin.encode(bitcoin.fast_multiply(bitcoin.G,bitcoin.decode_privkey(temp_key, 'hex'))[0], 16)
    return '03' + bitcoin.encode(bitcoin.fast_multiply(bitcoin.G,bitcoin.decode_privkey(temp_key, 'hex'))[0], 16)

#GUI
#图片+标题
top = Tk()
top.geometry('1000x680')
top.title('比特币钱包模型')
# photo = PhotoImage(file=r"C:\Users\A1718\下载\bitcoin.jpg")
# lab_top = Label(top,text='比特币钱包模型',image=photo,compound=LEFT,bg='yellow',pady=10,padx=10,relief=RIDGE,bd=8,font=('TkDefaultFont',45,'bold'))
# lab_top.pack(fill=X,padx=5,pady=5)
# separator = Frame(top,height=2,bd=1,relief=SUNKEN)
# separator.pack(fill=X,padx=5,pady=5)

#比特币地址内容
lab_addr = Label(top,text='比特币地址',bg="red", fg="white",relief=RIDGE,bd=4,font=('TkDefaultFont',12),pady=10)
lab_addr.pack(fill=X,padx=5,pady=5)

def pre_function():
    global temp_key
    i = bitcoinwallet_LIST.index(temp_key)
    i = (i-1) % len(bitcoinwallet_LIST)
    temp_key = bitcoinwallet_LIST[i]
    addr_ucomp.set(bitcoin.pubkey_to_address(bitcoin.encode_pubkey(bitcoin.fast_multiply(bitcoin.G,bitcoin.decode_privkey(temp_key, 'hex')),'hex')))
    addr_comp.set(bitcoin.pubkey_to_address(number_function().encode('utf-8')))
    priv_dec.set(bitcoin.decode_privkey(temp_key, 'hex'))
    priv_hex.set(temp_key)
    priv_WIF.set(bitcoin.encode_privkey(bitcoin.decode_privkey(temp_key, 'hex'), 'wif'))
    priv_hex_comp.set(entry_priv_hex.get()+'01')
    priv_WIF_comp.set(bitcoin.encode_privkey(bitcoin.decode_privkey(entry_priv_hex_comp.get(), 'hex'), 'wif'))
    pub_x.set(bitcoin.fast_multiply(bitcoin.G,bitcoin.decode_privkey(temp_key, 'hex'))[0])
    pub_y.set(bitcoin.fast_multiply(bitcoin.G,bitcoin.decode_privkey(temp_key, 'hex'))[1])
    pub_hex.set(bitcoin.encode_pubkey(bitcoin.fast_multiply(bitcoin.G,bitcoin.decode_privkey(temp_key, 'hex')),'hex'))
    pub_hex_comp.set(number_function())
    v.set("当前显示第%d个密钥信息，选中上面相应的比特币地址后Ctrl+V分享给你的小伙伴吧 :)" % (bitcoinwallet_LIST.index(temp_key)))

def nex_function():
    global temp_key
    i = bitcoinwallet_LIST.index(temp_key)
    i = (i+1) % len(bitcoinwallet_LIST)
    temp_key = bitcoinwallet_LIST[i]
    addr_ucomp.set(bitcoin.pubkey_to_address(bitcoin.encode_pubkey(bitcoin.fast_multiply(bitcoin.G,bitcoin.decode_privkey(temp_key, 'hex')),'hex')))
    addr_comp.set(bitcoin.pubkey_to_address(number_function().encode('utf-8')))
    priv_dec.set(bitcoin.decode_privkey(temp_key, 'hex'))
    priv_hex.set(temp_key)
    priv_WIF.set(bitcoin.encode_privkey(bitcoin.decode_privkey(temp_key, 'hex'), 'wif'))
    priv_hex_comp.set(entry_priv_hex.get()+'01')
    priv_WIF_comp.set(bitcoin.encode_privkey(bitcoin.decode_privkey(entry_priv_hex_comp.get(), 'hex'), 'wif'))
    pub_x.set(bitcoin.fast_multiply(bitcoin.G,bitcoin.decode_privkey(temp_key, 'hex'))[0])
    pub_y.set(bitcoin.fast_multiply(bitcoin.G,bitcoin.decode_privkey(temp_key, 'hex'))[1])
    pub_hex.set(bitcoin.encode_pubkey(bitcoin.fast_multiply(bitcoin.G,bitcoin.decode_privkey(temp_key, 'hex')),'hex'))
    pub_hex_comp.set(number_function())
    v.set("当前显示第%d个密钥信息，选中上面相应的比特币地址后 Ctrl+V 分享给你的小伙伴吧 :)" % (bitcoinwallet_LIST.index(temp_key)))

frame_butt = Frame(top)
frame_butt.pack(fill=X,padx=5)
butt_up = Button(frame_butt,text='点我查看上一个地址',pady=5,padx=100,bg='blue',fg='white',bd=4,font=('TkDefaultFont',11),command=pre_function)
butt_up.pack(side=LEFT,padx=5)
butt_down = Button(frame_butt,text='点我查看下一个地址',pady=5,padx=100,bg='blue',fg='white',bd=4,font=('TkDefaultFont',11),command=nex_function)
butt_down.pack(side=RIGHT,padx=5)

frame_1 = Frame(top)
frame_1.pack(fill=X,padx=5,pady=5)
lab_addr_ucomp = Label(frame_1,text='非压缩比特币地址：',width=22,relief=RAISED,bd=3,font=('TkDefaultFont',11))
lab_addr_ucomp.pack(side=LEFT,padx=5)
addr_ucomp = StringVar()
entry_addr_ucomp = Entry(frame_1, textvariable=addr_ucomp,relief=SUNKEN,bd=4,state='readonly',width=41)
entry_addr_ucomp.pack(side=LEFT)
addr_ucomp.set(bitcoin.pubkey_to_address(bitcoin.encode_pubkey(bitcoin.fast_multiply(bitcoin.G,bitcoin.decode_privkey(temp_key, 'hex')),'hex')))
lab_addr_comp = Label(frame_1,text='压缩比特币地址：',width=22,relief=RAISED,bd=3,font=('TkDefaultFont',11))
lab_addr_comp.pack(side=LEFT,padx=5)
addr_comp = StringVar()
entry_addr_comp = Entry(frame_1, textvariable=addr_comp,relief=SUNKEN,bd=4,state='readonly',width=41)
entry_addr_comp.pack(side=LEFT)
addr_comp.set(bitcoin.pubkey_to_address(number_function()))

#私钥信息
separator_2 = Frame(top,height=2,bd=1,relief=SUNKEN)
separator_2.pack(fill=X,padx=5,pady=5)
lab_priv = Label(top,text='相对应的私钥信息',bg="red", fg="white",relief=RIDGE,bd=4,font=('TkDefaultFont',12),pady=10)
lab_priv.pack(fill=X,padx=5,pady=5)
frame_2 = Frame(top)
frame_2.pack(fill=X,padx=5,pady=5)
lab_priv_dec = Label(frame_2,text='私钥（十进制）：',relief=RAISED,width=25,bd=3)
lab_priv_dec.pack(side=LEFT,padx=5)
priv_dec = StringVar()
entry_priv_dec = Entry(frame_2, textvariable=priv_dec,relief=SUNKEN,bd=4,state='readonly')
entry_priv_dec.pack(fill=X)
priv_dec.set(bitcoin.decode_privkey(temp_key, 'hex'))
frame_3 = Frame(top)
frame_3.pack(fill=X,padx=5,pady=5)
lab_priv_hex = Label(frame_3,text='私钥（十六进制）：',relief=RAISED,width=25,bd=3)
lab_priv_hex.pack(side=LEFT,padx=5)
priv_hex = StringVar()
entry_priv_hex = Entry(frame_3, textvariable=priv_hex,relief=SUNKEN,bd=4,state='readonly')
entry_priv_hex.pack(fill=X)
priv_hex.set(temp_key)
frame_4 = Frame(top)
frame_4.pack(fill=X,padx=5,pady=5)
lab_priv_WIF = Label(frame_4,text='私钥（WIF格式）：',relief=RAISED,width=25,bd=3)
lab_priv_WIF.pack(side=LEFT,padx=5)
priv_WIF = StringVar()
entry_priv_WIF = Entry(frame_4, textvariable=priv_WIF,relief=SUNKEN,bd=4,state='readonly')
entry_priv_WIF.pack(fill=X)
priv_WIF.set(bitcoin.encode_privkey(bitcoin.decode_privkey(temp_key, 'hex'), 'wif'))
frame_5 = Frame(top)
frame_5.pack(fill=X,padx=5,pady=5)
lab_priv_hex_comp = Label(frame_5,text='压缩私钥（十六进制）：',relief=RAISED,width=25,bd=3)
lab_priv_hex_comp.pack(side=LEFT,padx=5)
priv_hex_comp = StringVar()
entry_priv_hex_comp = Entry(frame_5, textvariable=priv_hex_comp,relief=SUNKEN,bd=4,state='readonly')
entry_priv_hex_comp.pack(fill=X)
priv_hex_comp.set(entry_priv_hex.get()+'01')
frame_6 = Frame(top)
frame_6.pack(fill=X,padx=5,pady=5)
lab_priv_WIF_comp = Label(frame_6,text='压缩私钥（WIF格式）：',relief=RAISED,width=25,bd=3)
lab_priv_WIF_comp.pack(side=LEFT,padx=5)
priv_WIF_comp = StringVar()
entry_priv_WIF_comp = Entry(frame_6, textvariable=priv_WIF_comp,relief=SUNKEN,bd=4,state='readonly')
entry_priv_WIF_comp.pack(fill=X)
priv_WIF_comp.set(bitcoin.encode_privkey(bitcoin.decode_privkey(entry_priv_hex_comp.get(), 'hex'), 'wif'))

#公钥信息
separator_2 = Frame(top,height=2,bd=1,relief=SUNKEN)
separator_2.pack(fill=X,padx=5,pady=5)
lab_pub = Label(top,text='相对应的公钥信息',bg="red", fg="white",relief=RIDGE,bd=4,font=('TkDefaultFont',12),pady=10)
lab_pub.pack(fill=X,padx=5,pady=5)
lab_fr0 = LabelFrame(top,text='公钥X坐标（十进制）',padx=5,pady=5)
lab_fr0.pack(fill=X,padx=5)
pub_x = StringVar()
entry_pub_x = Entry(lab_fr0,textvariable=pub_x,state='readonly')
entry_pub_x.pack(fill=X)
pub_x.set(bitcoin.fast_multiply(bitcoin.G,bitcoin.decode_privkey(temp_key, 'hex'))[0])
lab_fr1 = LabelFrame(top,text='公钥Y坐标（十进制）',padx=5,pady=5)
lab_fr1.pack(fill=X,padx=5)
pub_y = StringVar()
entry_pub_y = Entry(lab_fr1,textvariable=pub_y,state='readonly')
entry_pub_y.pack(fill=X)
pub_y.set(bitcoin.fast_multiply(bitcoin.G,bitcoin.decode_privkey(temp_key, 'hex'))[1])
lab_fr2 = LabelFrame(top,text='公钥（十六进制）',padx=5,pady=5)
lab_fr2.pack(fill=X,padx=5)
pub_hex = StringVar()
entry_pub_hex = Entry(lab_fr2,textvariable=pub_hex,state='readonly')
entry_pub_hex.pack(fill=X)
pub_hex.set(bitcoin.encode_pubkey(bitcoin.fast_multiply(bitcoin.G,bitcoin.decode_privkey(temp_key, 'hex')),'hex'))
lab_fr3 = LabelFrame(top,text='压缩公钥（十六进制）',padx=5,pady=5)
lab_fr3.pack(fill=X,padx=5)
pub_hex_comp = StringVar()
entry_pub_hex_comp = Entry(lab_fr3,textvariable=pub_hex_comp,state='readonly')
entry_pub_hex_comp.pack(fill=X)
pub_hex_comp.set(number_function())

#状态栏
v = StringVar()
lab_state = Label(top,textvariable=v)
lab_state.pack(fill=X,pady=4)
v.set("当前显示第%d个密钥信息，选中上面相应的比特币地址后Ctrl+V分享给你的小伙伴吧 :)" % (bitcoinwallet_LIST.index(temp_key)))

mainloop()