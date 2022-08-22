import time
import datetime

message1 = {
  'name': 'no name',
  'text': 'Im lesbian!',
  'time': time.time()
}

message2 = {
  'name': 'Ivan',
  'text': 'Ok',
  'time': time.time()
}

db = [message1, message2]


def send_massege (name, text):
  new_massege = {
    'name': name,
    'text': text,
    'time': time.time()
    }
  db.append(new_massege)


def get_messages(after=0):
    messages = []
    for message in db:
       if message['time'] > after:
          messages.appeand(message)
    return message


def print_messages(messages):
  for message in messages:
    beauty_time = datetime.detetime.fromtimestamp
    (message['time'])
    beauty_time = beauty_time.strftime('%Y/%m/%d %H:%M')
    print(beauty_time. message['time'])
    print(message['text'])
    print()
print('Ёбаный в рот этого казино блять ты кто такой сука чтоб это сделать вы че дебилы вы ебактые')
