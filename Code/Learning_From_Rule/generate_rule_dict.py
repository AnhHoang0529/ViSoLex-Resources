import pandas as pd
rule_dict = {} #key is rule ID and value is Label id. here it means rule 1 labels example as location
label2class = {} #key is Label Id, value is label
class_by_rule = ['không', 'quá', 'khóc', 'tao', 'nhen', 'dài', 'vãi', 'đó', 'này', 'đi',\
        'trai', 'sao', 'thôi', 'thế', 'nào', 'hèn', 'nữa', 'cái', 'ơi', 'á', 'luôn',\
        'rồi' , 'được', 'đã', 'ba', 'vò', 'nha', 'ê', 'à', 'đúng','đâu', 'buồn', 'biết', 'lòng',\
        'gớm' , 'ăn', 'thật', 'đây', 'chị', 'đấy', 'nhé', 'bên', 'xui', 'em', 'yêu', 'chưa', \
        'nhe', 'bạn', 'ta', 'giỏi', 'điên', 'đẹp', 'xỉu', 'xu', 'dạ', 'vui', 'đéo', 'qua', 'học', 'giùm',\
        'ghê', 'trời', 'có','trai', 'mà', 'khóc', 'lắm', 'ghét', 'quên','mày', 'nè', 'ai', 'vịt', 'vậy',\
        'lời', 'lên', 'tức']

for i, label in enumerate(class_by_rule):
    j = i+1
    rule_dict[i] = j
    label2class[j] = label

class2label = {value: key for key, value in label2class.items()}