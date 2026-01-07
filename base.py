import re


def verify_password():
    """"
    返回值：包含两个元素的元组，第一个元素是布尔值(True表示密码规范，False表示不规范)
           第二个元素是字符串(若密码不规范，则提供具体原因；若规范，则为None
    """
    password = input("请输入密码:")
    # 1.长度位于6-20之间
    if not 6 <= len(password) <= 20:
        return False, "密码长度必须在6-20之间"
    # 2.必须包含至少1个小写字母
    if not re.findall(r"[a-z]", password):
        return False, "密码必须包含至少1个小写字母~"
    # 3.必须包含至少1个大写字母
    if not re.findall(r"[A-Z]", password):
        return False, "密码必须包含至少1个大写字母~"
    # 4.必须包含至少1个数字
    if not re.findall(r"\d", password):
        return False, "密码必须包含至少1个数字~"
    # 5.必须包含至少1个特殊字符
    if not re.findall(r"W", password):
        return False, "密码必须包含至少1个特殊字符~"
    return True, None
