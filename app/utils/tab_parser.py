import re
from fastapi import APIRouter, UploadFile, HTTPException

router = APIRouter()

def detect_instrument(tab_text: str) -> str:
    lines = tab_text.strip().split("\n")
    tab_lines = [line for line in lines if "-" in line]
    if len(tab_lines) == 4:
        return "bass"
    if len(tab_lines) == 5:
        return "5-string bass"
    elif len(tab_lines) == 6:
        return "guitar or 6-sting bass"
    elif len(tab_lines) == 7:
        return "7-string guitar"
    elif len(tab_lines) == 12:
        return "12-string guitar"
    else:
        return "unknown"

KNOWN_TUNINGS = {
    "E - A - D - G - B - E": "Standard Guitar",
    "D - A - D - G - B - E": "Drop D",
    "D - G - C - F - A - D": "D Standard",
    "C - G - C - F - A - D": "Drop C",
    "D - A - D - G - A - D": "DADGAD",
    "E - A - D - G": "Standard Bass",
    "B - E - A - D - G": "5-string Bass",
}

def extract_tuning(tab_text: str) -> str:
    lines = tab_text.strip().split("\n")
    tuning_lines = [line for line in lines if re.match(r"^[A-Ga-g][#b]?[\|:]", line.strip())]

    if tuning_lines:
        note_pattern = re.compile(r"^[A-Ga-g][#b]?$")
        tuning = [line.strip().split("|")[0].strip().upper() for line in tuning_lines]
        joined = " - ".join(tuning)
        if all(note_pattern.match(note) for note in tuning):
            return KNOWN_TUNINGS.get(joined, f"{joined} (custom)")
    return "standard (assumed)"

def extract_metadata(tab_text: str) -> dict:
    metadata = {}
    if "Artist" in tab_text:
        metadata["artist"] = re.search(r"Artist:\s*(.+)", tab_text).group(1)
    if "Title" in tab_text:
        metadata["title"] = re.search(r"Title:\s*(.+)", tab_text).group(1)
    return metadata


@router.get("/metadata/{public_id}")
async def get_tab_metadata(public_id: str) -> dict[str, str | dict]:
    try:
        tab_text = download_tab_stream(public_id)
    except Exception:
        raise HTTPException(status_code=404, detail="Tab not found")

    return {
        "instrument": detect_instrument(tab_text),
        "tuning": extract_tuning(tab_text),
        "metadata": extract_metadata(tab_text)
    }
