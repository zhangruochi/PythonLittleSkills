"""
在python3中 str 的实例包含 unicode 字符
bytes 的实例包含8位原始的值
"""

def other_to_str(bytes_or_str):
    if isinstance(bytes_or_str,bytes):
        return bytes_or_str.decode("utf-8")
    string = bytes_or_str
    return string

def other_to_bytes(bytes_or_str):
    if isinstance(bytes_or_str,str):
        return bytes_or_str.encode("utf-8")
    bytes_value = bytes_or_str
    return bytes_value

"""
在python2中 str 包含原始的8位值
unicode实例 包含 unicode 字符              
"""

def other_to_str(unicode_or_str):
    if isinstance(unicode_or_str,unicode):
        return bytes_or_str.encode("utf-8")
    string = bytes_or_str
    return string

def other_to_unicode(unicode_or_str):
    if isinstance(unicode_or_str,str):
        return unicode_or_str.decode("utf-8")
    value = unicode_or_str
    return value    