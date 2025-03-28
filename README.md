# Экстрактор данных 1С в базу данных ClickHouseDB / Extractor 1C Clickhouse

## Название

Коммерческая версия => <https://infostart.ru/marketplace/1970328/>

Экстрактор данных 1С в ClickHouse

<https://kimkarus.ru/2024/02/12/instrukciya-polzovatelya/>

<https://github.com/kimkarus/Extractor_1C_Clickhouse>

Видео по быстрой установке и использованию

<https://youtu.be/Cbu98q5adfg>

<https://rutube.ru/video/9950d79387f22d01bcf7f1f1822896c4/>

<https://vk.com/video2644769_456239018>

## Краткое описание

Обработка для выгрузки данных из подготовленных СКД в фоновом режиме в базу ClickHouse. Это дополнительная подключаемая обработка.

## Описание

Обработка рассчитана на опытных пользователей 1С тех, кто знает, что такое СКД и конфигуратор 1С. Если вы не из таких, обратитесь к соответствующему специалисту.

**В инструкции нет картинок**

Все настройки вписываются внутрь самой обработки и в параметры СКД.

В обработке нет кода для обхода RLS.

## Результат работы обработки

- Создать базу данных ClickHouse, если есть права и ее нет.
- Создать таблицу данных по имени запроса.
- В фоновом режиме исполнить добавленные макеты запросов по добавленным командам.

### Требования

- Должная быть открытая для соединений база ClickHouse.
- Должен быть пользователь базы, который может делать INSERT в базу.
- Лучше заранее создать необходимое для вас имя базы.
- Должно быть право использовать и добавлять дополнительны обработки в информационную базу.
- В запросах рекомендуется использовать “ВЫБРАТЬ РАЗРЕШЕННЫЕ” (несмотря на то, что исполнение фоновое), чтобы не попадать на проблемы с правами по модели RLS.

### Технические требования

Решение протестировано на конфигурациях:

- 1С:Управление торговлей 11.5.17.122
- 1С:Бухгалтерия предприятия от 3.0.157.32
- 1С:Зарплата и управление персоналом 3.1.30.35
- 1С:Розница 3.0.10.178
- 1C:Комплексная автоматизация 2.5.20.91
- 1С:Управление производственным предприятием, редакция 1.3.122.2 (для фоновых заданий, требуется доработка вашей конфигурации 6 часов)

### Особенности

- **Используется тип таблиц “ReplacingMergeTree”, что означает замещение не ключевых значений новыми значениями.**
- **Не использовать поле “Период” в выходном слое отчета.**
- Параметры не формат даты должны быть предопределены.
- Заранее указать форматы для данных, которые не следует рассматривать, как ключи.
- Если формат данных в СКД не указать, то обработка будет воспринимать это поле, как ключевое значение и строковое.
- Все строковые поля попадут в ключи.
- **Если изменилась структура запроса, то добавьте новую команду в интерфейс. Обработка не умеет переделывать таблицы под ваш запрос. Обработка не добавляет новые колонки.**

### Установка

Инструкция по установке обработки - <https://kimkarus.ru/2025/02/08/instrukciya-po-ustanovke-ekstraktor-dannyh-1s-v-clickhouse/>

### Настройка параметров

Открываем обработку в режиме конфигуратора.

Действия -> Открыть модуль объекта

**Процедура “СведенияОВнешнейОбработке”**

Удаляем не наши “ДобавитьКоманду” и оставляем одну, чтобы по образу и подобию добавить свою фоновую задачу выгрузки.

Команда выглядит следующим образом:

```
ДобавитьКоманду(ТаблицаКоманд, "БросаниеВагоновТип фоновое", "Синхронизация1C_ClickHouseНаСервере_БросаниеВагоновТип" , "ВызовСерверногоМетода");
```

“ТаблицаКоманд” – системная таблица команд обработки. Из это таблицы в интерфейсе информационной базы 1С будет показывать наши добавленные команды таким образом.

“БросаниеВагоновТип фоновое” – Видимое и понятное имя команды для пользователя

“”Синхронизация1C_ClickHouseНаСервере\_БросаниеВагоновТип” – Системное имя команды, по которой ориентируется обработка.

**Здесь важно отметить**, что нижние подчеркивания “\_”, **это функциональная и обязательная часть** имени. Всего должно быть 2 подчеркивания всегда.

“\_БросаниеВагоновТип” – После второго подчеркивания, это имя запроса, который мы положили в макеты обработки

**Функция ЗаполнитьПараметры**

Здесь указываем параметры подключения к нашему серверу, где хранится наша уже созданная база данных или нет.

```
Функция ЗаполнитьПараметры() Экспорт
ТекущаяДата = ТекущаяДата();
СтруктураПараметры = Новый Структура;
СтруктураПараметры.Вставить("Адрес", "IP");
СтруктураПараметры.Вставить("Порт", 8123);
СтруктураПараметры.Вставить("Логин", "default");
СтруктураПараметры.Вставить("Пароль", "password");
СтруктураПараметры.Вставить("ИмяБазы", "db_name");
СтруктураПараметры.Вставить("ИмяТаблицы", "БросаниеВагоновТип");

СтруктураПараметры.Вставить("ДатаНачала", ДатаДнейНазад(ТекущаяДата, 1));
СтруктураПараметры.Вставить("ДатаОкончания", КонецДня(ТекущаяДата));
Возврат СтруктураПараметры;
КонецФункции
```

## Добавление отчетов на основе СКД

Макеты -> Добавить

Формируем или вставляем наш запрос.

### Требования

Добавить в параметры своего отчета

**Всегда использовать Период, как дату, а не стандартный период в параметрах СКД.**

**КоличествоДнейНазад** – за какое количество дней формировать отчет и обновлять записи в базе. По умолчанию = 1

**Начало и окончание дат периода** должны быть обозначены **Дата1 и Дата2.**

Остальные примеры для месяца и дня смотри функцию **ВернутьДату\_Запрос\_НаСервере**

## Добавление обработки в информационную базу

Администрирование -> Дополнительные обработки и отчеты

Добавить из файла.

Для добавленных команд в таблицу команд, будет возможность использовать их как фоновое задание. Отмечаем галочками и выставляем расписание исполнения.

Как только сохраните обработку в таком виде, запустятся столько фоновых здание, сколько отметите галками.

Чтобы запустить вручную каждое, необходимо зайти в Администрирование -> Обслуживание -> Регламентные и фоновые задания.

Общая форма обработки не предусмотрена. Используйте команды и кнопки для взаимодействия по образу и подобию из нашей “боевой” обработки.

Have fun!