#!/usr/bin/env python3

import json
import random
import urllib.request

HOST = 'localhost'
PORT = 8569
DB = 'o15-learn'
USER = 'admin'
PASS = 'admin'

def json_rpc(url, method, params):
    data = {'jsonrpc': '2.0',
            'method': method,
            'params': params,
            'id': random.randint(0, 1000000000),}

    req = urllib.request.Request(url=url, \
                                 data=json.dumps(data).encode(), \
                                 headers={'Content-Type':'application/json',})

    reply = json.loads(urllib.request.urlopen(req).read().decode('UTF-8'))
    if reply.get('error'):
        raise Exception(reply['error'])
    return reply['result']

def call(url, service, method, *args):
    return json_rpc(url, 'call', {'service': service, 'method': method, 'args': args})

url = 'http://%s:%s/jsonrpc' % (HOST, PORT)
uid = call(url, 'common', 'login', DB, USER, PASS)
print('url =',url)
print('uid =',uid)

session_infos = call(url, 'object', 'execute', \
                     DB, uid, PASS, \
                     'openacademy.session', \
                     'search_read', [], \
                     ['name', \
                      'number_of_seats'])

for session in session_infos:
  print(session)

print ('\n Создание новой сессии:\n')
print ('шаг 1/3 - задайте id курса из списка:')
course_infos = call(url, 'object', 'execute', \
                    DB, uid, PASS, \
                    'openacademy.course', \
                    'search_read', [], \
                    ['name'])

for course in course_infos:
  print(course)
new_session_course_id = int(input('id курса = '))

print ('шаг 2/3 - задайте наименование новой сессиии')
new_session_name = input('наименование новой сессии = ')

print ('шаг 3/3 - задайте количество мест для участников')
new_number_of_seats = int(input('количество мест = '))

print('\n Заданные значения:', \
      '\n id курса = ', new_session_course_id, \
      '\n наименование новой сессии = ', new_session_name, \
      '\n количество мест для участников = ', new_number_of_seats,'\n')

args = [{'name': new_session_name,
         'course_id': new_session_course_id,
         'number_of_seats': new_number_of_seats}]

new_session_id = call(url, 'object', 'execute', \
                      DB, uid, PASS, \
                      'openacademy.session', \
                      'create', \
                       args)


session_infos = call(url, 'object', 'execute', \
                     DB, uid, PASS, \
                     'openacademy.session', \
                     'search_read', [], \
                     ['name', \
                      'number_of_seats'])
print('Список сессий:')
for session in session_infos:
  print(session)
