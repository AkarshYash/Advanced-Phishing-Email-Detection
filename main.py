import sys
import os
from pathlib import Path

# ================================================
# ABSOLUTE PATH SOLUTION (GUARANTEED TO WORK)
# ================================================
# 1. Define ABSOLUTE path to your project
PROJECT_ROOT = Path(r"C:\Users\chatu\OneDrive\Desktop\email test")

sys.path.insert(0, str(PROJECT_ROOT))  # Highest priority
os.environ['PYTHONPATH'] = str(PROJECT_ROOT)  # Environment variable

# ================================================
# DEBUGGING OUTPUT (SHOWS EXACT PROBLEM)
# ================================================
print(f"\n=== SYSTEM DIAGNOSTICS ===")
print(f"Working directory: {os.getcwd()}")
print(f"Project root: {PROJECT_ROOT}")
print(f"Python path: {sys.path}")
print(f"Data folder exists: {os.path.exists(PROJECT_ROOT/'data')}")
if os.path.exists(PROJECT_ROOT/'data'):
    print(f"Data folder contents: {os.listdir(PROJECT_ROOT/'data')}")

# ================================================
# SAFE IMPORT WITH VALIDATION
# ================================================
try:
    # Attempt absolute import
    from data.load_dataset import load_training_data
    print("\nSUCCESS: Module imported successfully!")
except ImportError as e:
    print(f"\nFAILED: {e}")
    print("\nTROUBLESHOOTING GUIDE:")
    print("1. CONFIRM these files exist:")
    print(f"   - {PROJECT_ROOT/'data/__init__.py'}")
    print(f"   - {PROJECT_ROOT/'data/load_dataset.py'}")
    print("2. Verify:")
    print("   - No typos in file/folder names")
    print("   - Files are not empty")
    print("3. Try these commands:")
    print(f"   cd {PROJECT_ROOT}")
    print("   python -c \"from data.load_dataset import load_training_data; print('Direct import works!')\"")
    raise

# ================================================
# YOUR APPLICATION CODE
# ================================================
def main():
    print("\nApplication started successfully!")
    # Your code here...

if __name__ == '__main__':
    main()