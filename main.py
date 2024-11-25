import requests


class TestChuckNorrisJokes:
    def __init__(self, base_url):
        self.base_url = base_url

    def random_joke_from_category(self, joke_category):
        # получение случайной шутки по определенной категории
        url_category = f"{self.base_url}/random?category={joke_category}"
        result = requests.get(url_category)
        result.encoding = "utf-8"
        print(f"Ответ на запрос:\n{result.json()}")

        # проверка статус-кода
        assert result.status_code == 200, \
            "Ошибка: Ожидаемый результат ответа - код 200."
        print(f"Статус код: {result.status_code}")

        # проверка на соответствие категории
        get_category_from_result = result.json()["categories"][0]
        assert get_category_from_result == joke_category, \
            "Ошибка: Категория должна совпадать!"
        print(f"Категория соответствует выбранной - \"{get_category_from_result}\".")

        # проверка на содержании имени Chuck в теле шутки
        name_in_joke = "Chuck"
        assert name_in_joke in (result.json()["value"]), \
            "Ошибка: Имя Chuck должна содержаться в шутке!"
        print(f"Имя \"{name_in_joke}\" содержится в шутке.")

        # вывод на печать самой шутки
        print(f"Шутка с Чаком:\n{result.json()["value"]}")


"""
joke categories: "animal", "career", "celebrity", "dev", "explicit",
"fashion", "food", "history", "money", "movie", "music", "political",
"religion", "science", "sport", "travel".
"""

if __name__ == "__main__":
    base_url = "https://api.chucknorris.io/jokes"
    start_test = TestChuckNorrisJokes(base_url)
    start_test.random_joke_from_category(joke_category="sport")
