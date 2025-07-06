import os
import pandas as pd
from email.parser import BytesParser
from email import policy

def parse_email(filepath):
    with open(filepath, "rb") as f:
        msg = BytesParser(policy=policy.default).parse(f)
    return {
        "subject": msg.get("Subject", ""),
        "from": msg.get("From", ""),
        "body": msg.get_body(preferencelist=("plain", "html")).get_content(),
        "is_phishing": 0  # Default label (update later)
    }

def process_emails(base_path="data/raw/maildir", output_csv="data/processed/enron_emails.csv"):
    emails = []
    for root, _, files in os.walk(base_path):
        for file in files:
            filepath = os.path.join(root, file)
            try:
                emails.append(parse_email(filepath))
            except Exception as e:
                print(f"Skipping {filepath}: {e}")
    
    pd.DataFrame(emails).to_csv(output_csv, index=False)
    print(f"Saved {len(emails)} emails to {output_csv}")

if __name__ == "__main__":
    process_emails()  # Run this to generate the CSV