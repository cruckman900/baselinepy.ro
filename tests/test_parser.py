from app.utils.tab_parser import extract_tuning

def test_extract_drop_d_tuning():
    tab = "D|----------------\nA|----------------\nD|----------------\nG|----------------\nB|----------------\nE|----------------"
    assert extract_tuning(tab) == "Drop D"
