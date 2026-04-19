import re

text = "Hello! Welcome to @FiyaSmartFinds. Are you ready for Python??"

# Lowercase karna aur special characters hatana
clean_text = re.sub(r'[^a-zA-Z0-9\s]', '', text).lower()

print(f"Original: {text}")
print(f"Cleaned: {clean_text}")
