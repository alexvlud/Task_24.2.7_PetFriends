from api import PetFriends
from settings import valid_email, valid_password, wrong_password

pf = PetFriends()

#             Тесты из юнита

def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result


def test_get_all_pets_with_valid_key(filter=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0


def test_add_new_pet_with_valid_key(name='Дуня', animal_type='кошка', age=23, photo='images\cat.jpg'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_information_about_new_pet(auth_key, name, animal_type, age, photo)
    assert status == 200
    assert result['name']==name
    assert result['animal_type']==animal_type
    assert result['age'] == str(age)

def test_delete_last_mypet_with_valid_key(pet_id=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets'])>0:
        status = pf.delete_pet_from_database(auth_key, my_pets['pets'][0]['id'])
        assert status == 200
        #assert 'id' in result
    else:
        raise Exception("There is no my pets")


def test_update_mypet_information_with_valid_key(name='Дуня-обновленная',
                                                 animal_type='кошка',
                                                 age=25,
                                                 pet_id=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) > 0:
        status, result = pf.update_information_about_pet(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        assert status == 200
        assert result['name'] == name
        assert result['animal_type'] == animal_type
        assert result['age'] == str(age)
    else:
        raise Exception("There is no my pets")

def test_add_new_pet_without_photo_with_valid_key(name='Муня', animal_type='песель', age=123):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_information_about_new_pet_without_photo(auth_key, name, animal_type, age)
    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == str(age)

def test_add_photo_of_pet_with_valid_key(pet_id='', photo='images\dog.jpeg'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets']) > 0:
        status, result = pf.add_photo_of_pet(auth_key, my_pets['pets'][0]['id'], photo)
        assert status == 200
        assert len(result['pet_photo']) > 0
    else:
        raise Exception("There is no my pets")


#                 Другие 10 тестов
#1
def test_get_api_key_for_blanc_email_and_blanc_password(email='', password=''):
    status, result = pf.get_api_key(email, password)
    assert status == 403
#2
def test_get_api_key_for_valid_email_and_blanc_password(email=valid_email, password=''):
    status, result = pf.get_api_key(email, password)
    assert status == 403
#3
def test_get_api_key_for_valid_email_and_wrong_password(email=valid_email, password=wrong_password):
    status, result = pf.get_api_key(email, password)
    assert status == 403
#4
def test_get_all_pets_with_valid_key_and_filter(filter=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, result_all_pets = pf.get_list_of_pets(auth_key, filter)
    status, result_my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    assert status == 200
    assert len(result_all_pets['pets']) > len(result_my_pets['pets'])
#5
def test_add_new_pet_with_valid_key_with_blank_name(name='', animal_type='кошка', age=23, photo='images\cat.jpg'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_information_about_new_pet(auth_key, name, animal_type, age, photo)
    assert status == 400
    assert result['name']==name
#6
def test_add_new_pet_with_valid_key_with_wrong_age(name='Гуня', animal_type='кошка', age=-23, photo='images\cat.jpg'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_information_about_new_pet(auth_key, name, animal_type, age, photo)
    assert status == 400
    assert result['name']==name
#7
def test_add_new_pet_with_valid_key_without_age(name='Гуня', animal_type='кошка'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_information_about_new_pet_without_photo_and_age(auth_key, name, animal_type)
    assert status == 400
#8
def test_delete_last_mypet_without_valid_key(pet_id=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    auth_key['key']=auth_key['key'][1:]
    if len(my_pets['pets'])>0:
        status = pf.delete_pet_from_database(auth_key, my_pets['pets'][0]['id'])
        assert status == 403

    else:
        raise Exception("There is no my pets")
#9
def test_add_photo_of_pet_with_valid_key_and_witout_pet_id(photo='images\dog.jpeg'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets']) > 0:
        status, result = pf.add_photo_of_pet_without_pet_id(auth_key, photo)
        assert status == 404
    else:
        raise Exception("There is no my pets")
#10
def test_add_photo_of_pet_with_valid_key_and_blanc_pet_id(pet_id='', photo='images\dog.jpeg'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets']) > 0:
        status, result = pf.add_photo_of_pet(auth_key, pet_id, photo)
        assert status == 404
        assert len(result['pet_photo']) > 0
    else:
        raise Exception("There is no my pets")
#11
def test_add_photo_of_pet_with_valid_key_and_empty_file(pet_id='', photo=r'images\noth.jpg'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    if len(my_pets['pets']) > 0:
        status, result = pf.add_photo_of_pet(auth_key, my_pets['pets'][0]['id'], photo)
        assert status == 400
        assert len(result['pet_photo']) > 0
    else:
        raise Exception("There is no my pets")
