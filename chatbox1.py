
from nltk.chat.util import Chat,reflections

pairs=[
    [
        r"(.*)my name is (.*)",
        ["Hello %2, How are you today ?", ]
    ],
    [
        r"(.*)help(.*) ",
        ["I can help you ", ]
    ],
    [
        r"(.*) your name ?",
        ["My name is J.A.R.V.I.S like in Iron Man, but you can just call me Jarvis and I'm a chatbot .", ]
    ],
    [
        r"how are you (.*) ?",
        ["I'm doing very well", "i am great !"]
    ],
    [
        r"sorry (.*)",
        ["Its alright", "Its OK, never mind that", ]
    ],
    [
        r"i'm (.*) (good|well|okay|ok)",
        ["Nice to hear that", "Alright, great !", ]
    ],
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello", "Hey there", ]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse", ]

    ],
    [
        r"(.*)created(.*)",
        ["randerson112358 created me using Python's NLTK library ", "top secret ;)", ]
    ],
    [
        r"(.*) (location|city) ?",
        ['Tokyo, Japan', ]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain in the past 4 days here in %2", "In %2 there is a 50% chance of rain", ]
    ],
    [
        r"how (.*) health (.*)",
        ["Health is very important, but I am a computer, so I don't need to worry about my health ", ]
    ],
    [
        r"(.*)(sports|game|sport)(.*)",
        ["I'm a very big fan of Basketball", ]
    ],
    [
        r"who (.*) (moviestar|actor|actress)?",
        ["Zendaya"]
    ],
    [
        r"quit",
        ["Bye for now. See you soon :) ", "It was nice talking to you. See you soon :)"]
    ],
    [
        r"(.*)",
        ['That is nice to hear']
    ],




]

tr_pairs = [
    ["benim adim (.*)",["merhaba"]],
    [" (.*)adın (ne|nedir)?",["benim adım çetin"]],
    [" (.*)merhaba|",["hosgeldin"]],
    ["bitti",[""]],
    [" (.*)nerede yaşıyorsun?",["istanbul da yaşıyorum"]],
    [" (.*)nerelisin?",["ben bir sohbet botuyum dogum yerim yok"]],
    [" (.*) kac yasındasın?",["ben bir sohbet botuyum dogum yerim yok"]],
    [" (.*)hava nasıl?",["bügün hava güneşli"]],
    [" (.*)nasılsın?",["iyim teşekkür ederim sen nasılsın?"]],
    [" (.*) yardım edermisin?",["elbette yardım ederim"]]



]


tr_reflections={...}

#orjinal
print(reflections)
chat = Chat(tr_pairs,tr_reflections)
chat.converse(quit="bitti")
