# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

with open('file_words.txt', 'w') as data:
    data.write('Текст текабвст, из которого которогоабв надо удаабвлить удалить')
with open('file_words.txt', 'r') as data:
    string = data.readline()

def del_words(fined_text):
    fined_text = list(filter(lambda x: 'абв' not in x, fined_text.split()))
    return " ".join(fined_text)

with open('file_words.txt', 'r') as file:
    fined_text = file.read()

with open('file_words_2.txt', 'w') as file:
    fined_text = del_words(fined_text)
    file.write(fined_text)

print('Текст без абв: ' + fined_text)