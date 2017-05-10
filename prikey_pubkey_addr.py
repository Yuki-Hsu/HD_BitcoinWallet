import bitcoin
from tkinter import *

# Generate a random private key***********************************************************************
valid_private_key = False
while not valid_private_key:
    private_key = bitcoin.random_key()
    decoded_private_key = bitcoin.decode_privkey(private_key, 'hex')
    valid_private_key =  0 < decoded_private_key < bitcoin.N

print ("私钥（十六进制）：      ", private_key)
print ("私钥（十进制）：        ", decoded_private_key)

# Convert private key to WIF format
wif_encoded_private_key = bitcoin.encode_privkey(decoded_private_key, 'wif')
print ("私钥（WIF格式）：       ", wif_encoded_private_key)

# Add suffix "01" to indicate a compressed private key
compressed_private_key = private_key + '01'
print ("压缩私钥（十六进制）：  ", compressed_private_key)

# Generate a WIF format from the compressed private key (WIF-compressed)
wif_compressed_private_key = bitcoin.encode_privkey(bitcoin.decode_privkey(compressed_private_key, 'hex'), 'wif')
print ("压缩私钥（WIF格式）：   ", wif_compressed_private_key)

# Generate a public key*******************************************************************************
# Multiply the EC generator point G with the private key to get a public key point
public_key = bitcoin.fast_multiply(bitcoin.G,decoded_private_key)
print ("公钥十进制坐标(x,y)：   ", public_key)

# Encode as hex, prefix 04
hex_encoded_public_key = bitcoin.encode_pubkey(public_key,'hex')
print ("公钥十六进制非压缩：    ", hex_encoded_public_key)

# Compress public key, adjust prefix depending on whether y is even or odd
(public_key_x, public_key_y) = public_key
if (public_key_y % 2) == 0:
     compressed_prefix = '02' 
else:
     compressed_prefix = '03'
hex_compressed_public_key = compressed_prefix + bitcoin.encode(public_key_x, 16)
print ("公钥十六进制压缩：      ", hex_compressed_public_key)

# Generate bitcoin address from public key************************************************************
print ("比特币地址(b58check)：  ", bitcoin.pubkey_to_address(public_key))

# Generate compressed bitcoin address from compressed public key
print ("压缩公钥地址(b58check)：", bitcoin.pubkey_to_address(hex_compressed_public_key))





#GUI
#图片+标题
top = Tk()
top.geometry('1000x670')
top.title('比特币钱包模型')
# photo = PhotoImage(file=r"C:\Users\A1718\下载\bitcoin.jpg")
# lab_top = Label(top,text='比特币钱包模型',image=photo,compound=LEFT,bg='yellow',pady=10,padx=10,relief=RIDGE,bd=8,font=('TkDefaultFont',45,'bold'))
# lab_top.pack(fill=X,padx=5,pady=5)
# separator = Frame(top,height=2,bd=1,relief=SUNKEN)
# separator.pack(fill=X,padx=5,pady=5)

#比特币地址内容
lab_addr = Label(top,text='比特币地址',bg="red", fg="white",relief=RIDGE,bd=4,font=('TkDefaultFont',12),pady=10)
lab_addr.pack(fill=X,padx=5,pady=5)

def up_function():
    pass

def down_function():
    pass

frame_butt = Frame(top)
frame_butt.pack(fill=X,padx=5)
butt_up = Button(frame_butt,text='点我查看上一个地址',pady=5,padx=100,bg='blue',fg='white',bd=4,font=('TkDefaultFont',11),command=up_function)
butt_up.pack(side=LEFT,padx=5)
butt_down = Button(frame_butt,text='点我查看下一个地址',pady=5,padx=100,bg='blue',fg='white',bd=4,font=('TkDefaultFont',11),command=down_function)
butt_down.pack(side=RIGHT,padx=5)

frame_1 = Frame(top)
frame_1.pack(fill=X,padx=5,pady=5)
lab_addr_ucomp = Label(frame_1,text='非压缩比特币地址：',width=22,relief=RAISED,bd=3,font=('TkDefaultFont',11))
lab_addr_ucomp.pack(side=LEFT,padx=5)
addr_ucomp = StringVar()
entry_addr_ucomp = Entry(frame_1, textvariable=addr_ucomp,relief=SUNKEN,bd=4,state='readonly',width=41)
entry_addr_ucomp.pack(side=LEFT)
addr_ucomp.set(bitcoin.pubkey_to_address(public_key))
lab_addr_comp = Label(frame_1,text='压缩比特币地址：',width=22,relief=RAISED,bd=3,font=('TkDefaultFont',11))
lab_addr_comp.pack(side=LEFT,padx=5)
addr_comp = StringVar()
entry_addr_comp = Entry(frame_1, textvariable=addr_comp,relief=SUNKEN,bd=4,state='readonly',width=41)
entry_addr_comp.pack(side=LEFT)
addr_comp.set(bitcoin.pubkey_to_address(hex_compressed_public_key))

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
priv_dec.set(decoded_private_key)
frame_3 = Frame(top)
frame_3.pack(fill=X,padx=5,pady=5)
lab_priv_hex = Label(frame_3,text='私钥（十六进制）：',relief=RAISED,width=25,bd=3)
lab_priv_hex.pack(side=LEFT,padx=5)
priv_hex = StringVar()
entry_priv_hex = Entry(frame_3, textvariable=priv_hex,relief=SUNKEN,bd=4,state='readonly')
entry_priv_hex.pack(fill=X)
priv_hex.set(private_key)
frame_4 = Frame(top)
frame_4.pack(fill=X,padx=5,pady=5)
lab_priv_WIF = Label(frame_4,text='私钥（WIF格式）：',relief=RAISED,width=25,bd=3)
lab_priv_WIF.pack(side=LEFT,padx=5)
priv_WIF = StringVar()
entry_priv_WIF = Entry(frame_4, textvariable=priv_WIF,relief=SUNKEN,bd=4,state='readonly')
entry_priv_WIF.pack(fill=X)
priv_WIF.set(wif_encoded_private_key)
frame_5 = Frame(top)
frame_5.pack(fill=X,padx=5,pady=5)
lab_priv_hex_comp = Label(frame_5,text='压缩私钥（十六进制）：',relief=RAISED,width=25,bd=3)
lab_priv_hex_comp.pack(side=LEFT,padx=5)
priv_hex_comp = StringVar()
entry_priv_hex_comp = Entry(frame_5, textvariable=priv_hex_comp,relief=SUNKEN,bd=4,state='readonly')
entry_priv_hex_comp.pack(fill=X)
priv_hex_comp.set(compressed_private_key)
frame_6 = Frame(top)
frame_6.pack(fill=X,padx=5,pady=5)
lab_priv_WIF_comp = Label(frame_6,text='压缩私钥（WIF格式）：',relief=RAISED,width=25,bd=3)
lab_priv_WIF_comp.pack(side=LEFT,padx=5)
priv_WIF_comp = StringVar()
entry_priv_WIF_comp = Entry(frame_6, textvariable=priv_WIF_comp,relief=SUNKEN,bd=4,state='readonly')
entry_priv_WIF_comp.pack(fill=X)
priv_WIF_comp.set(wif_compressed_private_key)

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
pub_x.set(public_key[0])
lab_fr1 = LabelFrame(top,text='公钥Y坐标（十进制）',padx=5,pady=5)
lab_fr1.pack(fill=X,padx=5)
pub_y = StringVar()
entry_pub_y = Entry(lab_fr1,textvariable=pub_y,state='readonly')
entry_pub_y.pack(fill=X)
pub_y.set(public_key[1])
lab_fr2 = LabelFrame(top,text='公钥（十六进制）',padx=5,pady=5)
lab_fr2.pack(fill=X,padx=5)
pub_hex = StringVar()
entry_pub_hex = Entry(lab_fr2,textvariable=pub_hex,state='readonly')
entry_pub_hex.pack(fill=X)
pub_hex.set(hex_encoded_public_key)
lab_fr3 = LabelFrame(top,text='压缩公钥（十六进制）',padx=5,pady=5)
lab_fr3.pack(fill=X,padx=5)
pub_hex_comp = StringVar()
entry_pub_hex_comp = Entry(lab_fr3,textvariable=pub_hex_comp,state='readonly')
entry_pub_hex_comp.pack(fill=X)
pub_hex_comp.set(hex_compressed_public_key)

mainloop()

