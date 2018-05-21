def get_answer(question, answers={"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}):
    try:
        low_question = str(question).lower()
        return answers[low_question]
    except Exception as e:
        return 'Something bad happened'

print(get_answer('ПРИВЕТ'))
print(get_answer('GHBDTN'))