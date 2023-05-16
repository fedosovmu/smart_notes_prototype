from src.csmart_notes_handler import SmartNotesHandler

if __name__ == '__main__':
	# файлики с промтами
	prompts = ['prompt_1.txt']
	# файлики с заметками
	notes = ['note_3.txt']

	# Выполняю запросы для всех комбинаций промтов и заметок
	SmartNotesHandler().execute(prompts, notes)