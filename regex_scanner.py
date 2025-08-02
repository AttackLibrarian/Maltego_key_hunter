import re

# Define target patterns
PATTERNS = [
    re.compile(r'\b[A-Z0-9]{20,30}\b'),
    re.compile(r'\b(?:[A-Z0-9]{4,6}-){3,5}[A-Z0-9]{4,6}\b'),
    re.compile(r'\b[A-Za-z0-9+/]{24,50}={0,2}\b')
]

def scan_text(text):
    hits = []
    for pattern in PATTERNS:
        matches = pattern.findall(text)
        if matches:
            hits.extend(matches)
    return hits