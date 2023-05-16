

class SmartNotesHandler:
	def execute(self, prompts, notes):
		print('=== Запускаю скрипт ===')

		for prompt in prompts:
			print(f'Выполняю промт «{prompt}»')
			for note in notes:
				print(f'  - Анализирую заметку «{note}»')
				self._execute_prompt(prompt, note)

	def _execute_prompt(self, prompt, note):
		print('    Результат: (пока что нету. код еще не дописал)')
	
	def _read_file_from_data(self, file_name):
		pass

