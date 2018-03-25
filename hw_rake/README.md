# RAKE homework
### Выполнили Сонина Полина и Клименко Светлана

Текст: moomins.txt

Процент совпадения ручных разметок: 0.277


#### Сравнения

топ 15 ручная разметка | RAKE | RAKE mod
---------------------- | ---- | --------
bold decisions | 0 | 0
embrace independence | 0 | 0
feminist | 0 | 0
feminist role model | 0 | 0
fierce work ethic | 1 | 1
find power | 0 | 0
forbidden love | 0 | 0
lesbian | 0 | 0
moomin | 0 | 0
moominmamma | 0 | 0
moomintroll | 0 | 0
mother | 0 | 0
strong female characters | 1 | 1
tove jansson | 0 | 0
women | 0 | 0

Индекс совпадения топ 15 с оригинальным рейком: 0.133

#### Топ 15 RAKE vs топ 15 RAKE mod:

топ 15 RAKE | топ 15 RAKE mod
----------- | ---------------
friend eva wichman | strong female characters
red ruby hidden | moomins characters brand
fierce work ethic | signe hammarsten jansson
strong female characters | post war stories
moomins characters brand | calmly confident moominmamma
calmly confident moominmamma | finn family moomintroll
finn family moomintroll | friend eva wichman
female characters | red ruby hidden
moomin brand | fierce work ethic
recognise moomintroll | long term partner
quell moomintroll | female characters
characters thingumy | sophia jansson
signe hammarsten | characters thingumy
inseparable creatures | jansson wrote
moomin artwork | moomin stories

Количество чистых совпадений не изменилось, зато ключевые фразы выглядят более качественными и их порядок более логичным.


#### Изменения алгоритма:
- небольшие изменения в принципе деления на предложения
- убираются дополнительные типы кавычек
- лемматизация (WordNetLemmatizer из nltk)
- изменения в расчёте весов ключевых фраз

#### Обработка русского текста

Как оказалось, при запускании совсем базового rake, не обрабатываются русские стоп-слова и не считается рейтинг ключевых слов. 
Чтобы исправить это, в исходном коде нужно было дописать расширение файла со стоп-словами и добавить в регулярные выражения кириллический алфавит. 

Но и после этого список ключевых слов выглядит немного странно. Предпочтение отдано длинным, не всегда похожим на ключевые слова, коллокациям, что связано, вероятно, с отсутствием лемматизации и, как следствие, редкой повторяемостью токенов. 

Кроме лемматизации надо обновить список пунктуации, добавив туда специфические кавычки-елочки и длинное тире.
