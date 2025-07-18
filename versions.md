**IDEAS:**

- проверка даты версии данных
- расписание регламентных заданий в таблице запросов
- выгрузка в формате списка объектов JSON
- очистка журнала регистрации
- выгрузка измененных объектов по журналу регистрации
- несколько настроек выгрузки журнала регистрации

**TODO:**

- выгрузка журнала регистрации, единые правила
- журнал регистрации фильтры объектов

**1.3.4**

- обновление обычных форм
- поддержка выгрузки по одной записи
- фоновые задачи для портиций
- совместимость загрузки конфигурационного файла json между разными версиями
- устранены найденные ошибки и улучшена работа кода

**1.3.3**

- Разработан функционал добавления в базу данных отсутствуещих полей, те что есть в запросе, но нет в базе данных. Опция Создавать несуществующие поля в БД. Доработана опция "Проверить?" поиска несуществующих полей. Выводится сообщение пользователю.

**1.3.2**

- Добавлена возможность внесения дополнительных ключевых полей через таблицу "Дополнительные ключи".

**1.3.1**

- Отправка данных по REST API в шины данных
- Оптимизация кода

**1.3.0**

- Оптимизация кода
- Адаптация к форматам данных

**1.2.9**

- Импорт/экспорт конфигов

**1.2.8**

- Несколько запросов в одном интерфейсе

**1.2.7**

- Добавлены фиксированные дополнительные ключи

**1.2.4**

- Добавлена поддержка MySQL

**1.2.1**

- Добавлена поддержка PostgreSQL

**1.1.9**

- реализована поддержка обычных форм
- реализована механизм выгрузки данных в базу данных PostgreSQL
- улучшена работа с запросами
- разные фиксы

**1.1.4**

- добавлена возможность исключать Период из ключа
- добавлена возможность указывать путь до пользовательского корневого сертификата SSL для создания соединения
- добавлена функция экранизации специальных символов в строках
- разные фиксы

**1.1.3**

- Добавлен минимальный пользовательский интерфейс со всеми возможностями консольного варианта (фоновые команды)
- Добавлена возможность сохранения пользовательских настроек и воспроизведения их в фоновом режиме
- Для много поточного режима по прежнему следует использовать добавление фоновых команд и своих схем компоновки данных через конфигуратор

**1.1.2**

- Можно использовать “ПериодРегистратора” в СКД, как поле, как альтеративное поле “Период”. “ПериодРегистратора” замещает “Период” при его наличии.
- Добавлен параметр “ИспользоватьСтарыйМетодФоновыхЗаданий” и его логика\\
- обавлен параметр “ПроверитьТаблицу” и его логика
- Изменена логика обработки ключевых полей. Ключевые поля, это те, у которых явно не обозначен тип данных.
- Добавлена обработка тип данных “Булево”
- Устранены баги

**1.0.9**

- Реализован механизм игнорирования порядка полей из набора данных. Порядок полей из результата запроса.
- A mechanism has been implemented to ignore the order of fields from a data set. The order of the fields from the query result.

**1.0.8**

- Реализована работа параллельной выгрузки. Параметр “ОднимФайлом = Ложь” в параметрах СКД
- Параметр “КоличествоВПортиции” стоит 1000, чтобы делить результат запроса на несколько потоков

**1.0.7**

- Параметр батчей / порций / портиций выведен в отдельную переменную
- Улучшена работа с датами

**1.0.6**

- Реализована запись пачками / батчами по 1000 штук
- Оптимизация кода

**1.0.5**

- Оптимизация кода
- Обработка новых полей
- Добавлены несколько полей дат

**1.0.4**

- Создание МассивПолейКлючейПериод

**1.0.3**

- Обработка нового поля “КоличествоДнейНазад”
- Оптимизация функции ВернутьЧислоБезПробелов

**1.0.2**

- Оптимизация кода
- Обработка новых полей

**1.0.1 01.11.2023**

- добавил ключевые поля для специфических отчётов
- добавил способ поиска параметра даты для запроса