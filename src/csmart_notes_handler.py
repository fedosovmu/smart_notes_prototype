import os


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
		prompt_text = self._read_file_from_data(prompt)
		note_text = self._read_file_from_data(note)
		result = self._send_request(prompt_text, note_text)
	
	def _read_file_from_data(self, file_name):
		f = open(f'data/{file_name}')
		data = f.read()
		f.close()
		return data

	def _send_request(self, prompt, note):
		api_key = os.getenv("TEST_SECRET")

