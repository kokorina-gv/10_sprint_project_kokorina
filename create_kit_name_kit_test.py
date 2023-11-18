import sender_stand_request
import data


def get_kit_body_new(name):
    # копирую словарь с телом запроса из файла data, чтобы не потерять данные в исходном словаре
    current_kit_body = data.kit_body.copy()
    # изменение значения в поле name
    current_kit_body["name"] = name
    # возвращается новый словарь с нужным значением name
    return current_kit_body


# Функция позитивной проверки
def positive_assert(name):
    # Вызываю функцию копирования тела нового набора и передачу нового имени набора
    kit_body_new = get_kit_body_new(name)
    # В переменную kit_response сохраняю результат на создание набора
    kit_response = sender_stand_request.post_new_kit(kit_body_new)
    assert kit_response.status_code == 201

    # Проверяю, что в ответе есть поле name, и оно не пустое
    assert kit_response.json()["name"] == kit_body_new["name"]
    assert kit_response.json()["name"] != ""


# Функция негативной проверки
def negative_assert_code_400(name):
    # копирую словарь с телом запроса из файла data, чтобы не потерять данные в исходном словаре
    kit_body_new = get_kit_body_new(name)
    # В переменную kit_response сохраняю результат на создание набора
    response = sender_stand_request.post_new_kit(kit_body_new)
    assert response.status_code == 400
    # Проверяю, что в теле ответа атрибут "code" равен 400
    assert response.json()["code"] == 400


# Функция для негативной проверки, когда в ответе ошибка: "Не все необходимые параметры
def negative_assert_no_name(kit_body):
    # В переменную response сохраняется результат
    response = sender_stand_request.post_new_kit(kit_body)
    # Проверяю, что код ответа равен 400
    assert response.status_code == 400

    # Проверяется, что в теле ответа атрибут "code" равен 400
    assert response.json()[code] == 400


# Тест №1. Допустимое количество символов в поле:
# kit_body = {
# "name": "a"
# }
def test_create_kit_name_one_symbol():
    positive_assert("a")

# Тест №2. Допустимое количество символов (511):
# kit_body = {
# "name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"
# }
def test_create_kit_name_max_symbols():
    positive_assert(
        "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"
    )

# Тест 3. Количество символов меньше допустимого (0):
# kit_body = {
# "name": ""
# }
def test_create_kit_name_zero_symbols():
    body = kit_body("")
    negative_assert(body)


# Тест 4. Количество символов больше допустимого (512):
# kit_body = {
# "name":"AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"
# }
def test_create_kit_name_more_max_symbols():
    body = kit_body(
        "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    negative_assert(body)


# Тест 5. Разрешены английские буквы:
# kit_body = {
# "name": "QWErty"
# }
def test_create_kit_name_english_letters():
    positive_assert("QWErty")


# Тест 6. Разрешены русские буквы:
# kit_body = {
# "name": "Мария"
# }
def test_create_kit_name_russian_letters():
    positive_assert("Мария")


# Тест 7. Разрешены спецсимволы:
# kit_body = {
# "name": ""№%@","
# }
def test_create_kit_name_specifical_symbols():
    positive_assert("№%@", )


# Тест 8. Разрешены пробелы:
# kit_body = {
# "name": " Человек и КО "
# }
def test_create_kit_name_white_spaces():
    positive_assert(" Человек и КО ")


# Тест 9. Разрешены цифры:
# kit_body = {
# "name": "123"
# }
def test_create_kit_name_numbers():
    positive_assert("123")


# Тест 10. Параметр не передан в запросе:
# kit_body = {
# }
def test_create_kit_name_empty_body():
    kit_body = empty_body()
    negative_assert(kit_body)


# Тест 11. Передан другой тип параметра (число):
# kit_body = {
# "name": 123
# }
def test_create_kit_invalid_type():
    body = kit_body(123)
    negative_assert(body)
