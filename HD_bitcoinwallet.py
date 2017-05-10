import bitcoin
import hashlib

# Generate a random private key as a root seed********************************************************
valid_private_key_seed = False
while not valid_private_key_seed:
    private_key_seed = bitcoin.random_key()
    decoded_private_key_seed = bitcoin.decode_privkey(private_key_seed, 'hex')
    valid_private_key_seed =  0 < decoded_private_key_seed < bitcoin.N
print ("随机种子256 bits（十六进制）： ", private_key_seed)

# 由种子生成主私钥、主公钥、比特币地址
hash512_sequence = hashlib.sha512(private_key_seed.encode('utf-8')).hexdigest()
master_private_key = hash512_sequence[:64]
main_chain_code = hash512_sequence[64:]
master_public_key = bitcoin.encode_pubkey(bitcoin.fast_multiply(bitcoin.G,bitcoin.decode_privkey(master_private_key, 'hex')),'hex')
master_address = bitcoin.pubkey_to_address(master_public_key)
print ("主私钥（十六进制）：           ", master_private_key)
print ("主公钥（非压缩十六进制）：     ", master_public_key)
print ("相应比特币地址(b58check)：     ", master_address)

# 分层确定性钱包使用CKD（child key derivation）方程去从母密钥衍生出子密钥
# 生成3个子密钥
index_0 = '0000'
index_1 = '0001'
index_2 = '0002'

child_0_hash512_sequence = hashlib.sha512((master_public_key + main_chain_code + index_0).encode('utf-8')).hexdigest()
child_0_private_key = child_0_hash512_sequence[:64]
child_0_chain_code = child_0_hash512_sequence[64:]
child_0_public_key = bitcoin.encode_pubkey(bitcoin.fast_multiply(bitcoin.G,bitcoin.decode_privkey(child_0_private_key, 'hex')),'hex')
child_0_address = bitcoin.pubkey_to_address(child_0_public_key)
print ("索引0子私钥（十六进制）：      ", child_0_private_key)
print ("索引0子公钥（非压缩十六进制）：", child_0_public_key)
print ("相应比特币地址(b58check)：     ", child_0_address)

child_1_hash512_sequence = hashlib.sha512((master_public_key + main_chain_code + index_1).encode('utf-8')).hexdigest()
child_1_private_key = child_1_hash512_sequence[:64]
child_1_chain_code = child_1_hash512_sequence[64:]
child_1_public_key = bitcoin.encode_pubkey(bitcoin.fast_multiply(bitcoin.G,bitcoin.decode_privkey(child_1_private_key, 'hex')),'hex')
child_1_address = bitcoin.pubkey_to_address(child_1_public_key)
print ("索引1子私钥（十六进制）：      ", child_1_private_key)
print ("索引1子公钥（非压缩十六进制）：", child_1_public_key)
print ("相应比特币地址(b58check)：     ", child_1_address)

child_2_hash512_sequence = hashlib.sha512((master_public_key + main_chain_code + index_2).encode('utf-8')).hexdigest()
child_2_private_key = child_2_hash512_sequence[:64]
child_2_chain_code = child_2_hash512_sequence[64:]
child_2_public_key = bitcoin.encode_pubkey(bitcoin.fast_multiply(bitcoin.G,bitcoin.decode_privkey(child_2_private_key, 'hex')),'hex')
child_2_address = bitcoin.pubkey_to_address(child_2_public_key)
print ("索引2子私钥（十六进制）：      ", child_2_private_key)
print ("索引2子公钥（非压缩十六进制）：", child_2_public_key)
print ("相应比特币地址(b58check)：     ", child_2_address)