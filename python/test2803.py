import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
import re
import jamotools


# 조선왕조실록 데이터 파일 다운로드
train_file = tf.keras.utils.get_file('./tmp/input.txt', 'http://bit.ly/2Mc3SOV')

# 데이터를 메모리에 불러옵니다. encoding 형식으로 utf-8 을 지정해야합니다.
train_text = open(train_file, 'rb').read().decode(encoding='utf-8')

# 텍스트가 총 몇 자인지 확인합니다.
print(f'Length of text: {len(train_text)} characters')

# 처음 100 자를 확인해봅니다.
print(train_text[:100])

# 훈련 데이터 입력 정제
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


train_text = train_text.split('\n')
train_text = [clean_str(sentence) for sentence in train_text]
x_train = []

for sentence in train_text:
    x_train.extend(sentence.split(' '))
    x_train.append('\n')

x_train = [word for word in x_train if word != '']
print(x_train[:20])

# 단어를 토큰화해서 set로
vocab = sorted(set(x_train))
vocab.append('UNK')
print(f'{len(vocab)} unique words')

# vocab list를 숫자로 매핑하고, 반대도 실행
word2idx = {u: i for i, u in enumerate(vocab)}
idx2word = np.array(vocab)

text_as_int = np.array([word2idx[c] for c in x_train])

# word2idx 의 일부를 알아보기 쉽게 print
print('{')

for word, _ in zip(word2idx, range(10)):
    print('  {:4s}: {:3d},'.format(repr(word), word2idx[word]))

print('  ...\n}')
print('index of UNK: {}'.format(word2idx['UNK']))

# 토큰 데이터 확인
print(x_train[:20])
print(text_as_int[:20])

# 기본 데이터셋 만들기
seq_length = 25
examples_per_epoch = len(text_as_int) // seq_length
sentence_dataset = tf.data.Dataset.from_tensor_slices(text_as_int)
sentence_dataset = sentence_dataset.batch(seq_length+1, drop_remainder=True)

for item in sentence_dataset.take(1):
    print(idx2word[item.numpy()])
    print(item.numpy())

# 학습 데이터셋 만들기


def split_input_target(chunk):
    return [chunk[:-1], chunk[-1]]


train_dataset = sentence_dataset.map(split_input_target)

for x, y in train_dataset.take(1):
    print(idx2word[x.numpy()])
    print(x.numpy())
    print(idx2word[y.numpy()])
    print(y.numpy())

# 데이터셋 shuffle, batch 설정
BATCH_SIZE = 512
steps_per_epoch = examples_per_epoch // BATCH_SIZE
BUFFER_SIZE = 10000

train_dataset = train_dataset.shuffle(BUFFER_SIZE).batch(BATCH_SIZE, drop_remainder=True)

# 단어 단위 생성 모델 정의
total_words = len(vocab)

model = tf.keras.Sequential([
    tf.keras.layers.Embedding(total_words, 100, input_length=seq_length),
    tf.keras.layers.LSTM(units=100, return_sequences=True),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.LSTM(units=100),
    tf.keras.layers.Dense(total_words, activation='softmax')])

model.compile(
    optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.summary()

# 단어 단위 생성 모델 학습


def testmodel(epoch, logs):
    if epoch % 5 != 0 and epoch != 49:
        return

    test_sentence = train_text[0]
    next_words = 100

    for _ in range(next_words):
        test = test_sentence.split(' ')[-seq_length:]
        test = np.array(
            [word2idx[c] if c in word2idx else word2idx['UNK'] for c in test])
        test = tf.keras.preprocessing.sequence.pad_sequences(
            [test], maxlen=seq_length, padding='pre', value=word2idx['UNK'])
        output_idx = model.predict_classes(test)
        test_sentence += ' ' + idx2word[output_idx[0]]

    print(test_sentence)


testmodelcb = tf.keras.callbacks.LambdaCallback(on_epoch_end=testmodel)
history = model.fit(train_dataset.repeat(), epochs=50,
    steps_per_epoch=steps_per_epoch, callbacks=[testmodelcb], verbose=2)

model.save('lang.h5')
model = tf.keras.models.load_model(
    './lang.h5', custom_objects=None, compile=True)
print(model.summary())

test_sentence = '동헌에 나가 공무를 본 후 활 십오 순을 쏘았다'
test_sentence = jamotools.split_syllables(test_sentence)

next_chars = 300
char2idx = {u: i for i, u in enumerate(vocab)}

for _ in range(next_chars):
    test = test_sentence[-seq_length:]
    test = np.array(
        [char2idx[c] if c in char2idx else char2idx['UNK'] for c in test])
    test = tf.keras.preprocessing.sequence.pad_sequences(
        [test], maxlen=seq_length, padding='pre', value=char2idx['UNK'])

    output_idx = model.predict_classes(test)
    test_sentence += idx2word[output_idx[0]]

print(jamotools.join_jamos(test_sentence))
