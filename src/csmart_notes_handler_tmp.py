import os
import sys
import openai
import json
import time
# from rich import print
# from rich.console import Console
# from rich.markdown import Markdown

class SmartNotesHandler:
  dev = False
  def test(self):
    openai.api_key = os.getenv("API_KEY")
    # print(openai.Model.list())
    print(openai.Engine.list())
    
  def execute(self, prompts, notes):
    if self.dev:
        print(f'====== Запускаю скрипт , режим dev ({self.dev}) ======')
    else:
        print(f'====== Запускаю скрипт , режим dev ({self.dev}) ======')

    for prompt in prompts:
      print(f'Выполняю промт «{prompt}»')
      for note in notes:
        print(f'  - Анализирую заметку «{note}»')
        server_answer = self._execute_prompt(prompt, note)
        with open(f'out/f_{prompt}.txt', "w") as file:
          file.write(server_answer)
    print('====== Конец скрипта ====== \n')

  def _execute_prompt(self, prompt, note):
    prompt_text = self._read_file_from_data(prompt)
    note_text = self._read_file_from_data(note)
    start_time = time.time()
    # print(start_time)
    server_answer = self._send_request(prompt_text, note_text)
    sa_time = time.time()
    # print("----------")
    print("\n запрос секунд :",sa_time-start_time)
    if self.dev: 
      data_text = input("\n Уточним : ")
    print(' ')
    if 'data_text' in locals() and data_text:
      server_answer2 = self._send_request2(prompt_text, note_text, server_answer['content'], data_text)
    # print(sa_time)
    self._analyze_result(server_answer)
    ar_time = time.time()
    # print(ar_time)
    # print("********")
    # print("анализ секунд :",ar_time-sa_time)
    return server_answer['content']
  def _read_file_from_data(self, file_name):
    f = open(f'data/{file_name}')
    data = f.read()
    f.close()
    return data

  def _send_request(self, prompt, note):
    openai.api_key = os.getenv("API_KEY")
    organization = os.getenv("ORGANIZATION")
    try:
      # completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
      completion = openai.ChatCompletion.create(model="gpt-3.5-turbo-0301",
                                                temperature=0,
                                                # top_p=0.0001,
                                                messages=[{
                                                  "role": "system",
                                                  # "role": "user",
                                                  "content": prompt
                                                }, {
                                                  "role": "user",
                                                  "content": note
                                                }])
      server_answer = completion.choices[0].message
      # server_answer = completion.choices[0].message.content
      # print(f'    Ответ сервера {server_answer}')
      if self.dev :
        use = completion.usage
        # print(f'    Токены : {use}')
        # print(f'    Токены : {completion}')
        # console = Console()
        # md = Markdown(server_answer.content)
        # console.print(md)
        print(server_answer.content)
        # with open(f'file_{time.time()}.txt', "w") as file:
          # file.write(server_answer.content)
      return server_answer
    except:
      if self.dev :
        exc_type, exc_value, exc_traceback = sys.exc_info()
        # Вывод причины исключения
        print(f"Ошибка при запросе: {exc_value}")
    return None

  def _analyze_result(self, server_answer):
    if server_answer is None:
      return
    content = server_answer['content']
    try:
      events = json.loads(content)
      print('    Распознанные события:')
      # for event in events:
      #   print(f'      - "{event}"')
    except:
      print(' ')
      # print('    Ошибка. Не удалось распознать результат')
      # print(f'    Ответ сервера:')
      # print('=== Начало ответа ===')
      # print(content)
      print('=== Конец ответа ===')

  def _send_request2(self, prompt, note, sa, data_text):
    openai.api_key = os.getenv("API_KEY")
    organization = os.getenv("ORGANIZATION")
    try:
      #completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
      completion = openai.ChatCompletion.create(model="gpt-3.5-turbo-0301",
                                                temperature=0,
                                                # top_p=0.0001,
                                                messages=[{
                                                  "role": "system",
                                                  # "role": "user",
                                                  "content": prompt
                                                }, {
                                                  "role": "user",
                                                  "content": note
                                                }, {
                                                  "role": "assistant",
                                                  "content": sa
                                                }, {
                                                  "role": "user",
                                                  "content": data_text
                                                }])
      server_answer = completion.choices[0].message
      # server_answer = completion.choices[0].message.content
      # print(f'    Ответ сервера {server_answer}')
      if self.dev :
        use = completion.usage
        print(f'    Токены : {use} \n')
        # print(f'    Токены : {completion}')
        print(server_answer.content)
      return server_answer
    except:
      if self.dev :
        exc_type, exc_value, exc_traceback = sys.exc_info()
        # Вывод причины исключения
        print(f"Ошибка при запросе: {exc_value}")
    return None


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
