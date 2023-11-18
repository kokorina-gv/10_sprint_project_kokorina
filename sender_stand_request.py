import configuration
import requests
import data


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers_user)


response = post_new_user(data.user_body)
print(response.status_code)
print(response.json())

data.headers_user_auth["Authorization"] = "Bearer " + str(response.json()["authToken"])


def post_new_kit(body):
    return requests.post(configuration.URL_SERVICE + configuration.MAIN_KITS,
                         json=body,
                         headers=data.headers_user_auth)

kit_response = post_new_kit(data.kit_body)
print(kit_response.status_code)
print(kit_response.json())
