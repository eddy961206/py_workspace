import tensorflow as tf

tensor = tf.constant( [3.2,4,5] )
tensor2 = tf.constant( [6,7,8] )
tensor3 =  tf.constant([[1,2],
                    [3,4]])
tensor4 = tf.zeros([2,2,3])
# print(tf.add(tensor, tensor2))
# print(tensor * tensor2)
# print(tensor/tensor2)
# print(tf.matmul(tensor,tensor2))
# print(tensor4)
# print(tensor3.shape)
print(tensor)

w = tf.Variable(2.2)
print(w.numpy())
w.assign(3)
print(w)

