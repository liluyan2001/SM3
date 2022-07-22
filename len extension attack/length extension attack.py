from gmssl import sm3, func
import random
import newSM3
import struct

note = str(random.random())
note_hash = sm3.sm3_hash(func.bytes_to_list(bytes(note, encoding='utf-8')))
note_len = len(note)
append_message = "liluyan202022180198"   # 附加消息
pad_str = ""
pad = []


def generate_guess_hash(old_hash, note_len, append_message):

    vectors = []
    message = ""
    # 将old_hash分组，每组8个字节, 并转换为整数
    for r in range(0, len(old_hash), 8):
        vectors.append(int(old_hash[r:r + 8], 16))

    # 伪造消息
    if note_len > 64:
        for i in range(0, int(note_len / 64) * 64):
            message += 'a'
    for i in range(0, note_len % 64):
        message += 'a'
    message = func.bytes_to_list(bytes(message, encoding='utf-8'))
    message = padding(message)
    message.extend(func.bytes_to_list(bytes(append_message, encoding='utf-8')))
    return newSM3.sm3_hash(message, vectors)


def padding(msg):
    mlen = len(msg)
    msg.append(0x80)
    mlen += 1
    tail = mlen % 64
    range_end = 56
    if tail > range_end:
        range_end = range_end + 64
    for i in range(tail, range_end):
        msg.append(0x00)
    bit_len = (mlen - 1) * 8
    msg.extend([int(x) for x in struct.pack('>q', bit_len)])
    for j in range(int((mlen - 1) / 64) * 64 + (mlen - 1) % 64, len(msg)):
        global pad
        pad.append(msg[j])
        global pad_str
        pad_str += str(hex(msg[j]))
    return msg


guess_hash = generate_guess_hash(note_hash, note_len, append_message)
new_msg = func.bytes_to_list(bytes(note, encoding='utf-8'))
new_msg.extend(pad)
new_msg.extend(func.bytes_to_list(bytes(append_message, encoding='utf-8')))
new_msg_str = note + pad_str + append_message

new_hash = sm3.sm3_hash(new_msg)

print("note: "+note)
print("附加消息:", append_message)
print("new message: \n" + new_msg_str)
print("note hash:" + note_hash)
print("hash(new note):" + new_hash)
print("guess hash:" + guess_hash)

if new_hash == guess_hash:
    print("长度扩展攻击成功")
else:
    print("长度扩展攻击失败")
