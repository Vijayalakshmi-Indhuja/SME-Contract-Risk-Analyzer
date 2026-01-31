import spacy

nlp = spacy.load("en_core_web_sm")


def get_entities(text):
    doc = nlp(text)

    parties = []
    dates = []
    amounts = []
    locations = []

    for ent in doc.ents:
        if ent.label_ == "ORG":
            parties.append(ent.text)
        elif ent.label_ == "DATE":
            dates.append(ent.text)
        elif ent.label_ == "MONEY":
            amounts.append(ent.text)
        elif ent.label_ in ["GPE", "LOC"]:
            locations.append(ent.text)

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
