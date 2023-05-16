import os
import openai
import json


class SmartNotesHandler:
	def execute(self, prompts, notes):
		print('=== Запускаю скрипт ===')

		for prompt in prompts:
			print(f'Выполняю промт «{prompt}»')
			for note in notes:
				print(f'  - Анализирую заметку «{note}»')
				self._execute_prompt(prompt, note)
		print('=== Конец скрипта ===')

	def _execute_prompt(self, prompt, note):
		prompt_text = self._read_file_from_data(prompt)
		note_text = self._read_file_from_data(note)
		server_answer = self._send_request(prompt_text, note_text)
		self._analyze_result(server_answer)
	
	def _read_file_from_data(self, file_name):
		f = open(f'data/{file_name}')
		data = f.read()
		f.close()
		return data

	def _send_request(self, prompt, note):
		openai.api_key = os.getenv("API_KEY")
		organization = os.getenv("ORGANIZATION")

		try:
			completion = openai.ChatCompletion.create(
			  model="gpt-3.5-turbo",
			  messages=[
			  	{"role": "user", "content": prompt},
			    {"role": "user", "content": note}
			  ]
			)
			server_answer = completion.choices[0].message
			#print(f'    Ответ сервера {server_answer}')
			return server_answer
		except:
			print('    Ошибка. Проблемы при отправке запроса на сервер')
		return None

	def _analyze_result(self, server_answer):
		content = server_answer['content']
		try:
			events = json.loads(content)
			print('    Распознанные события:')
			for event in events:
				print(f'      - "{event}"')
		except:
			print('    Ошибка. Не удалось распознать результат')
			print(f'    «Ответ сервера {content}»')
