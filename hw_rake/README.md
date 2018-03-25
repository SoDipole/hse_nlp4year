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

#### Топ 15 RAKE:

kw | rating
-- | ------
friend eva wichman  |  9.0
red ruby hidden  |  9.0
fierce work ethic  |  8.0
moomins characters brand  |  7.7
strong female characters  |  7.7
calmly confident moominmamma  |  7.5
finn family moomintroll  |  7.333333333333334
female characters  |  4.7
moomin brand  |  4.5
quell moomintroll  |  4.333333333333334
recognise moomintroll  |  4.333333333333334
characters thingumy  |  4.2
deep understanding  |  4.0
necessarily easy  |  4.0
walt disney  |  4.0

#### Изменения алгоритма:
- небольшие изменения в принципе деления на предложения
- убираются дополнительные типы кавычек
- лемматизация (WordNetLemmatizer из nltk)
