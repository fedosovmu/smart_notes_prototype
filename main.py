from src.csmart_notes_handler import SmartNotesHandler

if __name__ == '__main__':
  # файлики с промтами
  # prompts = ['prompt_orig.txt']
  prompts = ['prompt_1.txt']
  # файлики с заметками
  # notes = ['note_2.txt']
  notes = ['note_1.txt', 'note_2.txt', 'note_3.txt']
  dev = True
  # default False
  # Выполняю запросы для всех комбинаций промтов и заметок
  SmartNotesHandler().execute(prompts, notes)
