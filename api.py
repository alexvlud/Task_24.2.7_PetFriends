import requests

class PetFriends:
    def __init__(self):
        self.base_url="https://petfriends.skillfactory.ru/"

    def get_api_key(self,email,password):
        headers={
            'email':email,
            'password': password
        }
        res=requests.get(self.base_url+'api/key', headers=headers)

        status=res.status_code
        result=""
        try:
            result=res.json()
        except:
            result=res.text
        return status, result

    def get_list_of_pets(self, auth_key, filter):
        headers={'auth_key':auth_key['key']}
        filter={'filter':filter}

        res=requests.get(self.base_url+'api/pets', headers=headers, params=filter)

        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def add_information_about_new_pet(self, auth_key, name, animal_type, age, pet_photo):
        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age,
        }
        headers = {'auth_key': auth_key['key']}
        file = {'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')}

        res = requests.post(self.base_url + 'api/pets', headers=headers, data=data, files=file)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def delete_pet_from_database(self, auth_key, pet_id):
        headers = {'auth_key': auth_key['key']}
        res=requests.delete(self.base_url + f'api/pets/{pet_id}', headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status

    def update_information_about_pet(self, auth_key, pet_id, name, animal_type, age):
        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age,
        }
        headers = {'auth_key': auth_key['key']}
        res = requests.put(self.base_url + f'api/pets/{pet_id}', headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def add_information_about_new_pet_without_photo(self, auth_key, name, animal_type, age):
        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age,
        }
        headers = {'auth_key': auth_key['key']}

        res = requests.post(self.base_url + 'api/create_pet_simple', headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def add_photo_of_pet(self, auth_key, pet_id, pet_photo):
        headers = {'auth_key': auth_key['key']}
        file = {'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')}

        res = requests.post(self.base_url + f'api/pets/set_photo/{pet_id}', headers=headers, files=file)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def add_information_about_new_pet_without_photo_and_age(self, auth_key, name, animal_type):
        data = {
            'name': name,
            'animal_type': animal_type,

        }
        headers = {'auth_key': auth_key['key']}

        res = requests.post(self.base_url + 'api/create_pet_simple', headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def add_photo_of_pet_without_pet_id(self, auth_key, pet_photo):
        headers = {'auth_key': auth_key['key']}
        file = {'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')}

        res = requests.post(self.base_url + f'api/pets/set_photo/', headers=headers, files=file)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result