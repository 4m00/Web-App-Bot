# Телеграм-бот с интеграцией веб-приложения

Этот телеграм-бот предназначен для упрощения процесса покупки товаров из интернет-магазина непосредственно в приложении Telegram с использованием интерфейса веб-приложения. Ниже представлен краткий обзор его функциональности и структуры.

## Функциональность

### Запуск бота
- После запуска бота пользователи получают приветственное сообщение и представлены с пользовательской клавиатурой для навигации.

### Покупка товаров
- Пользователи могут выбирать товары из списка, представленного во встроенном интерфейсе веб-приложения в чате.
- У каждого товара есть кнопка "Купить", которая запускает процесс покупки.
- После нажатия на "Купить" пользователю отправляется счет на оплату.

### Обработка оплаты
- После получения оплаты бот подтверждает успешную транзакцию и обрабатывает заказ.
- Он обрабатывает запросы предварительной проверки и уведомления о успешной оплате.

### Дополнительные возможности
- Пользователи могут получить доступ к информации о магазине, деталях доставки и оставить отзывы через текстовые команды в чате.

## Структура файлов

### Файлы на Python
- `bot.py`: Содержит основную логику телеграм-бота, включая обработчики сообщений, обработку оплаты и функциональность команд.
- `app.js`: Обрабатывает поведение интерфейса веб-приложения, встроенного в чат Telegram.
- `style.css`: Таблица стилей для форматирования HTML-контента веб-приложения.

### Файл HTML
- `index.html`: Основной HTML-файл, содержащий структуру интерфейса веб-приложения.

### Другие файлы
- `README.md`: Этот файл предоставляет обзор функциональности бота, его структуры и инструкции по использованию.

## Использование

Для использования бота:
1. Начните чат с ботом.
2. Переходите по интерфейсу веб-приложения для выбора товаров для покупки.
3. Нажмите на кнопку "Купить", чтобы запустить процесс покупки.
4. Следуйте инструкциям, чтобы завершить оплату.
5. После успешной оплаты заказ подтверждается, и транзакция обрабатывается.

## Примечания
- Убедитесь, что все необходимые токены и URL-адреса правильно настроены в коде перед развертыванием.
- Этот файл README служит руководством для понимания функциональности и структуры вашего бота.


