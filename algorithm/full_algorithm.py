import math

str_length = 0
letter_list = []
for i in range(97, 123):
    letter_list.append(chr(i))
count_dic = {}
psb_dic = {}


def d2b(d, length):
    b = ''
    for i in range(0, length):
        d *= 2
        if d >= 1:
            b += '1'
            d -= 1
        else:
            b += '0'
    return b


def b2d(b):
    d = 0
    for i in range(0, len(b)):
        if b[i] == '1':
            d += pow(2, -(i + 1))
    return d


def encode(str):
    low = 0
    high = 1
    width = high - low

    for i in range(0, str_length):
        c = str[i].lower()
        p = 0
        for j in range(ord('a'), ord(c)):
            p += psb_dic[chr(j)]
        low += width * p
        high = low + width * psb_dic[c]
        width = high - low

    result = high - width * 0.01
    print('编码选取的数：', result)
    code_length = math.ceil(math.log2(1 / width))
    return d2b(result, code_length)


def decode(code):
    result = b2d(code)
    low = 0
    high = 1
    width = high - low
    str = ''

    for i in range(0, str_length):
        cpsb = low
        for j in range(97, 123):

            if cpsb < result < (cpsb + width * psb_dic[chr(j)]):
                str += chr(j)
                low = cpsb
                high = cpsb + width * psb_dic[chr(j)]
                width = high - low
                break
            cpsb += width * psb_dic[chr(j)]

    return str


def shannon(psb):
    add_psb = 0
    code_dic = {}
    for item in psb:
        if item[1] == 0:
            break
        add_fs = add_psb + item[1] * 0.5
        add_psb += item[1]
        length = math.ceil(math.log2(1 / item[1]))
        code_dic[item[0]] = d2b(add_fs, length)
    return code_dic


if __name__ == '__main__':
    str_list = list(input('请输入字母序列(每8位需输入一位空格)：').split())
    print('完全统计编码')
    code_list = []
    decode_list = []
    full_len = 0
    shan_len = 0
    count_dic = count_dic.fromkeys(letter_list, 0)
    for str in str_list:
        for c in str:
            count_dic[c] += 1
            str_length += 1

    for i in range(97, 123):
        psb_dic[chr(i)] = count_dic[chr(i)] / str_length
    for str in str_list:
        str_length = len(str)
        code = encode(str)
        code_list.append(code)
        decode_str = decode(code)
        decode_list.append(decode_str)
    print('编码结果：')
    for code in code_list:
        print(code, end=' ')
        full_len += len(code)
    print('')
    print('编码长度：', full_len)
    for str in decode_list:
        print(str, end=' ')

    print('\n')
    print('香农编码')
    sort_psb = sorted(psb_dic.items(), key=lambda item: item[1], reverse=True)
    shannon_dic = shannon(sort_psb)
    print('编码结果：')
    for str in str_list:
        for c in str:
            print(shannon_dic[c], end='')
            shan_len += len(shannon_dic[c])
    print('')
    print('编码长度：', shan_len)
    print('编码长度之比为', full_len / shan_len)
