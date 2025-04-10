# 🏋️ Diet Bot 🤖

[![Aiogram](https://img.shields.io/badge/aiogram-3.x-blue.svg)](https://aiogram.dev/)
[![Python](https://img.shields.io/badge/Python-3.11%2B-yellowgreen)](https://python.org)
[![Docker](https://img.shields.io/badge/Docker-✔️%20Ready-blue)](https://docker.com)

Телеграм-бот для контроля здоровья и фитнес-прогресса. Рассчитывает дневную норму калорий, отслеживает потребление пищи и воды, учитывает физическую активность.

## 🌟 Основные функции

### 🔄 **Жизненный цикл пользователя**  
1. **Старт** → Настройка профиля под ваши параметры  
2. **Планирование** → Расчет индивидуальных норм  
3. **Действие** → Ежедневный трекинг активности и питания

### 📋 Персонализированный профиль
- Сбор антропометрических данных (рост, вес, возраст итд)
- Определение уровня активности
- Выбор цели

### 🔢 Умные расчеты
- Автоматический расчет дневной нормы калорий
- Обновление остатка калорий
- Трекинг водного баланса

### 🍏 Интеграции с API
- Автоматический расчет калорийности продуктов
- Отображение текущей погоды

### 📊 Основные команды
| Команда           | Описание                          |
|--------------------|-----------------------------------|
| `/start`          | Инициализация профиля             |
| `/about`          | Показать ваши данные              |
| `/calc_my_norm`   | Рассчитать дневную норму          |
| `/show_my_norm`   | Текущие показатели                |
| `/log_water`      | Внести потребление воды           |
| `/log_food`       | Добавить прием пищи               |
| `/log_workout`    | Записать тренировку               |

## 🚀 Установка и запуск

### Предварительные требования
- Python 3.11+
- Docker и Docker Compose
- API ключи

1. Клонировать репозиторий:
```bash
git clone https://github.com/yourusername/fitness-calorie-bot.git
cd fitness-calorie-bot
```

## 🛠 Технологический стек
- Core: Python 3.9, Aiogram 3.x
- API: 
- База данных: PostgreSQL (**в процессе**)
- Инфраструктура: Docker, Docker Compose
- Вспомогательные: Requests, Logging, Dotenv

## 📈 Системные особенности
- Асинхронная архитектура
- Контейнеризация сервисов
- Защита чувствительных данных через .env
