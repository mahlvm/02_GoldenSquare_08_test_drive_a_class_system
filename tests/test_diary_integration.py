from lib.diary import Diary
from lib.diary_entry import DiaryEntry

def tests_adds_list_diary_entries():
    diary = Diary()
    entry_1 = DiaryEntry("My title 1", "My content 1")
    entry_2 = DiaryEntry("My title 2", "My content 2")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.all() == [entry_1, entry_2]
