import requests
import json

headers = {'Content-Type': 'application/json'}

# JSON POST Request data
data = {
    "token": "7ae56a9445d15fae32e7d1351f6561a6 ",
    "username": "sahil@getdefault.in",
    "start": 1,
    "num": 100
}

# Endpoint URL
url = "https://www.proprofs.com/api/classroom/v1/reports/users/"

# Hit the POST Request
response = requests.request(
    "POST",
    url,
    data=json.dumps(data),
    headers=headers
).json()["result"]

# Initialize a blank result list of candidates
result_list = []

# Loop over all the candidates
for candidate in response:

    # H
    try:
        name = candidate["Name"]
        email = candidate["Email"]
        quiz = candidate["assignment"][0]["title"]
        result = candidate["assignment"][0]["percentCompleted"]
        candidate_detail = {
            'Name': name,
            'Email': email,
            'Quiz': quiz,
            'Result': result,
        }
        print(candidate_detail)
        result_list.append(candidate_detail)

    except Exception as e:
        print(e)

print(len(result_list))
