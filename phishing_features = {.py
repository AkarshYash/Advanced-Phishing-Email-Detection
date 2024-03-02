phishing_features = {
    'contains_http': 'http' in email_text,
    'contains_https': 'https' in email_text,
    'contains_at': '@' in email_text,
    'contains_dot': '.' in email_text,
    'contains_dollar': '$' in email_text,
    'contains_exclamation': '!' in email_text,
    'contains_question': '?' in email_text,
    'contains_percent': '%' in email_text,
    'contains_number': any(char.isdigit() for char in email_text),
    'word_count': len(words),
    'avg_word_length': sum(len(word) for word in words) / len(words)
}

phishing_proba = sum(1 for feature in phishing_features.values() if feature) / len(phishing_features)

return phishing_proba > 0.5