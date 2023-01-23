import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
import re


# Naver Sentiment Movie Corpus v1.0 다운로드
train_file = tf.keras.utils.get_file(
    './tmp/train.txt', 'https://raw.githubusercontent.com/e9t/nsmc/master/ratings_train.txt')
test_file = tf.keras.utils.get_file(
    './tmp/test.txt', 'https://raw.githubusercontent.com/e9t/nsmc/master/ratings_test.txt')

# 데이터를 메모리에 불러옵니다. encoding 형식으로 utf-8 을 지정해야합니다.
train_text = open(train_file, 'rb').read().decode(encoding='utf-8')
test_text = open(test_file, 'rb').read().decode(encoding='utf-8')

# 텍스트가 총 몇 자인지 확인합니다.
print(f'Length of train text: {len(train_text)} characters')
print(f'Length of test text: {len(test_text)} characters')

# 처음 300 자를 확인해봅니다.
print(train_text[:300])

# 학습을 위한 정답 데이터(Y) 만들기
y_train = np.array([[int(row.split('\t')[2])] for row in train_text.split('\n')[1:]
                    if row.count('\t') > 0])
y_test = np.array([[int(row.split('\t')[2])] for row in test_text.split('\n')[1:]
                   if row.count('\t') > 0])

print(y_train.shape, y_test.shape)
print(y_train[:5])

# train 데이터의 입력에 대한 정제
# From https://github.com/yoonkim/CNN_sentence/blob/master/process_data.py


def clean_str(string):
    string = re.sub(r"[^가-힣A-Za-z0-9(),!?\'\`]", " ", string)
    string = re.sub(r"\'s", " \'s", string)
    string = re.sub(r"\'ve", " \'ve", string)
    string = re.sub(r"n\'t", " n\'t", string)
    string = re.sub(r"\'re", " \'re", string)
    string = re.sub(r"\'d", " \'d", string)
    string = re.sub(r"\'ll", " \'ll", string)
    string = re.sub(r",", " , ", string)
    string = re.sub(r"!", " ! ", string)
    string = re.sub(r"\(", " \( ", string)
    string = re.sub(r"\)", " \) ", string)
    string = re.sub(r"\?", " \? ", string)
    string = re.sub(r"\s{2,}", " ", string)
    string = re.sub(r"\'{2,}", "\'", string)
    string = re.sub(r"\'", "", string)

    return string.lower()


x_train = [row.split('\t')[1] for row in train_text.split('\n')[1:]
           if row.count('\t') > 0]
x_train = [clean_str(sentence) for sentence in x_train]

# 문장을 띄어쓰기 단위로 단어 분리
sentences = [sentence.split(' ') for sentence in x_train]

for i in range(5):
    print(sentences[i])

# 단어 정제 및 문장 길이 줄임
sentences_new = []

for sentence in sentences:
    sentences_new.append([word[:5] for word in sentence][:25])

sentences = sentences_new

for i in range(5):
    print(sentences[i])

# Tokenizer와 pad_sequences를 사용한 문장 전처리
tokenizer = tf.keras.preprocessing.text.Tokenizer(num_words=20000)
tokenizer.fit_on_texts(sentences)
x_train = tokenizer.texts_to_sequences(sentences)
x_train = tf.keras.preprocessing.sequence.pad_sequences(
    x_train, padding='post')

print(x_train[:5])

# 감성 분석을 위한 모델 정의
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(20000, 300, input_length=25),
    tf.keras.layers.LSTM(units=50),
    tf.keras.layers.Dense(2, activation='softmax')])

model.compile(
    optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
print(model.summary())

# 감성 분석 모델 학습
history = model.fit(x_train, y_train, epochs=5, batch_size=128, validation_split=0.2)

# 테스트 데이터 평가
test = [row.split('\t')[1] for row in test_text.split('\n')[1:]
        if row.count('\t') > 0]
test = [clean_str(sentence) for sentence in test]
sentences = [sentence.split(' ') for sentence in test]
sentences_new = []

for sentence in sentences:
    sentences_new.append([word[:5] for word in sentence][:25])

sentences = sentences_new

x_test = tokenizer.texts_to_sequences(sentences)
x_test = tf.keras.preprocessing.sequence.pad_sequences(x_test, padding='post')

model.evaluate(x_test, y_test, verbose=0)

# 임의의 문장 감성 분석 결과 확인
test_sentence = '엘론 머스크 영화는 너무 재미 없었다'
test_sentence = test_sentence.split(' ')

test_sentences = []
now_sentence = []

for word in test_sentence:
    now_sentence.append(word)
    test_sentences.append(now_sentence[:])

x_test_1 = tokenizer.texts_to_sequences(test_sentences)
x_test_1 = tf.keras.preprocessing.sequence.pad_sequences(
    x_test_1, padding='post', maxlen=25)
predict = model.predict(x_test_1)

for idx, sentence in enumerate(test_sentences):
    print(sentence)
    print(predict[idx])
