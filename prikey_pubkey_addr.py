import bitcoin

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
