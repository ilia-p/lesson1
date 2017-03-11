def get_answer(question):
	answer={'Привет': 'И тебе привет!', 'как дела':'Лучше всех', 'пока':'Увидимся'}
	a=answer[question].lower()
	return a
question=input('Введите вопрос: ')
x=get_answer(question)
print (x)