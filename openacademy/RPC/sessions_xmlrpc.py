#!/usr/bin/env python3

import xmlrpc.client

host = 'localhost'
port = '8569'
db = 'o15-learn'
username = 'admin'
password = 'admin'

root = f'http://{host}:{port}/xmlrpc/'
models = xmlrpc.client.ServerProxy(f'{root}object')
uid = xmlrpc.client.ServerProxy(root + 'common').login(db, username, password)

session_infos = models.execute_kw(db, uid, password,\
                                 'openacademy.session',\
                                 'search_read',\
                                 [[]],\
                                 {'fields': ['name',\
                                             'number_of_seats']})

print("Список сессий:")
for session in session_infos:
  print(session)

print ('\n Создание новой сессии:\n')
print ("шаг 1/3 - задайте id курса из списка:")
course_infos = models.execute_kw(db, uid, password,\
                                'openacademy.course',\
                                'search_read',\
                                [[]],\
                                {'fields': ['name']})
for course in course_infos:
  print(course)

new_session_course_id = int(input('id курса = '))
print ("шаг 2/3 - задайте наименование новой сессиии")
new_session_name = input('наименование новой сессии = ')
print ("шаг 3/3 - задайте количество мест для участников")
new_number_of_seats = int(input('количество мест = '))
print('\n Заданные значения:', \
      '\n id курса = ', new_session_course_id, \
      '\n наименование новой сессии = ', new_session_name, \
      '\n количество мест для участников = ', new_number_of_seats,'\n')

new_session_id = models.execute_kw(db, uid, password,\
                                  'openacademy.session',\
                                  'create',\
                                  [{'name': new_session_name,\
                                    'number_of_seats': new_number_of_seats,\
                                    'course_id': new_session_course_id}])

session_infos = models.execute_kw(db, uid, password,\
                                 'openacademy.session',\
                                 'search_read',\
                                 [[]],\
                                 {'fields': ['name',\
                                             'number_of_seats']})

print("Список сессий:")
for session in session_infos:
  print(session)
