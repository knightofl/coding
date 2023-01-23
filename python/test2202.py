import numpy as np
import tensorflow as tf

a = tf.constant(1)
print(a)

b = tf.constant([1, 2, 3])
print(b)

c = tf.constant([[1, 2, 3], [4, 5, 6]])
print(c)

print(a.shape, b.shape, c.shape)
print(a.get_shape(), b.get_shape(), c.get_shape())

print(tf.rank(a), tf.rank(b), tf.rank(c))

print(b[0])

print(c[0])
print(c[0].shape)

print(c[1, :])
print(c[:1, :])

print(c[:1, :, tf.newaxis])
print(c[tf.newaxis, :1, :])

print(c, tf.transpose(c))
print(c@tf.transpose(c))

print(tf.Variable(np.random.normal(size=(2,3))))