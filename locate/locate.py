def getAbsCoor(p):
    ans = ()
    if p == 'C':
        ans = (0, 0)
    elif p == 'P1':
        ans = (-52.5, -32)
    elif p == 'P2':
        ans = (-52.5, 32)
    elif p == 'P3':
        ans = (52.5, 32)
    elif p == 'P4':
        ans = (52.5, -32)
    elif p == 'P5':
        ans = (0, -32)
    elif p == 'P6':
        ans = (0, 32)
    elif p == 'P7':
        ans = (-30, -7)
    elif p == 'P8':
        ans = (-30, 7)
    elif p == 'P9':
        ans = (30, 7)
    elif p == 'P10':
        ans = (30, -7)
    elif p == 'G1':
        ans = (-52.5, 0)
    elif p == 'G2':
        ans = (52.5, 0)
    return ans


if __name__ == '__main__':
    msg = '(P8 22 0) (P7 27.7 30)'
    s_msg = msg.split()

    p1_f = s_msg[0].strip('(')
    p1_r = float(s_msg[1])
    p1_theta = float(s_msg[2].strip(')'))

    p2_f = s_msg[3].strip('(')
    p2_r = float(s_msg[4])
    p2_theta = float(s_msg[5].strip(')'))

    p1_c = getAbsCoor(p1_f)
    p2_c = getAbsCoor(p2_f)

    dis = ((p1_c[0] - p2_c[0]) ** 2 + (p1_c[1] - p2_c[1]) ** 2) ** 0.5
    a = (p1_r ** 2 - p2_r ** 2 + dis ** 2) / (2 * dis)
    h = (p1_r ** 2 - a ** 2) ** 0.5

    cos_a = (p2_c[0] - p1_c[0]) / dis
    sin_a = (p2_c[1] - p1_c[1]) / dis
    pb_x = p1_c[0] + a * cos_a
    pb_y = p1_c[1] + a * sin_a

    if (p2_theta - p1_theta) > 0:
        sign = 1
    else:
        sign = -1

    px = pb_x - h * sign * sin_a
    py = pb_y + h * sign * cos_a

    print('坐标为：({},{})'.format(px, py))
