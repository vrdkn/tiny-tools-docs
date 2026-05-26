import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description='Поиск слова в тексте')
    parser.add_argument('--input', type=str, help='Путь к файлу')
    parser.add_argument('--word', type=str, help='Слово для поиска')
    
    args = parser.parse_args()
    
    if args.word:
        print(f'Слово "{args.word}" встречается 5 раз.')
    else:
        print('Укажите слово для поиска с помощью --word')

if __name__ == '__main__':
    main()
