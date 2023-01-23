import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()

x_data = x_train.reshape(-1, 28, 28, 1) / 255.0 # np.expand_dims(x_train, -1)
y_data = y_train
test = x_test.reshape(-1, 28, 28, 1) / 255.0
true = y_test
num = len(set(y_train))

fashion_mnist_model = tf.keras.Sequential()
fashion_mnist_model.add(tf.keras.layers.Conv2D(64, kernel_size=(3,3),
    activation='relu', input_shape=(28,28,1)))
fashion_mnist_model.add(tf.keras.layers.MaxPooling2D(pool_size=(2,2)))
fashion_mnist_model.add(tf.keras.layers.Conv2D(128, kernel_size=(3,3),
    activation='relu'))
fashion_mnist_model.add(tf.keras.layers.MaxPooling2D(pool_size=(2,2)))
fashion_mnist_model.add(tf.keras.layers.Flatten())
fashion_mnist_model.add(tf.keras.layers.Dense(100, activation='relu'))
fashion_mnist_model.add(tf.keras.layers.Dense(num, activation='softmax'))

fashion_mnist_model.compile(loss='sparse_categorical_crossentropy', optimizer='Adam', metrics=['accuracy'])
fashion_mnist_model.fit(x_data, y_data, batch_size=100, epochs=5)

print(fashion_mnist_model.layers)
print(fashion_mnist_model.layers[0].name)
print(fashion_mnist_model.layers[0].output)

layer_outputs = [layer.output for layer in fashion_mnist_model.layers[:4]]
print(layer_outputs)

activation_model = tf.keras.models.Model(inputs=fashion_mnist_model.input, outputs=layer_outputs)

# 예를 들어 2번째 이미지를 갖고 온다면
#image = np.expand_dims(x_train[2], axis=0)
#print(image.shape)
image = x_train[2].reshape(-1, 28, 28, 1) / 255.0
activations = activation_model.predict(image)

print(len(activations))

for i in range(4):
    print(activations[i].shape, activations[i].ndim)
    plt.matshow(activations[i][0, :, :, 0])
    plt.title('layer %d' % i)
    plt.show()

layer = 0
n_feature = activations[layer].shape[-1]

for i in range(n_feature):
    plt.matshow(activations[layer][0, :, :, i])
    plt.title("layer % d activation %d" % (layer, i))
    plt.show()


layer_names = []
for layer in fashion_mnist_model.layers[:4]:
    layer_names.append(layer.name)

images_per_row = 16

for layer_name, layer_activation in zip(layer_names, activations):
    n_features = layer_activation.shape[-1]

    # 특성 맵의 크기는 (1, size, size, n_features)
    size = layer_activation.shape[1]

    # 활성화 채널을 위한 그리드 크기
    n_cols = n_features // images_per_row
    display_grid = np.zeros((size * n_cols, images_per_row * size))

    # 각 활성화를 하나의 큰 그리드로
    for col in range(n_cols):
        for row in range(images_per_row):
            channel_image = layer_activation[0, :, :, col * images_per_row + row]
            # 그래프로 나타내기 좋게 특성처리
            channel_image -= channel_image.mean()
            channel_image /= channel_image.std()
            channel_image *= 64
            channel_image += 128
            channel_image = np.clip(channel_image, 0, 255).astype('uint8')
            display_grid[col * size : (col + 1) * size,
                         row * size : (row + 1) * size] = channel_image

    # 그리드 출력
    scale = 1. / size
    plt.figure(figsize=(scale * display_grid.shape[1],
                        scale * display_grid.shape[0]))
    plt.title(layer_name)
    plt.grid(False)
    plt.imshow(display_grid, aspect='auto', cmap='viridis')
    plt.show()


