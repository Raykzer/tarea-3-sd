#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import psycopg2
import re

def postgresql_connect():
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="postgres",
            host="db",
            port="5432",
            database="tarea"
        )
        return connection
    except (Exception, psycopg2.Error) as e:
        print("Error connecting to PostgreSQL:", e)
        sys.exit(1)

def process_input(line):
    doc = line.lower()

    # Extract name and document parts
    name, doc = doc.split('<splittername>')
    name, url = name.split()

    # Remove punctuation and numeric values
    doc = re.sub(r'\W+', ' ', doc.replace("\n", ' ')).strip()
    for char in [",", ".", '"', "'", "(", ")", "\\", ";", ":", "$1", "$", "&", "="]:
        doc = doc.replace(char, '')

    # Process each word in the document
    word_list = []
    for word in doc.split():
        if word.isalpha():
            word_list.append('{}\t{}\t{}'.format(word, name, 1))

    return word_list, name, url

def insert_paginas(cursor, name, url):
    try:
        for _ in range(30):
            cursor.execute("INSERT INTO paginas (id, url) VALUES (%s, %s) ON CONFLICT (id) DO NOTHING", (name, url))
        connection.commit()
    except (Exception, psycopg2.Error) as err:
        print("Error during paginas table insertion:", err)

def main_execution():
    connection = postgresql_connect()

    try:
        cursor = connection.cursor()

        for line in sys.stdin:
            word_list, name, url = process_input(line)

            # Sort and print the processed words
            for word_entry in sorted(word_list):
                print(word_entry)

            insert_paginas(cursor, name, url)

    finally:
        if connection:
            cursor.close()
            connection.close()

if __name__ == "__main__":
    main_execution()
