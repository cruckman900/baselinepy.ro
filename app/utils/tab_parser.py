import re

def detect_instrument(tab_text: str) -> str:
    lines = tab_text.strip().split("\n")
    tab_lines = [line for line in lines if "-" in line]
    if len(tab_lines) == 4:
        return "bass"
    elif len(tab_lines) == 6:
        return "guitar"
    else:
        return "unknown"

def extract_tuning(tab_text: str) -> str:
    # Look for lines that resemble tuning notation, e.g., "E|", "D|, etc
    lines = tab_text.strip().split("\n")
    tuning_lines = [line for line in lines if re.match(r"^[A-Ga-g][#b]?[\|:]", line.strip())]

    if tuning_lines:
        tuning = [line.strip().split("|")[0].strip() for line in tuning_lines]
        return " - ".join(tuning)
    return "standard (assumed)"
