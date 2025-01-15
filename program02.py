import urllib.request
import pickle
from soynlp import DoublespaceLineCorpus
from soynlp.word import WordExtractor
from soynlp.tokenizer import LTokenizer

# 트레이닝 데이터 내려 받기
# urllib.request.urlretrieve('https://raw.githubusercontent.com/lovit/soynlp/master/tutorials/2016-10-20.txt', filename='data_train.txt')

data_train = DoublespaceLineCorpus('data_train.txt')
# print(len(data_train))
# print(type(data_train))

# 트레이닝 실행 및 파일로 저장.
model = WordExtractor()
model.train(data_train)
# model.save('./resources/my_model.model')


# 응집확률 기반 토크나이저 
word_score_table = model.extract()
scores = {word:score.cohesion_forward for word, score in word_score_table.items()} 
tokenizer = LTokenizer(scores=scores)
with open('./resources/my_tokenizer1.model','wb') as f:
    pickle.dump(tokenizer,f)

# 분기엔트로피 기반 토크나이저
scores = {word:score.right_branching_entropy for word, score in word_score_table.items()}        # 분기엔트로피를 score로 사용.
tokenizer = LTokenizer(scores=scores)

with open('./resources/my_tokenizer2.model','wb') as f:
    pickle.dump(tokenizer,f)

# 응집확률 * 분기엔트로피 기반 토크나이저 
scores = {word:score.cohesion_forward*score.right_branching_entropy for word, score in word_score_table.items()}     
tokenizer = LTokenizer(scores=scores)

with open('./resources/my_tokenizer3.model','wb') as f:
    pickle.dump(tokenizer,f)