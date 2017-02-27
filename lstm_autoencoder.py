import tensorflow as tf
import numpy as np

onehot_tok_idx_en = np.load('data/onehot_tok_idx_en.npy').item()
onehot_tok_idx_fr = np.load('data/onehot_tok_idx_fr.npy').item()

sent_en = np.load('data/sent_en.npy').item()
sent_fr = np.load('data/sent_fr.npy').item()

# Build LSTM graph

vocab_size = len(onehot_tok_idx_fr)
num_layers = 8
num_steps = 2000
hidden_size = 500


# def length(sequence):
#     used = tf.sign(tf.reduce_max(tf.abs(sequence), reduction_indices=2))
#     length = tf.reduce_sum(used, reduction_indices=1)
#     length = tf.cast(length, tf.int32)
#     return length

# x = tf.placeholder("float16", shape=[
#                    None, num_steps, vocab_size], name="x_placeholder")
# y = tf.placeholder("float16", shape=[None, num_outputs], name="y_placeholder")

# weights = tf.Variable(tf.truncated_normal(
#     [hidden_size, num_outputs], stddev=0.05, dtype=tf.float16))
# bias = tf.Variable(tf.constant(.1, shape=[num_outputs], dtype=tf.float16))

# lstm = tf.contrib.rnn.BasicLSTMCell(
#     hidden_size, forget_bias=0.0, state_is_tuple=True)
# stacked_lstm = tf.contrib.rnn.MultiRNNCell(
#     [lstm] * num_layers, state_is_tuple=True)

# outputs, state = tf.contrib.legacy_seq2seq.embedding_rnn_seq2seq(
#     encoder_inputs=x, decoder_inputs=x, cell=stacked_lstm, num_encoder_symbols=vocab_size, num_decoder_symbols=vocab_size, embedding_size=1000, output_projection=None, feed_previous=False,dtype=tf.float16)

# # outputs = tf.transpose(outputs, [1,0,2])
# # last = tf.gather(outputs, num_steps - 1)
# # y_pred = tf.nn.softmax(tf.matmul(last, weights) + bias)
# outputs = tf.reduce_mean(outputs, 1)
# y_pred = tf.nn.softmax(tf.matmul(outputs, weights) + bias)

# cross_entropy = tf.reduce_mean(
#     tf.nn.softmax_cross_entropy_with_logits(logits=y_pred, labels=y))
# optimizer = tf.train.AdamOptimizer(
#     learning_rate=learning_rate).minimize(cross_entropy)

# correct_pred = tf.equal(tf.argmax(y_pred, 1), tf.argmax(y, 1))
# accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

