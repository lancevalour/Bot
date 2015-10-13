import duckduckgo


class Bot:

    def __init__(self):
        self.type_answer = 'answer'
        self.type_disambiguation = 'disambiguation'
        self.type_nothing = 'nothing'

    def answer(self, question):
        result = duckduckgo.query(question)
        result_type = result.type
        if result_type is self.type_answer:
            return result.abstract.text
        elif result_type is self.type_disambiguation:
            return result.related[0].text
        elif result_type is self.type_nothing:
            return result.answer.text


bot = Bot()
print(bot.answer("facebook"))
