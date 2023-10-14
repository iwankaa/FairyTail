import time

# Define the story sections with different choices
story_sections = {
    "start": {
        "text": "Жила колись в одному селі маленька дівчинка, та така красуня, що кращої за неї, мабуть, ніхто й не бачив."
                "\nМати любила її до нестями, а бабуся ще більше. "
                "\nДобра бабуся зшила для внучки червону шапочку, яка була їй так до лиця, що дівчинку всі почали звати Червоною Шапочкою."
                "\nОдного разу мати напекла пиріжків і каже:",
        "choices": ["Піти до бабусі", "Залишитися вдома"],
        "transitions": ["Forest1", "Home1"]
    },
    "Forest1": {
        "text": "Червона Шапочка хутко зібралась та пішла до своєї бабусі, яка жила в іншому селі. "
                "\nЙде вона лісом, коли раптом зустрівся їй вовк. "
                "\nЙому відразу ж захотілося з'їсти дівчинку, але він не наважився це зробити, бо поблизу в лісі були лісоруби. "
                "\nОт він питає, куди вона йде.",
        "choices": ["Відповісти вовку", "Вдарити вовка палкою та піти додому"],
        "transitions": ["Forest2", "Home2"]
    },
    "Forest2": {
        "text": "Бідна дівчинка, не знаючи, що дуже небезпечно зупинятися в лісі і слухати вовка, відповідає йому:"
                "\n– Я йду навідатись до своєї бабусі й несу їй пиріжок та горщичок масла, які матуся передала їй."
                "\n– А чи далеко вона живе ? – питає вовк."
                "\n– Так, далеко, – відповідає йому Червона Шапочка, – он за тим вітряком, бачите, в першому будиночку в селі."
                "\n– Гаразд, – каже вовк, – я теж піду до неї навідаюсь. Я ось цією стежкою піду, а ти йди он тією, побачимо, хто з нас швидше прийде.",
        "choices": ["Погодитись на авантюру вовка", "Піти додому"],
        "transitions": ["HomeGrendmas1", "Home2"]
    },
    "HomeGrendmas1": {
        "text": "Вовк щосили побіг найкоротшою стежкою."
                "\n А дівчинка пішла довшою стежкою та ще гралася, збирала горіхи, бігала за метеликами і робила букети з квіточок."
                "\n Вовк миттю добіг до бабусиного будиночка і постукав у двері: тук-тук."
                "– Хто там?"
                "– Це ваша внучка, Червона Шапочка, – відповів вовк, змінивши голос. – Я принесла вам пиріжка і горщичок масла. Це матуся передала.",
        "choices": ["Повірити вовку", "Зрозуміти, шо внучка дівчинка, а не тварина"],
        "transitions": ["HomeGrendmas2", "Home3"]
    },
    "HomeGrendmas2": {
        "text": " Добра бабуся лежала в ліжку, бо справді трохи нездужала. Вона гукнула йому: "
                "\n– Смикни за мотузочку, клямка й відкриється. "
                "\nВовк смикнув за мотузочку, і двері відчинилися. "
                "\nТут він накинувся на бабусю і зжер її одразу, бо він уже понад три дні нічого не їв."
                "\nПотім зачинив двері, ліг на бабусине ліжко і почав чекати Червону Шапочку."
                "\nНезабаром дівчинка прийшла і постукала: тук-тук."
                "\n – Хто там?",
        "choices": ["Відповісти вовку", "Зрозуміти, що вабуся не гавкає"],
        "transitions": ["HomeGrendmas3", "Home4"]
    },
    "HomeGrendmas3": {
        "text": " Червона Шапочка спочатку перелякалась, почувши грубий голос вовка, але потім подумала, що, мабуть, у бабусі нежить, і відповіла:"
                "\n– Це ваша внучка, Червона Шапочка. Я принесла вам пиріжка і горщичок масла. Це матуся передала."
                "\nВовк гукнув їй трохи ніжнішим голосом:"
                "\n– Смикни за мотузочку, клямка й відкриється."
                "\nЧервона Шапочка смикнула за мотузочку, і двері відчинилися. Побачивши, що дівчинка ввійшла до кімнати, вовк сховався під ковдру та й каже:"
                "\n– Поклади пиріжок на скриню і горщичок там постав, а сама йди полеж зі мною."
                "\nЧервона Шапочка лягла в ліжко і дуже здивувалась, коли побачила, який вигляд в її бабусі.",
        "choices": ["Думати чому бабушка так схожк на вовка", "Зрозуміти, що це вовк"],
        "transitions": ["HomeGrendmas4", "Home4"]
    },
    "HomeGrendmas4": {
        "text": " – Бабусю, які ж у вас руки великі! – каже вона."
                "\n– Це щоб міцніше тебе обнімати, онученько!"
                "\n– Бабусю, які ж у вас ноги великі!"
                "\n– Це щоб краще бігати, дитинко!"
                "\n– Бабусю, які ж у вас вуха великі!"
                "\n– Це щоб краще чути, дівчинко!"
                "\n– Бабусю, які ж у вас очі великі!"
                "\n– Це щоб краще бачити, онученько!"
                "\n– Бабусю, які ж у вас зуби великі!"
                "\n– А це щоб тебе з'їсти!"
                "\nЗ цими словами злий вовк накинувся на Червону Шапочку і з'їв її."
                "\nАле на щастя, в той самий час мимо будиночка проходили лісоруби із великими сокирами.",
        "choices": ["Кричати, щоб хтось почув і прийшов на допомогу", "Змеритися з долею"],
        "transitions": ["HomeGrendmas5", "End"]
    },
"HomeGrendmas5": {
        "text": "Вони почули шум, вбігли до будиночка та вбили вовка."
                "\nА потім розрізали йому черево, а звідти вилізли бабуся й Червона Шапочка, живі та здорові.",
        "choices": ["The Кінець"],
        "transitions": ["End"]
    },
    "Home1": {
        "text": "Мама сама пішла до бабусі, а шапочку вигнали з дому",
        "choices": ["The Кінець"],
        "transitions": ["End"]
    },
    "Home2": {
        "text": "Коли шакочка прийшла додому, вона розповіда мамі, що сталося в лікі, і та в свою чергу похвалила дочку.",
        "choices": ["The Кінець"],
        "transitions": ["End"]
    },
    "Home3": {
        "text": "Бабуся не відчинила вовку, а зразу покликала на допомогу, врятувавши себе та свою онучку",
        "choices": ["The Кінець"],
        "transitions": ["End"]
    },
    "Home4": {
        "text": "Шапочка зрозуміла, що бабуся знахидиться у небезпеці та покликала на допомогу лісорубів. Вони швидко прибігли та врятували бабусю",
        "choices": ["The Кінець"],
        "transitions": ["End"]
    },
    "End": {
        "text": "The end of the story.",
        "choices": [],
        "transitions": []
    }
}

class PetriNet:
    def __init__(self):
        self.places = {"Start": 1, "Home": 0, "Lake": 0, "Forest": 0, "End": 0}

    # ... (other methods remain the same)

if __name__ == "__main__":
    petri_net = PetriNet()
    current_section = "start"

    print("Вітаємо в симутялорі казки")
    time.sleep(1)
    print("Влаштовуйтесь зручніше, щоб поринути у прекрасний світ казки Черврна шапочка")
    time.sleep(2)
    print("А ми починаємо")
    time.sleep(1)

    while current_section != "End":
        section = story_sections[current_section]
        print(section["text"])
        for i, choice in enumerate(section["choices"]):
            print(f"{i + 1}. {choice}")

        choice_num = input("Виберіть варіант (введіть номер): ")
        if choice_num.isdigit():
            choice_num = int(choice_num)
            if 1 <= choice_num <= len(section["choices"]):
                transition = section["transitions"][choice_num - 1]
                current_section = transition
            else:
                print("Невірний вибір.")
        else:
            print("Будь ласка, введіть номер варіанту.")
