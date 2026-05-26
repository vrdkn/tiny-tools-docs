# Столовая онлайн

![Логотип](https://static.ucheba.ru/pix/logo_cache/22242.upto100x100.webp)
![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)

## Описание

Веб-приложение для заказа еды в столовой учебного заведения.  
Позволяет пользователям просматривать меню, формировать заказ, оплачивать онлайн и получать еду по QR-коду.

Основные возможности:
- Просмотр меню с фотографиями и ценами
- Добавление блюд в корзину
- Онлайн-оплата картой или СБП
- Генерация QR-кода для получения заказа
- Админ-панель для сотрудников столовой

## Требования

- Python 3.10 или выше
- PostgreSQL 16
- Современный браузер (Chrome, Edge, Firefox)

## Установка

```bash
# 1. Клонируйте репозиторий
git clone https://github.com/vrdkn/tiny-tools-docs.git
cd tiny-tools-docs

# 2. Создайте виртуальное окружение
python -m venv venv
source venv/bin/activate   # Для Windows: venv\Scripts\activate

# 3. Установите зависимости
pip install -r requirements.txt

# 4. Настройте базу данных PostgreSQL
#    Создайте базу canteen_db и выполните скрипты из папки sql/

## Использование
```
# Запуск сервера
python main.py
# Откройте в браузере http://127.0.0.1:8000

## Документация 
Полная документация в папке /docs.

## Автор
Редькина Ева Эдуардовна 

## 
```
