from gingerit.gingerit import GingerIt
def correct(text):
    new_text = GingerIt().parse(text)
    print(f"Text before change: {text}")
    print(f"Text after change: {new_text['result']}")
    return new_text['result']
correct("Hello my name are Mostfa Jenhani and I is a compter science engineerig student, I are 23 years old , I loves gaming and gambling ")