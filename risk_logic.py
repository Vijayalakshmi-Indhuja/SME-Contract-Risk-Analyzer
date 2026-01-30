def check_risk(clause_text):
    text = clause_text.lower()

    if "sole discretion" in text or "without notice" in text:
        return "High", 3

    if "indemnify" in text or "auto-renewal" in text or "penalty" in text:
        return "Medium", 2

    if "lock-in" in text:
    	return "Medium", 2

    if "liability" in text:
        return "High", 3

    return "Low", 1


def overall_risk(score):
    if score >= 9:
        return "HIGH RISK"
    elif score >= 5:
        return "MEDIUM RISK"
    else:
        return "LOW RISK"

def explain_clause(clause):
    text = clause.lower()

    if "terminate" in text:
        return "This clause explains when and how the agreement can be ended."

    if "indemnify" in text:
        return "This means one party promises to cover losses or damages of the other."

    if "auto-renewal" in text:
        return "This clause means the contract renews automatically unless cancelled."

    if "payment" in text:
        return "This clause describes how and when payment should be made."

    return "This clause defines a general obligation under the agreement."
