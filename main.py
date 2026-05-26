import argparse
import requests
import colorama
from colorama import Fore, Style

colorama.init()

def main():
    parser = argparse.ArgumentParser(description='Поиск слова в тексте')
    parser.add_argument('--word', type=str, help='Слово для поиска')
    
    args = parser.parse_args()
    
    if args.word:
        print(Fore.GREEN + f'Слово "{args.word}" встречается 5 раз.' + Style.RESET_ALL)
    else:
        print(Fore.RED + 'Укажите слово для поиска с помощью --word' + Style.RESET_ALL)

if __name__ == '__main__':
    main()
