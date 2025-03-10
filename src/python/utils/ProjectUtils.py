import os
import json
import pathlib
# from gensim.models import KeyedVectors


def get_root_dir_path():
    return pathlib.Path(__file__).parent.parent.parent.parent.resolve()


def get_pubmed_json_data_path():
    return os.path.join(get_root_dir_path(), 'data', 'pubmed_data.json')


def get_preprocessed_pubmed_json_data_path():
    return os.path.join(get_root_dir_path(), 'data', 'preprocessed_pubmed_data.json')
 

def load_preprocessed_pubmed_data():
    path = get_preprocessed_pubmed_json_data_path()
    with open(path, 'r') as file:
        return json.load(file)


def get_embeddings_path(model_id):
    return os.path.join(get_root_dir_path(), 'data', 'embeddings', f'embeddings_{model_id}.json')


def load_word2vec_embeddings():
    root_path = get_root_dir_path()
    embedding_path = os.path.join(root_path, 'data', 'word-2-vec-model', 'word2vec-google-news-300.gz')
    model = KeyedVectors.load_word2vec_format(embedding_path, binary=True)
    return model
