import re
import numpy as np
from generate_rule_dict import rule_dict,label2class

def get_sent_dict(sentence_list):
  #list_of_words=sentence.strip().split(" ")
  list_of_words = sentence_list
  length_of_words=[len(i)+1 for i in list_of_words]
  words=[0]
  words.extend(length_of_words[0:-1])
  cummulative_list=np.cumsum(words)
  cummulative_list[0]=0
  sent_dict=dict(zip(cummulative_list,range(len(cummulative_list))))
  return sent_dict

#ex: thích anh cá mập k
#ex602	2 nói điiiii , lý do 2 che là như vầy phải honggggggg
def rule0(sentence,sent_dict,rule_firing):
  label= rule_dict[0]
  s=sentence.lower()
  pattern= re.compile(r'\b(k|khu+m+|khong|hong+g+|hông+g+)\b')
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
        
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

  #ex: ủa alo bất công quákkk / quáaaaaaa (k có thể lặp lại n lần)
def rule1(sentence,sent_dict,rule_firing):
  label= rule_dict[1]
  s=sentence.lower()
  pattern= re.compile(r"\b(quá+k+|quá+a+|qué+e+|qé+e+|q+é+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
        
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

  #Ex48: mới vô ca còn đỡ chứ gần về mà vô thì chỉ có nước khók(k có thể lặp lại n lần)
def rule2(sentence,sent_dict,rule_firing):
  label= rule_dict[2]
  s=sentence.lower()
  pattern= re.compile(r"\bkhó+k+\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
        
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex145: trời ơi bây ơi cứu tauuu / taoooo (u hoặc o cuối có thể lặp lại n lần)

def rule3(sentence,sent_dict,rule_firing):
  label= rule_dict[3]
  s=sentence.lower()
  pattern= re.compile(r"\b(ta+u+|ta+o+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
        
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex 161:	mình nghĩ đẹp ớ bạn thích là dc nhenn
def rule4(sentence,sent_dict,rule_firing):
  label= rule_dict[4]
  s=sentence.lower()
  pattern= re.compile(r"\bnhe+n+\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
        
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex180: mà house friend thì gắn bó còn dàiiii
def rule5(sentence,sent_dict,rule_firing):
  label= rule_dict[5]
  s=sentence.lower()
  pattern= re.compile(r"\bdài+i+\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
        
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#ex184: mặt kiểu phán xét vỡiiii / vãiiiii
def rule6(sentence,sent_dict,rule_firing):
  label= rule_dict[6]
  s=sentence.lower()
  pattern= re.compile(r"\b(vãi+i+|vỡi+i+|vai+z+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
        
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex204:	mặt nó đâu ae vn cần thấy đoáaaa / đóooooooooooo / đóaaaaaaaaaaa

def rule7(sentence,sent_dict,rule_firing):
  label= rule_dict[7]
  s=sentence.lower()
  pattern= re.compile(r"\b(đó+o+|đóa+a+|đoá+a+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
        
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex258:	này thì sports - live in peace nàyyyyyy

def rule8(sentence,sent_dict,rule_firing):
  label= rule_dict[8]
  s=sentence.lower()
  pattern= re.compile(r"\b(này+y+|nài+i+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
        
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex336:	nuôi thêm anh em cho kiwi điiiii

def rule9(sentence,sent_dict,rule_firing):
  label= rule_dict[9]
  s=sentence.lower()
  pattern= re.compile(r"\b(đi+i+|di+i+|đê+e+|đêy+y+|đe+e+|de+e+|ik+k+|i+i)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
        
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex386:	học tập đi nha a zaiiii
def rule10(sentence,sent_dict,rule_firing):
  label= rule_dict[10]
  s=sentence.lower()
  pattern= re.compile(r"\bzai+i+\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
        
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex476:	sữa đặc quẹo keo lì tái châu dzữ dzị shaoooo/ saooooooo
def rule11(sentence,sent_dict,rule_firing):
  label= rule_dict[11]
  s=sentence.lower()
  pattern= re.compile(r"\b(shao+o+|sao+o+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
        
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex528:	đây chồng em tăng xương xương có 10-11 cân thoyyyy/thôyyy/thoiiii/thôiiiiiiii
def rule12(sentence,sent_dict,rule_firing):
  label= rule_dict[12]
  s=sentence.lower()
  pattern= re.compile(r"\b(thoy+y+|thoi+i+|thui+i+|thôi+i+|thôy+y+|thồy+y+|thoai+i+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
        
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex559	mấy chị tính ghê théeee/ theeeeeeeee/ thếeeeeeeeee
def rule13(sentence,sent_dict,rule_firing):
  label= rule_dict[13]
  s=sentence.lower()
  pattern= re.compile(r"\b(thé+e+|the+e+|thế+e+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
        
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex564	nổ địa chỉ đi để trải nghiệm nàoooo / naoooooo
def rule14(sentence,sent_dict,rule_firing):
  label= rule_dict[14]
  s=sentence.lower()
  pattern= re.compile(r"\b(nào+o+|nao+o+|nèo+o+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
        
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex635	bất lợi của người hèngggggg / hènnnnnnn
def rule15(sentence,sent_dict,rule_firing):
  label= rule_dict[15]
  s=sentence.lower()
  pattern= re.compile(r"\b(hèng+g|hèn+n+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
        
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex669	tr clm mới chia tay đừng có hiện mấy bài này nữaaaaa
#Ex2607	còn thua cái đèo ngoạn mục nụaaaa
def rule16(sentence,sent_dict,rule_firing):
  label= rule_dict[16]
  s=sentence.lower()
  pattern= re.compile(r"\b(nữa+a+|nụa+a+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
        
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex736	làm ơn ngủ sớm giúp t cáiiiiiii
def rule17(sentence,sent_dict,rule_firing):
  label= rule_dict[17]
  s=sentence.lower()
  pattern= re.compile(r"\b(cái+i+|cais)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
        
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex796	nên là k gì là k thể đâu các bạn ơiiiiiii
#Ex2667	càng ngày càng xinh á trời quoiiii , chị đẹpppppp
def rule18(sentence,sent_dict,rule_firing):
  label= rule_dict[18]
  s=sentence.lower()
  pattern= re.compile(r"\b(ơi+i+|oi+i+|quơi+i+|quoi+i+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
        
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex841	dĩnh bảo ngọt ngào aaaaa
def rule19(sentence,sent_dict,rule_firing):
  label= rule_dict[19]
  s=sentence.lower()
  pattern= re.compile(r"\b(aa+|á+a+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
        
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex875	quá bình thường luonn =))
def rule20(sentence,sent_dict,rule_firing):
  label= rule_dict[20]
  s=sentence.lower()
  pattern= re.compile(r"\b(luon+n+|luôn+n+|luôn+g|lun+n)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
        
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex911	zòyyyy xong sáng mai cái máy tính của em tới công chuyện với c :)))))
def rule21(sentence,sent_dict,rule_firing):
  label= rule_dict[21]
  s=sentence.lower()
  pattern= re.compile(r"\b(zoy+y+|zòy+y+|roi+i+|ròi+i+|rồi+i+|rùi+i+|ùi+i+|roài+i+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
        
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex928	chứ riêng t thà nóng cm nhưng trắng là đượttt
def rule22(sentence,sent_dict,rule_firing):
  label= rule_dict[22]
  s=sentence.lower()
  pattern= re.compile(r"\b(đượt+t+|được+c+|dc+c+|đc+c+|duoc+c+|dd+c)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
        
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex961	trưa nắng nóng quýnh 1 ly rau má đậu xanh dô nó đẽeeee
def rule23(sentence,sent_dict,rule_firing):
  label= rule_dict[23]
  s=sentence.lower()
  pattern= re.compile(r"\b(đẽ+e+|đã+a+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
        
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex1026	có la vie ở đây mà lo gì mấy baaaa
def rule24(sentence,sent_dict,rule_firing):
  label= rule_dict[24]
  s=sentence.lower()
  pattern= re.compile(r"\b(ba+a+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
        
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex1048	xem có 90p mà áp lực vòooooooooo
def rule25(sentence,sent_dict,rule_firing):
  label= rule_dict[25]
  s=sentence.lower()
  pattern= re.compile(r"\b(vò+o+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
        
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex1074	em múc cho cj gáo nước mưa nhaa
#EX2578	khác biệt 1c khó chịu nháaa
def rule26(sentence,sent_dict,rule_firing):
  label= rule_dict[26]
  s=sentence.lower()
  pattern= re.compile(r"\b(nha+a+|nhá+a+|nhoa+a+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
        
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex1087	mình về với nhau thôi em eeiii =))
def rule27(sentence,sent_dict,rule_firing):
  label= rule_dict[27]
  s=sentence.lower()
  pattern= re.compile(r"\b(eei+i+|e+i+|êi+i+|ê+e+|e+e+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
        
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex1108	đúnggggg nhớ cảm giác đi concert quá àaaaaaaa
def rule28(sentence,sent_dict,rule_firing):
  label= rule_dict[28]
  s=sentence.lower()
  pattern= re.compile(r"\b(à+a+|af|àf|à+k+|à+h+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
        
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

def rule29(sentence,sent_dict,rule_firing):
  label= rule_dict[29]
  s=sentence.lower()
  pattern= re.compile(r"\b(đúng+g+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
        
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex1219	nhưng mà sẽ ko có ảnh chụp mình tại concert đâuuuu ko có kỷ niệm rất buồnnnnn
def rule30(sentence,sent_dict,rule_firing):
  label= rule_dict[30]
  s=sentence.lower()
  pattern= re.compile(r"\b(đâu+u+|đôu+u+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
        
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

def rule31(sentence,sent_dict,rule_firing):
  label= rule_dict[31]
  s=sentence.lower()
  pattern= re.compile(r"\b(buồn+n+|bùn+n+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
        
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex1273	trộm vía tuôi kiểu 1 , kiểu high của ai khom biếcccc =))))
def rule32(sentence,sent_dict,rule_firing):
  label= rule_dict[32]
  s=sentence.lower()
  pattern= re.compile(r"\b(biếc+c+|biết+t+|biet+t+|biec+c+|biêts|bieets|biêcs|bít+t+|bíc+c+|bt+t+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
        
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex1317	dzừa lònggg ghê gứmmm lunnn hà :)))))
def rule33(sentence,sent_dict,rule_firing):
  label= rule_dict[33]
  s=sentence.lower()
  pattern= re.compile(r"\b(lòng+g+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
        
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

def rule34(sentence,sent_dict,rule_firing):
  label= rule_dict[34]
  s=sentence.lower()
  pattern= re.compile(r"\b(gớm+m+|gứm+m+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
        
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex1349	không cần ra đường mà vẫn ăngg no
def rule35(sentence,sent_dict,rule_firing):
  label= rule_dict[35]
  s=sentence.lower()
  pattern= re.compile(r"\b(ăn+n+|ăng+g+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
        
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex1514	và đó là sự thặccccc
def rule36(sentence,sent_dict,rule_firing):
  label= rule_dict[36]
  s=sentence.lower()
  pattern= re.compile(r"\b(thặc+c+|thật+t+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
        
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex1545	đi học hay làm trúa hề đâyy
def rule37(sentence,sent_dict,rule_firing):
  label= rule_dict[37]
  s=sentence.lower()
  pattern= re.compile(r"\b(đây+y+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
        
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex1620	chà đạp em đi chịiiiii
def rule38(sentence,sent_dict,rule_firing):
  label= rule_dict[38]
  s=sentence.lower()
  pattern= re.compile(r"\b(chị+i+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
        
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex1622	nghe có vẻ hay đếy =)))
def rule39(sentence,sent_dict,rule_firing):
  label= rule_dict[39]
  s=sentence.lower()
  pattern= re.compile(r"\b(đếy+y+|đấy+y+|đếi+i+|đêí+i+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
        
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex1623	cty tôi k làm t7 nên thành ra nghỉ 4 ngày nhoéeeee
def rule40(sentence,sent_dict,rule_firing):
  label= rule_dict[40]
  s=sentence.lower()
  pattern= re.compile(r"\b(nhé+e+|nhóe+e+|nhoé+e+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
        
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex1797	bt em đã có ng ở cạnh bênnn ~~~
def rule41(sentence,sent_dict,rule_firing):
  label= rule_dict[41]
  s=sentence.lower()
  pattern= re.compile(r"\b(bên+n+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
        
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex1986	ván cược nhiều điều xuii
def rule42(sentence,sent_dict,rule_firing):
  label= rule_dict[42]
  s=sentence.lower()
  pattern= re.compile(r"\b(xui+i+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
        
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex2065	idol một thời cụa emm ...
def rule43(sentence,sent_dict,rule_firing):
  label= rule_dict[43]
  s=sentence.lower()
  pattern= re.compile(r"\b(em+m+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
        
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex2104	đừng hỏi tại sao mừn mất tích nhó bạn iuu
def rule44(sentence,sent_dict,rule_firing):
  label= rule_dict[44]
  s=sentence.lower()
  pattern= re.compile(r"\b(iu+u|yêu+u+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
        
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#2129	em bé làm nhưng phải ráng giữ sức khoẻ nghe chưaaa
def rule45(sentence,sent_dict,rule_firing):
  label= rule_dict[45]
  s=sentence.lower()
  pattern= re.compile(r"\b(chưa+a+|chữa+a+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
        
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex2176	mơi mốt cô đừng có zị nhee
def rule46(sentence,sent_dict,rule_firing):
  label= rule_dict[46]
  s=sentence.lower()
  pattern= re.compile(r"\b(nhe+e+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
        
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex2199	guốc t cũng mòn hết đế r chúng pạnnnn
def rule47(sentence,sent_dict,rule_firing):
  label= rule_dict[47]
  s=sentence.lower()
  pattern= re.compile(r"\b(pạ+n+|bạn+n+|bẹ+n+|pẹ+n+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
        
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex2222	thế mà khum nghĩ ra taaa
def rule48(sentence,sent_dict,rule_firing):
  label= rule_dict[48]
  s=sentence.lower()
  pattern= re.compile(r"\b(ta+a+|te+e+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
        
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex2305	húuuuu ghệ đẹp quá giỏiii
def rule49(sentence,sent_dict,rule_firing):
  label= rule_dict[49]
  s=sentence.lower()
  pattern= re.compile(r"\b(giỏi+i+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
        
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex2333	triệu lệ dĩnh xinh điênnnn
def rule50(sentence,sent_dict,rule_firing):
  label= rule_dict[50]
  s=sentence.lower()
  pattern= re.compile(r"\b(điên+n|đin+n+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
        
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex2667	càng ngày càng xinh á trời quoiiii , chị đẹpppppp
def rule51(sentence,sent_dict,rule_firing):
  label= rule_dict[51]
  s=sentence.lower()
  pattern= re.compile(r"\b(đẹp+p+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
        
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex2686	trương gia nghê xinh xỉuuu
def rule52(sentence,sent_dict,rule_firing):
  label= rule_dict[52]
  s=sentence.lower()
  pattern= re.compile(r"\b(xỉu+u+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
        
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing
#Ex2696	đang đúng tự nhiên sai xong cái đi tù xuuuuuuuuuuu
def rule53(sentence,sent_dict,rule_firing):
  label= rule_dict[53]
  s=sentence.lower()
  pattern= re.compile(r"\b(xu+u+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
        
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex2819	là vuii dữ chưa dạaaaa
def rule54(sentence,sent_dict,rule_firing):
  label= rule_dict[54]
  s=sentence.lower()
  pattern= re.compile(r"\b(dạ+a+|dà+a+|dợ+o+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
        
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

def rule55(sentence,sent_dict,rule_firing):
  label= rule_dict[55]
  s=sentence.lower()
  pattern= re.compile(r"\b(vui+i+|dui+i+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
        
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex3043	game củ c , 1 ngày chơi 4 5 tiếng , cả tháng trời ddeoooo quaaa
def rule56(sentence,sent_dict,rule_firing):
  label= rule_dict[56]
  s=sentence.lower()
  pattern= re.compile(r"\b(đéo+o+|éo+o+|d+eo+o+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
        
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

def rule57(sentence,sent_dict,rule_firing):
  label= rule_dict[57]
  s=sentence.lower()
  pattern= re.compile(r"\b(qua+a+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
        
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex3052	biết đou ngiu còn đang đi họcccc :))))
def rule58(sentence,sent_dict,rule_firing):
  label= rule_dict[58]
  s=sentence.lower()
  pattern= re.compile(r"\b(học+c+|hoc+c+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
        
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex3188	năn nỉ đeo kính dùmmmmm
def rule59(sentence,sent_dict,rule_firing):
  label= rule_dict[59]
  s=sentence.lower()
  pattern= re.compile(r"\b(dùm+m+|giùm+m+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
        
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex3218	công nhận chipu đẹp gheee
#Ex3323	hướng nội gkee nhát gkeee
def rule60(sentence,sent_dict,rule_firing):
  label= rule_dict[60]
  s=sentence.lower()
  pattern= re.compile(r"\b(ghe+e+|ghê+e+|gke+e+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
        
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex3374	t thích viết bút lông quá trờyyy =))))))
def rule61(sentence,sent_dict,rule_firing):
  label= rule_dict[61]
  s=sentence.lower()
  pattern= re.compile(r"\b(tr+|trời+i+|chời+i+|chòi+i+|chài+i+|trờy+y+|tròi+i+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
        
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex3523	nữ thần thanh xuân , hoa khôi giảng đường , nam thần của các trái tim , tổng tài siêu cấp đẹp trai là coá thậtttt
def rule62(sentence,sent_dict,rule_firing):
  label= rule_dict[62]
  s=sentence.lower()
  pattern= re.compile(r"\b(có+o+|có+a+|coá+|coá+a+|kó+o+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex4478	anh rất tểnh và đẹp zaiii
def rule63(sentence,sent_dict,rule_firing):
  label= rule_dict[63]
  s=sentence.lower()
  pattern= re.compile(r"\b(zai+i+|trai+i+|zoai+i+|troai+i+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex4820	tới bsi còn ngạc nhiên lunn màaa
def rule64(sentence,sent_dict,rule_firing):
  label= rule_dict[64]
  s=sentence.lower()
  pattern= re.compile(r"\b(mà+a+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex4912	hạnh phúc đến phát khok
def rule65(sentence,sent_dict,rule_firing):
  label= rule_dict[65]
  s=sentence.lower()
  pattern= re.compile(r"\b(khóc+c+|khoc+c+|khók+k+|kho+k+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex4950	thiệt sự á tr cảm ơn lắmmm :))
def rule66(sentence,sent_dict,rule_firing):
  label= rule_dict[66]
  s=sentence.lower()
  pattern= re.compile(r"\b(lắm+m+|nhắm+m+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex4967	ăn hoài không mập ra ghecccccc
def rule67(sentence,sent_dict,rule_firing):
  label= rule_dict[67]
  s=sentence.lower()
  pattern= re.compile(r"\b(ghét+t+|ghéc+c+|ghet+t+|ghec+c+|ghék+k+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex5017	mãi ko baoh quênnnn
def rule68(sentence,sent_dict,rule_firing):
  label= rule_dict[68]
  s=sentence.lower()
  pattern= re.compile(r"\b(quên+n+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex5137	phiên bản của màiii nàaa xinh zữ chòi mừi một điểm lunn
def rule69(sentence,sent_dict,rule_firing):
  label= rule_dict[69]
  s=sentence.lower()
  pattern= re.compile(r"\b(mày+y+|mà+i+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

def rule70(sentence,sent_dict,rule_firing):
  label= rule_dict[70]
  s=sentence.lower()
  pattern= re.compile(r"\b(nè+e+|nà+a+|nì+i|ne+e+|ni+i+|nè+k+|ne+k+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex5423	khum aiii bth khi êo
def rule71(sentence,sent_dict,rule_firing):
  label= rule_dict[71]
  s=sentence.lower()
  pattern= re.compile(r"\b(ai+i+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex5588	trứng đòi khôn hơn vịtttttt
def rule72(sentence,sent_dict,rule_firing):
  label= rule_dict[72]
  s=sentence.lower()
  pattern= re.compile(r"\b(vịt+t+|dịt+t+|dzịt+t+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex5799	tao đã đọc lại thì mài cũm vạiiii
def rule73(sentence,sent_dict,rule_firing):
  label= rule_dict[73]
  s=sentence.lower()
  pattern= re.compile(r"\b(vậy+y+|vại+i+|zậy+y+|dzậy+y+|dzại+i+|dzị+|z+ị+|z+|zạy+y+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex5848	đại bàng gọi chim xẻ trả lờiii
def rule74(sentence,sent_dict,rule_firing):
  label= rule_dict[74]
  s=sentence.lower()
  pattern= re.compile(r"\b(lời+i+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex6088	:))) nhạc lênnn nước mắt tuôn gơi
def rule75(sentence,sent_dict,rule_firing):
  label= rule_dict[75]
  s=sentence.lower()
  pattern= re.compile(r"\b(lên+n+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing

#Ex846	vẫn còn hiền quá , đọc mà tứk á
def rule76(sentence,sent_dict,rule_firing):
  label= rule_dict[76]
  s=sentence.lower()
  pattern= re.compile(r"\b(tức+c+|tứk+)\b")
  r=re.finditer(pattern,s)
  for match in r:
    start=match.start()
    end=match.end()
    for key in sent_dict.keys():
      if key in range(start,end):
          rule_firing[sent_dict[key]]=label2class[label]
  return rule_firing 
  
# Define a list to store the functions
rule_list = []

# Iterate over the function names
for i in range(76):  # Assuming you have functions named from rule0 to rule50
    function_name = f"rule{i}"  # Generate function name
    if function_name in globals():  # Check if the function exists
        function = globals()[function_name]  # Get the function object
        rule_list.append(function)  # Add the function to the list

num_rules=len(rule_list)

def regrex_rule(sentence, sentence_lst, rule_lst=rule_list):
  sent_dict = get_sent_dict(sentence_lst)
  for rule_id, rule in enumerate(rule_lst):     
     new_sent = rule(sentence, sent_dict, sentence_lst)
  return new_sent

def dictionary_rule(sentence, sentence_lst, dictionary):
  for i, token in enumerate(sentence_lst):
      if token in dictionary:
         if len(dictionary[token]) == 1:
            sentence_lst[i] = dictionary[token][0]
  return sentence_lst
         