from app.Pet_friends import Pet_friends
from valid_data import valid_email, valid_password
import os

pf = Pet_friends()

def test_get_api_key_status(email=valid_email, password=valid_password):
    """ Проверяем что запрос api ключа возвращает статус 200 и в результате содержится слово key"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)
    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert "key" in result

def test_get_all_pets_with_valid_key(filter=''):
    """ Проверяем что запрос всех питомцев возвращает не пустой список.
    Для этого сначала получаем api ключ и сохраняем в переменную auth_key. Далее используя этого ключ
    запрашиваем список всех питомцев и проверяем что список не пустой."""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)

    assert status == 200
    assert len(result['pets']) > 0

def test_add_new_pet_with_valid_data(name='Барбоскин', animal_type='двортерьер',
                                     age="4", pet_photo='images/cat1.jpg'):
    """Проверяем что можно добавить питомца с корректными данными"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name

def test_successful_delete_self_pet():
    """Проверяем возможность удаления питомца"""

    # Получаем ключ auth_key и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем - если список своих питомцев пустой, то добавляем нового и опять запрашиваем список своих питомцев
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, "Суперкот", "кот", "3", "images/cat1.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Берём id первого питомца из списка и отправляем запрос на удаление
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    # Ещё раз запрашиваем список своих питомцев
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем что статус ответа равен 200 и в списке питомцев нет id удалённого питомца
    assert status == 200
    assert pet_id not in my_pets.values()

def test_successful_update_self_pet_info(name='Мурзик', animal_type='Котэ', age=5):
    """Проверяем возможность обновления информации о питомце"""

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Если список не пустой, то пробуем обновить его имя, тип и возраст
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        # Проверяем что статус ответа = 200 и имя питомца соответствует заданному
        assert status == 200
        assert result['name'] == name
    else:
        # если спиок питомцев пустой, то выкидываем исключение с текстом об отсутствии своих питомцев
        raise Exception("Нет моих питомцев")

def test_get_my_pets_with_filter_my_pets(filter='my_pets'):
    """ Проверяем фильтр "мои питомцы".
    Для этого сначала получаем api ключ и сохраняем в переменную auth_key. Далее используя этого ключ
    запрашиваем список своих питомцев и проверяем что список не пустой.
    Доступное значение параметра filter - 'my_pets'"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.get_list_of_pets(auth_key, filter)
    if len(my_pets["pets"]) > 0:
        assert status == 200
    else:
        assert status == 200
        raise Exception("Пустой список 'Мои питомцы'")

def test_get_api_key_status_no_valid_pass(email=valid_email, password="No_valid"):
    """Проверяем что запрос api с не правльным паролем выдает ошибку"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status
    status = pf.get_api_key(email, password)
    # Сверяем что статус код не равен 200
    assert status != 200
    raise Exception("Не правильный ввод password")

def test_add_new_pet_with_no_valid_data(name='КотоПес', animal_type='',
                                     age='56', pet_photo='images/cat1.jpg'):
    """Проверяем что нельзя добавить питомца с пустым полем Порода"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    if status == 200:
        raise Exception("Нельзя добавлять питомца с пустым полем Порода")

def test_add_new_pet_no_photo(name='Мальчик', animal_type='Тип',
                                     age='4'):
    """Проверяем что можно добавить питомца с корректными данными без фото"""

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_not_photo(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name

def test_add_photo_for_id_my_pets(pet_photo='images/cat1.jpg'):
    """Проверяем добовления фото нашему питомцу"""

    # Запрашиваем ключ api и сохраняем в переменую auth_key, и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Проверяем - если список своих питомцев пустой, то добавляем нового и опять запрашиваем список своих питомцев
    if len(my_pets['pets']) == 0:
        pf.add_new_pet_not_photo(auth_key, "Суперкот", "кот", "3")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

        pet_id = my_pets['pets'][0]['id']
        status, result = pf.add_photo_for_id_pets(auth_key, pet_id, pet_photo)
        return status, result
    else:
        # Берём id первого питомца из списка и отправляем запрос добавления фото
        pet_id = my_pets['pets'][0]['id']
        status, result = pf.add_photo_for_id_pets(auth_key, pet_id, pet_photo)
        # Сверяем полученный ответ с ожидаемым результатом
        return status, result
    assert status == 200
    assert my_pets["pets"][0]["id"] in result

def test_add_photo_for_id_any_pets(pet_photo='images/cat1.jpg'):
    """Проверяем добовления фото случайному питомцу"""

    # Запрашиваем ключ api и сохраняем в переменую auth_key, и запрашиваем список всех питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, list_pets = pf.get_list_of_pets(auth_key, "")

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Берём id первого питомца из списка и отправляем запрос добавления фото
    pet_id = list_pets['pets'][0]['id']
    status, _ = pf.add_photo_for_id_pets(auth_key, pet_id, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    if status == 200:
        raise Exception("Попался наш питомиц, изменить Ид на другое")
    else:
        raise Exception("Нельзя менять фото любому питомцу")

def test_get_api_key_status_no_valid_email(email="No_valid", password=valid_password):
    """Проверяем что запрос api с не правльным паролем выдает ошибку"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status
    status = pf.get_api_key(email, password)
    # Сверяем что статус код не равен 200
    assert status != 200
    raise Exception("Не правильный ввод email")

def test_add_new_pet_no_valid_age_date(name='Боря', animal_type='Брат',
                                     age='пять'):
    """Проверяем что нельзя добавить питомца возраст которого указан буквами """

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_not_photo(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом

    if result['age'] == age:
        raise Exception("Некорректный ввод данных, нельзя в возрасте буквы")

def test_add_new_pet_no_valid_name_date(name='', animal_type='Брат',
                                     age='5'):
    """Проверяем что нельзя добавить питомца c пустым поля Имя """

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_not_photo(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом

    if result['name'] == name:
        raise Exception("Некорректный ввод данных, нельзя чтобы поля Имя было пустым")

def test_add_new_pet_no_valid_animal_type_date(name='Боря', animal_type='',
                                     age='пять'):
    """Проверяем что нельзя добавить питомца без названия породы """

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_not_photo(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом

    if result['animal_type'] == animal_type:
        raise Exception("Некорректный ввод данных, нельзя чтобы поле Порода было пустым")