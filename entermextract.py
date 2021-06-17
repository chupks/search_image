import re

from nltk.tokenize import WordPunctTokenizer as WPT
from nltk.corpus import stopwords as SW
from nltk.corpus import brown
from json import load, dump

stopwords = set(SW.words('english'))

wpt = WPT()

a_text = '''Since the invention of computers or machines, their capability to perform various tasks went on growing exponentially. Humans have developed the power of computer systems in terms of their diverse working domains, their increasing speed, and reducing size with respect to time.

A branch of Computer Science named Artificial Intelligence pursues creating the computers or machines as intelligent as human beings.
What is Artificial Intelligence?

According to the father of Artificial Intelligence, John McCarthy, it is “The science and engineering of making intelligent machines, especially intelligent computer programs”.

Artificial Intelligence is a way of making a computer, a computer-controlled robot, or a software think intelligently, in the similar manner the intelligent humans think.

AI is accomplished by studying how human brain thinks, and how humans learn, decide, and work while trying to solve a problem, and then using the outcomes of this study as a basis of developing intelligent software and systems.
Philosophy of AI

While exploiting the power of the computer systems, the curiosity of human, lead him to wonder, “Can a machine think and behave like humans do?”

Thus, the development of AI started with the intention of creating similar intelligence in machines that we find and regard high in humans.
Goals of AI

    To Create Expert Systems − The systems which exhibit intelligent behavior, learn, demonstrate, explain, and advice its users.

    To Implement Human Intelligence in Machines − Creating systems that understand, think, learn, and behave like humans.

What Contributes to AI?

Artificial intelligence is a science and technology based on disciplines such as Computer Science, Biology, Psychology, Linguistics, Mathematics, and Engineering. A major thrust of AI is in the development of computer functions associated with human intelligence, such as reasoning, learning, and problem solving.

Out of the following areas, one or multiple areas can contribute to build an intelligent system.
Components of AI
Programming Without and With AI

The programming without and with AI is different in following ways −
Programming Without AI 	Programming With AI
A computer program without AI can answer the specific questions it is meant to solve. 	A computer program with AI can answer the generic questions it is meant to solve.
Modification in the program leads to change in its structure. 	AI programs can absorb new modifications by putting highly independent pieces of information together. Hence you can modify even a minute piece of information of program without affecting its structure.
Modification is not quick and easy. It may lead to affecting the program adversely. 	Quick and Easy program modification.
What is AI Technique?

In the real world, the knowledge has some unwelcomed properties −

    Its volume is huge, next to unimaginable.
    It is not well-organized or well-formatted.
    It keeps changing constantly.

AI Technique is a manner to organize and use the knowledge efficiently in such a way that −

    It should be perceivable by the people who provide it.
    It should be easily modifiable to correct errors.
    It should be useful in many situations though it is incomplete or inaccurate.

AI techniques elevate the speed of execution of the complex program it is equipped with.
Applications of AI

AI has been dominant in various fields such as −

    Gaming − AI plays crucial role in strategic games such as chess, poker, tic-tac-toe, etc., where machine can think of large number of possible positions based on heuristic knowledge.

    Natural Language Processing − It is possible to interact with the computer that understands natural language spoken by humans.

    Expert Systems − There are some applications which integrate machine, software, and special information to impart reasoning and advising. They provide explanation and advice to the users.

    Vision Systems − These systems understand, interpret, and comprehend visual input on the computer. For example,

        A spying aeroplane takes photographs, which are used to figure out spatial information or map of the areas.

        Doctors use clinical expert system to diagnose the patient.

        Police use computer software that can recognize the face of criminal with the stored portrait made by forensic artist.

    Speech Recognition − Some intelligent systems are capable of hearing and comprehending the language in terms of sentences and their meanings while a human talks to it. It can handle different accents, slang words, noise in the background, change in human’s noise due to cold, etc.

    Handwriting Recognition − The handwriting recognition software reads the text written on paper by a pen or on screen by a stylus. It can recognize the shapes of the letters and convert it into editable text.

    Intelligent Robots − Robots are able to perform the tasks given by a human. They have sensors to detect physical data from the real world such as light, heat, temperature, movement, sound, bump, and pressure. They have efficient processors, multiple sensors and huge memory, to exhibit intelligence. In addition, they are capable of learning from their mistakes and they can adapt to the new environment.

History of AI

Here is the history of AI during 20th century −
Year 	Milestone / Innovation
1923 	

Karel Čapek play named “Rossum's Universal Robots” (RUR) opens in London, first use of the word "robot" in English.
1943 	

Foundations for neural networks laid.
1945 	

Isaac Asimov, a Columbia University alumni, coined the term Robotics.
1950 	

Alan Turing introduced Turing Test for evaluation of intelligence and published Computing Machinery and Intelligence. Claude Shannon published Detailed Analysis of Chess Playing as a search.
1956 	

John McCarthy coined the term Artificial Intelligence. Demonstration of the first running AI program at Carnegie Mellon University.
1958 	

John McCarthy invents LISP programming language for AI.
1964 	

Danny Bobrow's dissertation at MIT showed that computers can understand natural language well enough to solve algebra word problems correctly.
1965 	

Joseph Weizenbaum at MIT built ELIZA, an interactive problem that carries on a dialogue in English.
1969 	

Scientists at Stanford Research Institute Developed Shakey, a robot, equipped with locomotion, perception, and problem solving.
1973 	

The Assembly Robotics group at Edinburgh University built Freddy, the Famous Scottish Robot, capable of using vision to locate and assemble models.
1979 	

The first computer-controlled autonomous vehicle, Stanford Cart, was built.
1985 	

Harold Cohen created and demonstrated the drawing program, Aaron.
1990 	

Major advances in all areas of AI −

    Significant demonstrations in machine learning
    Case-based reasoning
    Multi-agent planning
    Scheduling
    Data mining, Web Crawler
    natural language understanding and translation
    Vision, Virtual Reality
    Games

1997 	

The Deep Blue Chess Program beats the then world chess champion, Garry Kasparov.
2000 	

Interactive robot pets become commercially available. MIT displays Kismet, a robot with a face that expresses emotions. The robot Nomad explores remote regions of Antarctica and locates meteorites.'''

r_text = '''С момента изобретения компьютеров или машин их способность выполнять различные задачи росла в геометрической прогрессии. Люди развили мощь компьютерных систем с точки зрения их разнообразных рабочих областей, их растущей скорости и уменьшения размера по отношению ко времени.

Отрасль компьютерных наук, называемая искусственным интеллектом, преследует цель создания компьютеров или машин, столь же интеллектуальных, как и люди.
Что такое искусственный интеллект?

По словам отца искусственного интеллекта Джона Маккарти, это “наука и техника создания интеллектуальных машин, особенно интеллектуальных компьютерных программ".

Искусственный интеллект-это способ заставить компьютер, управляемого компьютером робота или программное обеспечение мыслить разумно, подобно тому, как мыслят разумные люди.

ИИ достигается путем изучения того, как человеческий мозг мыслит и как люди учатся, принимают решения и работают, пытаясь решить проблему, а затем используют результаты этого исследования в качестве основы для разработки интеллектуального программного обеспечения и систем.
Философия ИИ

Используя мощь компьютерных систем, любопытство человека заставляет его задуматься: “Может ли машина думать и вести себя так, как люди?”

Таким образом, развитие ИИ началось с намерения создать подобный интеллект в машинах, который мы находим и высоко ценим у людей.
Цели ИИ

    Для создания экспертных систем − систем, которые демонстрируют интеллектуальное поведение, учатся, демонстрируют, объясняют и консультируют своих пользователей.

    Внедрять человеческий интеллект в машины − создавать системы, которые понимают, думают, учатся и ведут себя как люди.

Что способствует развитию ИИ?

Искусственный интеллект-это наука и технология, основанная на таких дисциплинах, как информатика, биология, Психология, лингвистика, математика и инженерия. Основная направленность ИИ заключается в развитии компьютерных функций, связанных с человеческим интеллектом, таких как рассуждение, обучение и решение проблем.

Из следующих областей одна или несколько областей могут способствовать созданию интеллектуальной системы.
Компоненты
программирования ИИ Без ИИ и с ИИ

Программирование без ИИ и с ним отличается следующими способами:
Программирование Без ИИ Программирование с ИИ
Компьютерная программа без искусственного интеллекта может ответить на конкретные вопросы, для решения которых она предназначена. 	Компьютерная программа с искусственным интеллектом может ответить на общие вопросы, для решения которых она предназначена.
Модификация программы приводит к изменению ее структуры. 	Программы искусственного интеллекта могут поглощать новые модификации, объединяя очень независимые фрагменты информации. Следовательно, вы можете изменить даже мельчайшую часть информации программы, не влияя на ее структуру.
Модификация не является быстрой и легкой. Это может привести к неблагоприятному влиянию на программу. 	Быстрая и простая модификация программы.
Что такое техника ИИ?

В реальном мире знание обладает некоторыми нежелательными свойствами −

    Его объем огромен, почти невообразим.
    Он не очень хорошо организован и не очень хорошо отформатирован.
    Он постоянно меняется.

Техника ИИ −это способ организации и эффективного использования знаний таким образом, чтобы -

    Она должна быть воспринята людьми, которые ее предоставляют.
    Он должен быть легко модифицируемым для исправления ошибок.
    Он должен быть полезен во многих ситуациях, хотя он неполный или неточный.

Методы искусственного интеллекта повышают скорость выполнения сложной программы, которой он оснащен.
Применение ИИ

ИИ доминирует в различных областях, таких как −

    Игровой ИИ играет решающую роль в стратегических играх, таких как шахматы, покер, крестики − нолики и т. Д., Где машина может думать о большом количестве возможных позиций, основанных на эвристических знаниях.

    Обработка естественного языка − Можно взаимодействовать с компьютером, который понимает естественный язык, на котором говорят люди.

    Экспертные системы − Существуют некоторые приложения, которые интегрируют машины, программное обеспечение и специальную информацию для передачи аргументации и рекомендаций. Они предоставляют пользователям разъяснения и советы.

    Системы зрения − Эти системы понимают, интерпретируют и воспринимают визуальный ввод на компьютере. Например,

        Шпионский самолет делает фотографии, которые используются для получения пространственной информации или карты местности.

        Врачи используют клиническую экспертную систему для диагностики пациента.

        Полиция использует компьютерное программное обеспечение, которое может распознать лицо преступника по сохраненному портрету, сделанному судебным художником.

    Распознавание речи − Некоторые интеллектуальные системы способны слышать и понимать язык в терминах предложений и их значений, пока человек разговаривает с ним. Он может обрабатывать различные акценты, жаргонные слова, шум на заднем плане, изменение шума человека из-за холода и т. Д.

    Распознавание рукописного текста − Программное обеспечение для распознавания рукописного текста считывает текст, написанный на бумаге ручкой или на экране стилусом. Он может распознавать формы букв и преобразовывать их в редактируемый текст.

    Интеллектуальные роботы − Роботы способны выполнять задачи, поставленные человеком. У них есть датчики для обнаружения физических данных из реального мира, таких как свет, тепло, температура, движение, звук, удар и давление. У них есть эффективные процессоры, множество датчиков и огромная память, чтобы продемонстрировать интеллект. Кроме того, они способны учиться на своих ошибках и могут адаптироваться к новой среде.

История ИИ

Вот история ИИ в течение 20 −го века -
Веха года / Инновации
1923 	

Пьеса Карела Чапека под названием “Универсальные роботы Россума” (RUR) открывается в Лондоне, впервые используя слово "робот" на английском языке.
1943 	

Заложены основы нейронных сетей.
1945 	

Айзек Азимов, выпускник Колумбийского университета, придумал термин "Робототехника".
1950 	

Алан Тьюринг представил тест Тьюринга для оценки интеллекта и опубликовал компьютерную технику и интеллект. Клод Шеннон опубликовал Подробный анализ игры в шахматы в качестве поиска.
1956 	

Джон Маккарти ввел термин "Искусственный интеллект". Демонстрация первой запущенной программы искусственного интеллекта в Университете Карнеги-Меллона.
1958 	

Джон Маккарти изобретает язык программирования LISP для ИИ.
1964 	

Диссертация Дэнни Боброу в Массачусетском технологическом институте показала, что компьютеры могут достаточно хорошо понимать естественный язык, чтобы правильно решать задачи по алгебре.
1965 	

Джозеф Вайценбаум из Массачусетского технологического института создал ELIZA, интерактивную проблему, которая ведет диалог на английском языке.
1969 	

Ученые из Стэнфордского исследовательского института разработали робота Shakey, оснащенного двигательными способностями, восприятием и решением проблем.
1973 	

Группа сборочной робототехники Эдинбургского университета построила Фредди, знаменитого шотландского робота, способного использовать зрение для поиска и сборки моделей.
1979 	

Был построен первый автономный автомобиль с компьютерным управлением-Стэнфордская тележка.
1985 	

Гарольд Коэн создал и продемонстрировал программу рисования Аарона.
1990 	

Основные достижения во всех областях ИИ −

    Значительные демонстрации в области машинного обучения
    Аргументация на основе конкретных случаев
    Многоагентное планирование
    Планирование
    Интеллектуальный анализ данных,
понимание и перевод естественного языка веб-искателя
    Видение, Виртуальная Реальность
    Игры

1997 	

Программа Deep Blue Chess обыгрывает тогдашнего чемпиона мира по шахматам Гарри Каспарова.
2000 	

Интерактивные домашние животные-роботы становятся коммерчески доступными. MIT показывает Kismet, робота с лицом, которое выражает эмоции. Робот-кочевник исследует отдаленные районы Антарктиды и находит метеориты.'''

class TermExtractor():
    
    def __collect_word_frequrencies(self, _in):
        the_corpora = self.__parse_text(_in)
        frequrencies = []

        for n in range(1,5):
            n_gramms = [ the_corpora[i:i+n] for i in range(len(the_corpora)) ]
            for n_gramm in n_gramms:
                frequrencies += [(tuple(n_gramm), n_gramms.count(n_gramm))]


        freq_dict = {}

        for n_gramm, f in frequrencies:
            if f > 1:
                k = " ".join(n_gramm)
                freq_dict.update({k: f})
        
        return freq_dict
        
    def __parse_text(self, src):
        return [ x for x in ( x.lower() for x in src ) if re.match(r'\w+',x) and x not in stopwords ]
    
    def __init__(self):
        try:
            self.freq_dict = load(open('freq_dict.json'))
        except FileNotFoundError:
            self.freq_dict = self.__collect_word_frequrencies(wpt.tokenize(open("ai.txt").read()))
            dump(self.freq_dict, open('freq_dict.json','w'), indent=2)    

    def __call__(self, a_text, strings=1, limit=None):
        tokens = self.__parse_text(wpt.tokenize(a_text))
        
        local_frequrencies = []
        for n in range(1,5):
            n_gramms = [ tokens[i:i+n] for i in range(len(tokens)) ]
            for n_gramm in n_gramms:
                local_frequrencies += [(tuple(n_gramm), n_gramms.count(n_gramm))]
                
        local_frequrencies = set(local_frequrencies)
        
        kw = []
        n = 0
        for n_gramm, f0 in local_frequrencies:
            k = " ".join(n_gramm)
            try:
                f1 = self.freq_dict[k]
                f = f0 * f1
                if f:
                    kw += [(k, f0)]
            except KeyError:
                if f0 > 2:
                    kw += [(k, f0)]
            n += 1
                    
        kw = [ x[0] for x in sorted(kw, key=lambda x:x[1], reverse=1) ]
        if limit:
            kw = kw[0:limit]
        return kw
    
if __name__ == '__main__':
    te = TermExtractor()
    print([ x for x in te(a_text) if x.count(' ') > 0 ])
    
    from rutermextract import TermExtractor as TE
    te = TE()
    print([ x for x in te(r_text,strings=1) if x.count(' ') > 0 ])
    
