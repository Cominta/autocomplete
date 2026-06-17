import sqlite3
import re
from sqlite3 import Error

def createDbFromRawData(file_path):

    try:
        conn = sqlite3.connect('EnglishDictionary.sqlite')
        conn.text_factory = str
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS words_freq (word text,freq integer);")
        print("Opened database successfully")
    except Error as e:
            print(e)

    # Open the raw text file
    with open(file_path, "r") as file:
        words = file.read()

    # Remove special characters, punctuation, and numbers
    cleaned_words = re.sub(r'[^a-zA-Z\s]', '', words)

    # Split the cleaned string into a list of words & generate sqlite db
    data = cleaned_words.split()
    count = 0
    for temp in data:
        count=count+1
        print("Loop 1: ",count)
        row=c.execute("SELECT count(*) FROM words_freq WHERE word LIKE ?", ("word="+temp,))
        rowcount=row.fetchone()[0]
        if rowcount <= 0:
            freq=1
            conn.execute("INSERT INTO words_freq (freq,word) VALUES (?,?)",(freq,"word="+temp))
            conn.commit()
            print("Records Inserted successfully")
        else:
            conn.execute("UPDATE words_freq SET freq = freq + 1 WHERE word LIKE ?", ("word="+temp,))
            conn.commit()
            print("Records Updated successfully")
    conn.close()

createDbFromRawData("/Users/adnanchohan/PycharmProjects/AOSP_DictionaryTool/RawDataLists/raw.txt") # file_path