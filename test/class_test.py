# coding=utf-8
import random
import sys


class FakeUser:
    def fake_name(self, amount, one_word=False, two_words=False):
        n = 0
        while n <= amount:
            if one_word:
                full_name = random.choice(fn) + random.choice(ln1)
            elif two_words:
                full_name = random.choice(fn) + random.choice(ln2)
            else:
                full_name = random.choice(fn) + random.choice(ln1 + ln2)
            yield full_name
            n += 1

    def fake_gender(self, amount=1):
        n = 0
        while n <= amount:
            gender = random.choice(['男', '女', '未知'])
            yield gender
            n += 1


class SnsUser(FakeUser):
    def get_followers(self, amount=1, few=True, a_lot=False):
        n = 0
        while n <= amount:
            if few:
                followers = random.randrange(1, 50)
            elif a_lot:
                followers = random.randrange(200, 10000)
            yield followers
            n += 1


fn = (
    '李', '王', '张', '刘', '陈', '杨', '周', '黄', '孙', '吴', '徐', '赵', '林', '胡', '朱', '梁', '郭', '高', '何', '马', '郑', '罗', '宋',
    '唐',
    '谢', '叶', '韩', '任', '潘', '于', '冯', '蒋', '董', '吕', '邓', '许', '曹', '曾', '袁', '汪', '程', '田', '彭', '钟', '蔡', '魏', '沈',
    '方',
    '卢', '余', '杜', '丁', '苏', '贾', '姚', '姜', '陆', '戴', '傅', '夏', '廖', '萧', '石', '江', '范', '今', '谭', '邹', '崔', '薛', '邱',
    '康',
    '史', '侯', '邵', '熊', '秦', '雷', '孟', '庞', '白', '毛', '郝', '钱', '段', '俞', '洪', '汤', '顾', '贺', '龚', '尹', '万', '龙', '赖',
    '章',
    '孔', '武', '邢', '颜', '梅', '阮', '黎', '常', '倪', '施', '乔', '樊', '严', '齐', '陶', '向', '温', '文', '易', '兰', '闫', '芦', '牛',
    '尚  ', '安', '管', '殷', '霍', '翟', '佘', '葛', '庄', '伍', '辛', '申', '付', '代', '鲁', '季', '覃', '柳', '单', '房', '左', '尤', '凌',
    '韦', '柯', '鲍', '蒲', '牟', '屈', '成', '游', '祁')
ln1 = (
    '娉', '览', '莱', '屹', '佳', '涵', '轩', '泓', '妍', '乐', '嘉', '哲', '俊', '博', '宇', '凯', '伊', '淇', '一', '渊', '逸', '凡', '悦',
    '奕',
    '晨', '怡', '泽', '依', '浩', '彤', '冰', '媛', '洲', '森', '淳', '羽', '锋')
ln2 = (
    '治明', '正顺', '书铎', '嘉赐', '嘉容', '嘉勋', '宾鸿', '宾实', '彬彬', '彬炳', '彬郁', '斌斌', '斌蔚', '滨海', '波光', '波鸿', '波峻', '博瀚', '博超',
    '博简',
    '博明', '鹏赋', '鹏海', '鹏鲸', '鹏鹍', '璞玉', '奇玮', '祺福', '锐锋', '锐思', '睿才', '绍钧', '思源', '天罡', '天工', '天翰', '天和', '天华', '伟博',
    '伟彦',
    '兴朝', '星汉', '星渊', '英华', '温纶', '温茂', '温书', '温韦', '文昌', '文成', '文栋', '子墨', '子平', '子琪', '泽宇')

user_a = FakeUser()
user_b = SnsUser()
print(sys.path[3])