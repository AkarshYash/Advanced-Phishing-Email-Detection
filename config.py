MODEL_PATHS = {
    'bert': 'data/models/bert_model',
    'ensemble': 'data/models/ensemble_model.pkl',
    'vectorizers': {
        'text': 'data/models/text_vectorizer.pkl',
        'url': 'data/models/url_vectorizer.pkl'
    }
}

SCORE_THRESHOLDS = {
    'high_risk': 0.8,
    'medium_risk': 0.5,
    'low_risk': 0.2
}