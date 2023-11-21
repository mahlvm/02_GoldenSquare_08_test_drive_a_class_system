from lib.diary import Diary

def test_initially_has_empty_list_of_entries():
    diary = Diary()
    assert diary.all() == []

def test_initially_word_count_zero():
    diary = Diary()
    assert diary.count_words() == 0