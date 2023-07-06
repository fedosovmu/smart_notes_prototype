# from src.csmart_notes_handler import SmartNotesHandler
from src.csmart_notes_handler_tmp import SmartNotesHandler

if __name__ == '__main__':
  # файлики с промтами
  # prompts = ['prompt_orig.txt']
  # prompts = ['prompt_1.txt']
  prompts = ['prompt_2_0.txt', 'prompt_2_1.txt', 'prompt_2_2.txt']
  # файлики с заметками
  notes = ['note_1.txt']
  # notes = ['note_1.txt', 'note_2.txt', 'note_3.txt', 'note_4.txt', 'note_5.txt', 'note_6.txt']
  # default False
  # Выполняю запросы для всех комбинаций промтов и заметок
  s = SmartNotesHandler()
  s.dev = True
  # s.test()
  s.execute(prompts, notes)
