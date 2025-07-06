

# 📧 Email Detection & Feature Extractor  
**A Python tool for detecting email files and extracting key features (headers, content, attachments) with forensic capabilities.**  

![Python](https://img.shields.io/badge/Python-3.8%2B-blue) 
![License](https://img.shields.io/badge/License-MIT-green) 
![CLI](https://img.shields.io/badge/CLI-Yes-brightgreen)

---

## 🔍 **What This Tool Does**  
1. **Detects email files** (`.eml`, `.msg`, `.pst`) in directories  
2. **Extracts metadata**:  
   - Headers (From/To/Subject)  
   - Body content (plaintext/HTML)  
   - Attachments (with hash generation)  
3. **Forensic Mode**:  
   - IP extraction from headers  
   - DKIM/DMARC validation  
   - Timeline reconstruction  

---

## 🛠️ **Tech Stack**  
```python
├── email_analyzer.py       # Core extraction logic
├── file_scanner.py         # Filesystem traversal  
├── forensic_mode.py        # Advanced analysis  
├── utils/                  # Helpers (hashing, etc.)
└── tests/                  # Sample .eml files for testing
```

**Key Libraries**:  
- `email` (Python stdlib) - Parsing MIME emails  
- `olefile` - MSG file handling  
- `pypff` - PST file support *(optional)*  
- `tqdm` - Progress bars  

---

## 🚀 **Quick Start**  

### Installation  
```bash
git clone https://github.com/AkarshYash/Email-Detection-Feature-Extractor.git
cd Email-Detection-Feature-Extractor
pip install -r requirements.txt
```

### Basic Usage  
```bash
# Scan a directory for emails
python email_analyzer.py --input ./emails/ --output report.json

# Enable forensic mode
python email_analyzer.py --forensic --input suspect.eml
```

---

## 💡 **Features**  

### **1. Email Detection**  
- Supports: `.eml`, `.msg`, `.pst`  
- Recursive directory scanning  

### **2. Feature Extraction**  
| Feature          | Example Output |  
|------------------|----------------|  
| **Headers**      | `X-Originating-IP: 192.168.1.1` |  
| **Body Text**    | `Plaintext/HTML extracted` |  
| **Attachments**  | `invoice.pdf (SHA256: a1b2c3...)` |  

### **3. Forensic Mode**  
```python
{
  "sender_ip": "192.168.1.1",
  "dkim_verified": false,
  "received_chain": [
    "2023-01-01 12:00:00 - Received by mail.server.com"
  ]
}
```



---

## 🤝 **Contributing**  
1. Fork the repository  
2. Add tests for new features  
3. Submit a PR with clear documentation  
