import os

path = input('Enter folder path: ')

if not os.path.isdir(path):
    print("The provided path doesn't exist.")
    exit()

ext = ('.txt', '.md') 
files = [f for f in os.listdir(path) if f.endswith(ext)]

if not files:
    print("No .txt or .md files found in the folder.")
    exit()

print("Available files:")
for file in files:
    print(f"- {file}")

choice = input('Choose a file (include extension): ')

if choice not in files:
    print("File not found or not supported.")
    exit()

with open(os.path.join(path, choice), 'r', encoding='utf-8') as file:
    content = file.read()
    print("\n File content:")
    print(content)

word_choice = input('Word: ')

word_choice = word_choice.lower()

spl_content = content.split()

word_count = 0

for i in spl_content:
    clean_word = i.strip('.,!?')
    clean_word = clean_word.lower()
    if word_choice ==  clean_word:
        word_count += 1
print(f'the word "{word_choice}" was found {word_count} times in "{choice}"!')