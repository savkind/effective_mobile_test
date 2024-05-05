class Messages:
    msg_add: str = 'Введите запись в формате \"Категория(доход/расход);Сумма;Описание\"'
    msg_uncor_cat: str = 'Неверная категория'
    msg_uncor_sum: str = "Неверная сумма, используйте только цифры"
    msg_search: str = "Введите фильтр в формате \"Поле(date/category/sum):Значение\""
    msg_uncor_filter: str = "Неверный фильтр"
    msg_commands: str = "Команды: \n 1 - Вывести баланс \n 2 - Добавление записи \n 3 - Редактирование записи \n 4 - Поиск по записям"
    user_input: str = "> "
    msg_input_id: str = "Введите id транзакции:"
    msg_uncor_command: str = "Неверная команда!"
