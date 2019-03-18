#!/usr/bin/env python3

import sqlite3
import re


resources_path = 'POSIX-1-2017.docset/Contents/Resources/'

conn = sqlite3.connect(resources_path + 'docSet.dsidx')
cur = conn.cursor()

try:
    cur.execute('DROP TABLE searchIndex;')
except:
    pass
cur.execute(
    'CREATE TABLE searchIndex(id INTEGER PRIMARY KEY, name TEXT, type TEXT, path TEXT);')
cur.execute(
    'CREATE UNIQUE INDEX anchor ON searchIndex (name, type, path);')

insert_sql = 'INSERT OR IGNORE INTO searchIndex(name, type, path) VALUES (?,?,?)'

docpath = resources_path + 'Documents/'

cur.execute(insert_sql, ('Base Definitions', 'Guide', 'basedefs/contents.html'))
cur.execute(insert_sql, ('System Interfaces', 'Guide', 'functions/contents.html'))
cur.execute(insert_sql, ('Shell & Utilities', 'Guide', 'utilities/contents.html'))
cur.execute(insert_sql, ('Rationale', 'Guide', 'xrat/contents.html'))

headers_index = docpath + 'idx/head.html'
headers_pattern = re.compile(
    r'<li><a href="\.\./(?P<path>[^"]+)" target="main">&lt;(?P<name>[^&]+)&gt;</a></li>'
)
for header in headers_pattern.finditer(open(headers_index).read()):
    cur.execute(insert_sql,
                (header.group('name'), 'File', header.group('path')))

utilities_index = docpath + 'idx/utilities.html'
utilities_pattern = re.compile(
    r'<li><a href="\.\./(?P<path>[^"]+)" target="main">(?P<name>[^<]+)</a>'
)
for utility in utilities_pattern.finditer(open(utilities_index).read()):
    cur.execute(insert_sql,
                (utility.group('name'), 'Command', utility.group('path')))

functions_index = docpath + 'idx/functions.html'
functions_pattern = re.compile(
    r'<li><a href="\.\./(?P<path>[^"]+)" target="main"><i>(?P<name>[^<]+)</i>\(?\)?</a></li>'
)
for function in functions_pattern.finditer(open(functions_index).read()):
    cur.execute(insert_sql,
                (function.group('name'), 'Function', function.group('path')))

conn.commit()
conn.close()
