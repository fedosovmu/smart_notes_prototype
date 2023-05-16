import os
import openai


class SmartNotesHandler:
	def execute(self, prompts, notes):
		print('=== Запускаю скрипт ===')

		for prompt in prompts:
			print(f'Выполняю промт «{prompt}»')
			for note in notes:
				print(f'  - Анализирую заметку «{note}»')
				self._execute_prompt(prompt, note)

	def _execute_prompt(self, prompt, note):
		prompt_text = self._read_file_from_data(prompt)
		note_text = self._read_file_from_data(note)
		result = self._send_request(prompt_text, note_text)
		print(f'    Результат: {result}')
	
	def _read_file_from_data(self, file_name):
		f = open(f'data/{file_name}')
		data = f.read()
		f.close()
		return data

	def _send_request(self, prompt, note):
		openai.api_key = os.getenv("API_KEY")
		organization = os.getenv("ORGANIZATION")
		
		completion = openai.ChatCompletion.create(
		  model="gpt-3.5-turbo",
		  messages=[
		  	{"role": "user", "content": prompt},
		    {"role": "user", "content": note}
		  ]
		)

		print('    Ответ сервера')
		result = completion.choices[0].message
		print(result)

		
		return '(Код анализирующий результат еще не готов)'
