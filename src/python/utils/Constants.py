# QDRANT_DATABASE_CONNECTION_STRING = "http://db:6333"
QDRANT_DATABASE_CONNECTION_STRING = 'http://qdrant-service:6333'

GEMINI_API_KEY = 'AIzaSyD3TNFRihgFWBehAtmsuTs9yYQ3VBWx95k'


COLLECTIONS = {
    'gemini-2000-cosine': {
        'embedding_size': 768,
        'model_id': '01'
    },
    'gemini-2000-euclidean': {
        'embedding_size': 768,
        'model_id': '02'
    },
    'gemini-760-cosine': {
        'embedding_size': 768,
        'model_id': '03'
    },
    'gemini-760-euclidean': {
        'embedding_size': 768,
        'model_id': '04'
    },
    'word2vec-2000-cosine': {
        'embedding_size': 300,
        'model_id': '05'
    },
    'word2vec-2000-euclidean': {
        'embedding_size': 300,
        'model_id': '06'
    },
    'word2vec-760-cosine': {
        'embedding_size': 300,
        'model_id': '07'
    },
    'word2vec-760-euclidean': {
        'embedding_size': 300,
        'model_id': '08'
    }
}
