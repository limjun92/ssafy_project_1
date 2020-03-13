# from konlpy.tag import Kkma
# from konlpy.utils import pprint

from konlpy.tag import Hannanum
hannanum = Hannanum() 
 
# hannanum.analyze  #구(Phrase) 분석
# hannanum.morphs   #형태소 분석
# hannanum.nouns    #명사 분석
# hannanum.pos      #형태소 분석 태깅

print(hannanum.analyze(u'롯데마트의 흑마늘 양념 치킨이 논란이 되고 있다.'))
print(hannanum.morphs(u'롯데마트의 흑마늘 양념 치킨이 논란이 되고 있다.'))
print(hannanum.nouns(u'다람쥐 헌 쳇바퀴에 타고파'))
print(hannanum.pos(u'웃으면 더 행복합니다!'))

# kkma = Kkma()
# pprint(kkma.sentences(u'네, 안녕하세요. 반갑습니다.'))
# pprint(kkma.nouns(u'질문이나 건의사항은 깃헙 이슈 트래커에 남겨주세요.'))
# pprint(kkma.pos(u'오류보고는 실행환경, 에러메세지와함께 설명을 최대한상세히!^^'))

