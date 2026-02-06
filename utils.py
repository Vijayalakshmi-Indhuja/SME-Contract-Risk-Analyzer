import re

def get_entities(text):
    # Simple regex-based entity extraction

    # Extract possible organization names (basic capitalized words pattern)
    parties = re.findall(r'\b[A-Z][A-Za-z& ]+(?:Ltd|LLC|Inc|Corporation|Company)?\b', text)

    # Extract dates (basic formats)
    dates = re.findall(r'\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b', text)

    # Extract money amounts ($1000, ₹5000 etc.)
    amounts = re.findall(r'(?:\$|₹)\s?\d+(?:,\d{3})*(?:\.\d{2})?', text)

    # Extract locations (simple capitalized words assumption)
    locations = re.findall(r'\b(?:in|at|from)\s+([A-Z][a-zA-Z]+)', text)

    return {
        "Parties": list(set(parties)),
        "Dates": list(set(dates)),
        "Amounts": list(set(amounts)),
        "Jurisdiction": list(set(locations))
    }


def split_clauses(text):
    lines = text.split("\n")
    clauses = []

    for line in lines:
        if len(line.strip()) > 40:
            clauses.append(line.strip())

    return clauses
