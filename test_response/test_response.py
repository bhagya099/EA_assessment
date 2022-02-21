import pytest

# importing the function from get_festival_data file to get response
from get_festivals_data import get_festivals_data

# storing in a variable
response = get_festivals_data()

# checking the response code will be ok
def test_response_code():
    assert response.status_code == 200,"response code is not 200"

# checking the response is json and make sure is not empty

def test_response_empty():
    # fist do test if response is ok
    test_response_code()
    assert response.json() != "", "Response is empty"


# checking the keys "name" and "bands" is in response and values are not empty
@pytest.mark.parametrize("keys", ['name', 'bands'])
def test_response_keys(keys):
    # first checking if response is correct
    test_response_empty()
    # looping in json response
    for key in response.json():
        assert keys in key.keys(), f"{keys} key is not in response"
        assert key[keys] != '', f"{keys} value are empty"


# checking the bands has two keys and their value not empty
@pytest.mark.parametrize("keys", ['name', 'recordLabel'])
def test_response_bands(keys):
    # first checking if response is correct
    test_response_empty()
    for key in response.json():
        # print(i['bands'])
        for key_res in key['bands']:
            # print(key_res)
            assert keys in key_res
            assert key_res[keys] != "", f"{keys}  value is empty"