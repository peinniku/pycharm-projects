CN_mobile = \
    [134, 135, 136, 137, 138, 139, 150, 151, 152, 157, 158, 159, 182, 183, 184, 187, 188, 147, 178, 1705]
CN_union = [130, 131, 132, 155, 156, 185, 186, 145, 176, 1709]
CN_telecom = [133, 153, 180, 181, 189, 177, 1700]

num = input('enter your number: ')
num3 = int(num[:3])
num4 = int(num[:4])
if len(num) < 11:
    print('should be in 11 digits')
elif num3 in CN_mobile or num3 in CN_telecom or num3 in CN_union \
        or num4 in CN_union or num4 in CN_telecom or num4 in CN_mobile:
    if num3 in CN_mobile or num4 in CN_mobile:
        print('operator: china mobile')
    if num3 in CN_telecom or num4 in CN_telecom:
        print('operator: china telecom')
    if num3 in CN_union or num4 in CN_union:
        print('operator: china union')
else:
    print('no such operator')
