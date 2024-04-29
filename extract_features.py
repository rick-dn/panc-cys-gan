import os
import shutil

import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_text as text

from bert_model_selection import bert_model_selection

tf.get_logger().setLevel('ERROR')

# url = 'https://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz'
#
# dataset = tf.keras.utils.get_file('aclImdb_v1.tar.gz', url,
#                                   untar=True, cache_dir='.',
#                                   cache_subdir='')
#
# dataset_dir = os.path.join(os.path.dirname(dataset), 'aclImdb')
#
# train_dir = os.path.join(dataset_dir, 'train')
#
# # remove unused folders to make it easier to load the data
# remove_dir = os.path.join(train_dir, 'unsup')
# shutil.rmtree(remove_dir)

# text_input = ['je ne sui pa idiot asdf adsf asdf ']

bert_model_name = 'small_bert/bert_en_uncased_L-4_H-512_A-8'

tfhub_handle_encoder, tfhub_handle_preprocess = bert_model_selection(bert_model_name=bert_model_name)

bert_preprocess_model = hub.KerasLayer(tfhub_handle_preprocess)

# print('bert output', bert_results.numpy().shape)


def extract_bert_features(text_inputs):

    bert_output = []
    for idx, text_input in enumerate(text_inputs):

        # if idx > 2:
        #     break
        print('processing row', idx)
        text_preprocessed = bert_preprocess_model([text_input])
        # text_preprocessed = bert_preprocess_model([text_input[0]])

        bert_model = hub.KerasLayer(tfhub_handle_encoder)
        bert_result = bert_model(text_preprocessed)

        # print(f'Keys       : {list(text_preprocessed.keys())}')
        # print(f'Shape      : {text_preprocessed["input_word_ids"].shape}')
        # print(f'Word Ids   : {text_preprocessed["input_word_ids"][0, :12]}')
        # print(f'Input Mask : {text_preprocessed["input_mask"][0, :12]}')
        # print(f'Type Ids   : {text_preprocessed["input_type_ids"][0, :12]}')

        # print(f'Loaded BERT: {tfhub_handle_encoder}')
        # print(f'Pooled Outputs Shape:{bert_result["pooled_output"].shape}')
        # print(f'Pooled Outputs Values:{bert_result["pooled_output"][0, :12]}')
        # print(f'Sequence Outputs Shape:{bert_result["sequence_output"].shape}')
        # print(f'Sequence Outputs Values:{bert_result["sequence_output"][0, :12]}')
        bert_output.append(bert_result['pooled_output'])

    return np.asarray(bert_output, dtype=np.float32)
