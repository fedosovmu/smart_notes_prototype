import os
import openai
import json
import time

class SmartNotesHandler:

  def execute(self, prompts, notes):
    print('====== Запускаю скрипт ======')

    for prompt in prompts:
      print(f'Выполняю промт «{prompt}»')
      for note in notes:
        print(f'  - Анализирую заметку «{note}»')
        self._execute_prompt(prompt, note)
    print('====== Конец скрипта ======')

  def _execute_prompt(self, prompt, note):
    prompt_text = self._read_file_from_data(prompt)
    note_text = self._read_file_from_data(note)
    start_time = time.time()
    # print(start_time)
    server_answer = self._send_request(prompt_text, note_text)
    sa_time = time.time()
    print("----------")
    print("запрос секунд :",sa_time-start_time)
    # print(sa_time)
    self._analyze_result(server_answer)
    ar_time = time.time()
    # print(ar_time)
    print("********")
    print("анализ секунд :",ar_time-sa_time)

  def _read_file_from_data(self, file_name):
    f = open(f'data/{file_name}')
    data = f.read()
    f.close()
    return data

  def _send_request(self, prompt, note):
    openai.api_key = os.getenv("API_KEY")
    organization = os.getenv("ORGANIZATION")
    try:
      completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                                temperature=0,
                                                messages=[{
                                                  "role": "user",
                                                  "content": prompt
                                                }, {
                                                  "role": "user",
                                                  "content": note
                                                }])
      server_answer = completion.choices[0].message
      # server_answer = completion.choices[0].message.content
      # print(f'    Ответ сервера {server_answer}')
      use = completion.usage
      print(f'    Токены : {use}')
      # if True: print(server_answer.content)
      return server_answer
    except:
      print('    Ошибка. Проблемы при отправке запроса на сервер')
    return None

  def _analyze_result(self, server_answer):
    if server_answer is None:
      return
    content = server_answer['content']
    try:
      events = json.loads(content)
      print('    Распознанные события:')
      for event in events:
        print(f'      - "{event}"')
    except:
      print('    Ошибка. Не удалось распознать результат')
      print(f'    Ответ сервера:')
      print('=== Начало ответа ===')
      print(content)
      print('=== Конец ответа ===')


# Серверм может ответить на один и тот же вопрос сразу в нескольких форматах. Пока что мы умеем парсить только формат 1. Я планирую доработать функцию парсинга в будущем, чтобы мы могли разпознавать более нестандартные ответы вместо того чтобы падать с ошибкой.
#
#
# Формат 1. Чистый json
# ["Event 1", "Event 2"]
#
#
# Формат 2. Json с добавлением пояснений
# Events: ["Event 1", "Event 2"]
# ["Event 1", "Event 2"] (Significant for narrator)
#
#
# Формат 3. Произвольный список
# Events:
#  - Event 1
#  - Event 2
#
# This is all events significant for narrator
