# Extractor_1C_Clickhouse

<div class="entry-content">
								
<h2 class="wp-block-heading">Название</h2>



<p>Экстрактор данных 1С в ClickHouse</p>



<p><a href="https://github.com/kimkarus/Extractor_1C_Clickhouse">https://github.com/kimkarus/Extractor_1C_Clickhouse</a></p>



<h2 class="wp-block-heading">Краткое описание</h2>



<p>Обработка для выгрузки данных из подготовленных СКД в фоновом режиме в базу ClickHouse. Это дополнительная подключаемая обработка.</p>



<h2 class="wp-block-heading">Описание</h2>



<p>Обработка рассчитана на опытных пользователей 1С тех, кто знает, что такое СКД и конфигуратор 1С. Если вы не из таких, обратитесь к соответствующему специалисту.</p>



<p><strong>В инструкции нет картинок.</strong></p>



<p>Все настройки вписываются внутрь самой обработки и в параметры СКД.</p>



<p>В обработке нет кода для обхода RLS.</p>



<h2 class="wp-block-heading">Результат работы обработки</h2>



<ul>
<li>Создать базу данных ClickHouse, если есть права и ее нет.</li>



<li>Создать таблицу данных по имени запроса.</li>



<li>В фоновом режиме исполнить добавленные макеты запросов по добавленным командам.</li>
</ul>



<h2 class="wp-block-heading">Требования</h2>



<ul>
<li>Должная быть открытая для соединений база ClickHouse.</li>



<li>Должен быть пользователь базы, который может делать INSERT в базу.</li>



<li>Лучше заранее создать необходимое для вас имя базы.</li>



<li>Должно быть право использовать и добавлять дополнительны обработки в информационную базу.</li>



<li>В запросах рекомендуется использовать “ВЫБРАТЬ РАЗРЕШЕННЫЕ” (несмотря на то, что исполнение фоновое), чтобы не попадать на проблемы с правами по модели RLS.</li>
</ul>



<h2 class="wp-block-heading">Особенности</h2>



<ul>
<li><strong>Используется тип таблиц “ReplacingMergeTree”, что означает замещение не ключевых значений новыми значениями.</strong></li>



<li><strong>Не использовать поле “Период” в выходном слое отчета.</strong></li>



<li>Параметры не формат даты должны быть предопределены.</li>



<li>Заранее указать форматы для данных, которые не следует рассматривать, как ключи.</li>



<li>Если формат данных в СКД не указать, то обработка будет воспринимать это поле, как ключевое значение и строковое.</li>



<li>Все строковые поля попадут в ключи.</li>



<li><strong>Если изменилась структура запроса, то добавьте новую команду в интерфейс. Обработка не умеет переделывать таблицы под ваш запрос. Обработка не добавляет новые колонки.</strong></li>
</ul>



<h2 class="wp-block-heading">Установка</h2>



<h3 class="wp-block-heading">Настройка параметров</h3>



<p>Открываем обработку в режиме конфигуратора.</p>



<p>Действия -&gt; Открыть модуль объекта</p>



<p><strong>Процедура “СведенияОВнешнейОбработке”</strong></p>



<p>Удаляем не наши “ДобавитьКоманду” и оставляем одну, чтобы по образу и подобию добавить свою фоновую задачу выгрузки.</p>



<p>Команда выглядит следующим образом:</p>



<div class="wp-block-codemirror-blocks-code-block code-block" id="0"><pre class="CodeMirror" data-setting="{&quot;mode&quot;:&quot;clike&quot;,&quot;mime&quot;:&quot;text/x-csrc&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;styleActiveLine&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true,&quot;fileName&quot;:&quot;1C&quot;,&quot;language&quot;:&quot;C&quot;,&quot;modeName&quot;:&quot;c&quot;}" id="code-block-0" style="display: none;">ДобавитьКоманду(ТаблицаКоманд, "БросаниеВагоновТип фоновое", "Синхронизация1C_ClickHouseНаСервере_БросаниеВагоновТип" , "ВызовСерверногоМетода");</pre><div class="CodeMirror CodeMirror-simplescroll cm-s-material"><div class="CodeMirror-panel"><div class="info-panel"><span class="language c c">C</span><div class="control-panel"><span class="tool" data-tip="Full Screen"><b class="fullscreen maximize"></b></span><span class="tool" data-tip="Copy Code"><b class="copy"></b></span></div></div></div><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 36px; left: 4px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;" tabindex="0"></textarea></div><div class="CodeMirror-simplescroll-horizontal" cm-not-content="true" style="display: block; right: 0px; left: 0px;"><div style="width: 228.392px; left: 0px;"></div></div><div class="CodeMirror-simplescroll-vertical adjust-top" cm-not-content="true" style="display: none;"><div></div></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px; margin-bottom: -17px; border-right-width: 13px; min-height: 40px; min-width: 1442.05px; padding-right: 0px; padding-bottom: 8px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: none;"><div class="CodeMirror-measure"></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-cursors"><div class="CodeMirror-cursor" style="left: 4px; top: 0px; height: 32.3958px;">&nbsp;</div></div><div class="CodeMirror-code" role="presentation"><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">ДобавитьКоманду</span>(<span class="cm-variable">ТаблицаКоманд</span>, <span class="cm-string">"БросаниеВагоновТип фоновое"</span>, <span class="cm-string">"Синхронизация1C_ClickHouseНаСервере_БросаниеВагоновТип"</span> , <span class="cm-string">"ВызовСерверногоМетода"</span>);</span></pre></div></div></div></div></div><div style="position: absolute; height: 13px; width: 1px; border-bottom: 8px solid transparent; top: 40px;"></div><div class="CodeMirror-gutters" style="display: none; height: 61px;"></div></div></div></div>



<p>“ТаблицаКоманд” – системная таблица команд обработки. Из это таблицы в интерфейсе информационной базы 1С будет показывать наши добавленные команды таким образом.</p>



<p>“БросаниеВагоновТип фоновое” – Видимое и понятное имя команды для пользователя</p>



<p>“”Синхронизация1C_ClickHouseНаСервере_БросаниеВагоновТип” – Системное имя команды, по которой ориентируется обработка.</p>



<p><strong>Здесь важно отметить</strong>, что нижние подчеркивания “_”, <strong>это функциональная и обязательная часть</strong> имени. Всего должно быть 2 подчеркивания всегда.</p>



<p>“_БросаниеВагоновТип” – После второго подчеркивания, это имя запроса, который мы положили в макеты обработки.</p>



<p><strong>Функция ЗаполнитьПараметры</strong></p>



<p>Здесь указываем параметры подключения к нашему серверу, где хранится наша уже созданная база данных или нет.</p>



<div class="wp-block-codemirror-blocks-code-block code-block" id="1"><pre class="CodeMirror" data-setting="{&quot;mode&quot;:&quot;clike&quot;,&quot;mime&quot;:&quot;text/x-csrc&quot;,&quot;theme&quot;:&quot;material&quot;,&quot;lineNumbers&quot;:false,&quot;styleActiveLine&quot;:false,&quot;lineWrapping&quot;:false,&quot;readOnly&quot;:true,&quot;fileName&quot;:&quot;1C&quot;,&quot;language&quot;:&quot;C&quot;,&quot;modeName&quot;:&quot;c&quot;}" id="code-block-1" style="display: none;">Функция ЗаполнитьПараметры() Экспорт
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
КонецФункции</pre><div class="CodeMirror CodeMirror-simplescroll cm-s-material"><div class="CodeMirror-panel"><div class="info-panel"><span class="language c c">C</span><div class="control-panel"><span class="tool" data-tip="Full Screen"><b class="fullscreen maximize"></b></span><span class="tool" data-tip="Copy Code"><b class="copy"></b></span></div></div></div><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 36px; left: 4px;"><textarea autocorrect="off" autocapitalize="off" spellcheck="false" style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;" tabindex="0"></textarea></div><div class="CodeMirror-simplescroll-horizontal" cm-not-content="true" style="display: block; right: 0px; left: 0px;"><div style="width: 424.949px; left: 0px;"></div></div><div class="CodeMirror-simplescroll-vertical adjust-top" cm-not-content="true" style="display: none; bottom: 8px;"><div style="height: 283.5px; top: 0px;"></div></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true" style="height: 8px; width: 8px;"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px; margin-bottom: -17px; border-right-width: 13px; min-height: 462px; min-width: 769.125px; padding-right: 0px; padding-bottom: 8px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div role="presentation" style="position: relative; outline: none;"><div class="CodeMirror-measure"></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-cursors"><div class="CodeMirror-cursor" style="left: 4px; top: 0px; height: 32.3958px;">&nbsp;</div></div><div class="CodeMirror-code" role="presentation" style=""><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">Функция</span> <span class="cm-def">ЗаполнитьПараметры</span>() <span class="cm-variable">Экспорт</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-tab" role="presentation" cm-text="	">    </span><span class="cm-variable">ТекущаяДата</span> <span class="cm-operator">=</span> <span class="cm-variable">ТекущаяДата</span>();</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-tab" role="presentation" cm-text="	">    </span><span class="cm-variable">СтруктураПараметры</span> <span class="cm-operator">=</span> <span class="cm-variable">Новый</span> <span class="cm-variable">Структура</span>;</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-tab" role="presentation" cm-text="	">    </span><span class="cm-variable">СтруктураПараметры</span>.<span class="cm-variable">Вставить</span>(<span class="cm-string">"Адрес"</span>, <span class="cm-string">"IP"</span>);</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-tab" role="presentation" cm-text="	">    </span><span class="cm-variable">СтруктураПараметры</span>.<span class="cm-variable">Вставить</span>(<span class="cm-string">"Порт"</span>, <span class="cm-number">8123</span>);</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-tab" role="presentation" cm-text="	">    </span><span class="cm-variable">СтруктураПараметры</span>.<span class="cm-variable">Вставить</span>(<span class="cm-string">"Логин"</span>, <span class="cm-string">"default"</span>);</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-tab" role="presentation" cm-text="	">    </span><span class="cm-variable">СтруктураПараметры</span>.<span class="cm-variable">Вставить</span>(<span class="cm-string">"Пароль"</span>, <span class="cm-string">"password"</span>);</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-tab" role="presentation" cm-text="	">    </span><span class="cm-variable">СтруктураПараметры</span>.<span class="cm-variable">Вставить</span>(<span class="cm-string">"ИмяБазы"</span>, <span class="cm-string">"db_name"</span>);</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-tab" role="presentation" cm-text="	">    </span><span class="cm-variable">СтруктураПараметры</span>.<span class="cm-variable">Вставить</span>(<span class="cm-string">"ИмяТаблицы"</span>, <span class="cm-string">"БросаниеВагоновТип"</span>);</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" class="cm-tab-wrap-hack" style="padding-right: 0.1px;"><span class="cm-tab" role="presentation" cm-text="	">    </span></span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-tab" role="presentation" cm-text="	">    </span><span class="cm-variable">СтруктураПараметры</span>.<span class="cm-variable">Вставить</span>(<span class="cm-string">"ДатаНачала"</span>, <span class="cm-variable">ДатаДнейНазад</span>(<span class="cm-variable">ТекущаяДата</span>, <span class="cm-number">1</span>));</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-tab" role="presentation" cm-text="	">    </span><span class="cm-variable">СтруктураПараметры</span>.<span class="cm-variable">Вставить</span>(<span class="cm-string">"ДатаОкончания"</span>, <span class="cm-variable">КонецДня</span>(<span class="cm-variable">ТекущаяДата</span>));</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-tab" role="presentation" cm-text="	">    </span><span class="cm-variable">Возврат</span> <span class="cm-variable">СтруктураПараметры</span>;</span></pre><pre class=" CodeMirror-line " role="presentation"><span role="presentation" style="padding-right: 0.1px;"><span class="cm-variable">КонецФункции</span></span></pre></div></div></div></div></div><div style="position: absolute; height: 13px; width: 1px; border-bottom: 8px solid transparent; top: 462px;"></div><div class="CodeMirror-gutters" style="display: none; height: 483px;"></div></div></div></div>



<h2 class="wp-block-heading">Добавление отчетов на основе СКД</h2>



<p>Макеты -&gt; Добавить</p>



<p>Формируем или вставляем наш запрос.</p>



<h3 class="wp-block-heading">Требования</h3>



<p>Добавить в параметры своего отчета</p>



<p><strong>Всегда использовать Период, как дату, а не стандартный период в параметрах СКД.</strong></p>



<p><strong>КоличествоДнейНазад</strong> – за какое количество дней формировать отчет и обновлять записи в базе. По умолчанию = 1</p>



<p><strong>Начало и окончание дат периода</strong> должны быть обозначены <strong>Дата1 и Дата2.</strong></p>



<p>Остальные примеры для месяца и дня смотри функцию <strong>ВернутьДату_Запрос_НаСервере</strong></p>



<h2 class="wp-block-heading">Добавление обработки в информационную базу</h2>



<p>Администрирование -&gt; Дополнительные обработки и отчеты</p>



<p>Добавить из файла.</p>



<p>Для добавленных команд в таблицу команд, будет возможность использовать их как фоновое задание. Отмечаем галочками и выставляем расписание исполнения.</p>



<p>Как только сохраните обработку в таком виде, запустятся столько фоновых здание, сколько отметите галками.</p>



<p>Чтобы запустить вручную каждое, необходимо зайти в Администрирование -&gt; Обслуживание -&gt; Регламентные и фоновые задания.</p>



<p>Общая форма обработки не предусмотрена. Используйте команды и кнопки для взаимодействия по образу и подобию из нашей “боевой” обработки.</p>



<p>Have fun!</p>
