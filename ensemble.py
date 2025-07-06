# models/ensemble.py
import pickle
import pandas as pd
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from config import MODEL_PATHS, SCORE_THRESHOLDS

class PhishingDetector:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(max_features=1000)
        self.model = RandomForestClassifier()
    
    def train(self, X, y):
        X_vec = self.vectorizer.fit_transform(X)
        self.model.fit(X_vec, y)
    
    def predict_with_score(self, emails):
        probabilities = self.model.predict_proba(
            self.vectorizer.transform(emails))
        scores = [self._probability_to_score(p[1]) for p in probabilities]
        predictions = self.model.predict(
            self.vectorizer.transform(emails))
        return list(zip(predictions, scores))
    
    def _probability_to_score(self, probability):
        if probability >= SCORE_THRESHOLDS['high_risk']:
            return min(10, int(8 + (probability - 0.8) * 10))
        elif probability >= SCORE_THRESHOLDS['medium_risk']:
            return min(8, int(5 + (probability - 0.5) * 10))
        else:
            return max(1, int(1 + probability * 8))
    
    def save_models(self):
        Path(MODEL_PATHS['vectorizers']['text']).parent.mkdir(exist_ok=True)
        with open(MODEL_PATHS['vectorizers']['text'], 'wb') as f:
            pickle.dump(self.vectorizer, f)
        with open(MODEL_PATHS['ensemble'], 'wb') as f:
            pickle.dump(self.model, f)
    
    @classmethod
    def load_models(cls):
        detector = cls()
        with open(MODEL_PATHS['vectorizers']['text'], 'rb') as f:
            detector.vectorizer = pickle.load(f)
        with open(MODEL_PATHS['ensemble'], 'rb') as f:
            detector.model = pickle.load(f)
        return detector