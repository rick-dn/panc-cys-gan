import pandas as pd

import tensorflow as tf
import tensorflow_hub as hub

import tensorflow_text as text

from bert_model_selection import bert_model_selection

csv_file = '../../datasets/SMSSpamCollection'
df= pd.read_csv(csv_file, sep='t', names=['label', 'message'])
print(df.head())

df.rename(columns = {'label':'Category', 'message':'Message'}, inplace = True)
print(df.head())

df['spam']=df['Category'].apply(lambda x: 1 if x=='spam' else 0)
print(df.head())

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df['Message'],df['spam'], stratify=df['spam'])
X_train.head(4)


bert_model_name = 'small_bert/bert_en_uncased_L-4_H-512_A-8'

tfhub_handle_encoder, tfhub_handle_preprocess =bert_model_selection(bert_model_name=bert_model_name)

bert_preprocess_model = hub.KerasLayer(tfhub_handle_preprocess)


print('bert encode: ')
bert_encoder = hub.KerasLayer(tfhub_handle_encoder)

print('bert preprocess: ')
bert_preprocess = hub.KerasLayer(tfhub_handle_preprocess)


# Bert layers
text_input = tf.keras.layers.Input(shape=(), dtype=tf.string, name='text')
preprocessed_text = bert_preprocess(text_input)
outputs = bert_encoder(preprocessed_text)
# Neural network layers
l = tf.keras.layers.Dropout(0.1, name="dropout")(outputs['pooled_output'])
l = tf.keras.layers.Dense(1, activation='sigmoid', name="output")(l)
# Use inputs and outputs to construct a final model
model = tf.keras.Model(inputs=[text_input], outputs = [l])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=2, batch_size=32)

y_predicted = model.predict(X_test)
y_predicted = y_predicted.flatten()
print(y_predicted)

