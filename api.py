import urllib.request
import json, requests

def logins(id, password):
    url = "https://api.dimigo.life/users/login"
    values = {'id': id, 'password': password}
    headers = {'content-type': 'application/json'}

    data=json.dumps(values).encode()
    req = urllib.request.Request(url, data, headers)
    with urllib.request.urlopen(req) as response:
        parsed = json.loads(response.read())
        if parsed['success'] == True:
            return parsed['data']
        else:
            return parsed['code']

def my_page(token):
    url = "https://api.dimigo.life/users/me"
    headers = {'Authorization':token}

    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as response:
        parsed = json.loads(response.read())
        if parsed['success'] == True:
            return parsed['data']
        else:
            return parsed['code']

def washer_tables(token):
    url = "https://api.dimigo.life/washer/table"
    headers = {'Authorization':token}

    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as response:
        parsed = json.loads(response.read())
        if parsed['success'] == True:
            return parsed['data']
        else:
            return parsed['code']

def washer_apply(washer, time, token):
    url = "https://api.dimigo.life/washer/table/apply/" + washer + "?timeId=" + time
    print(url)
    headers = {'Authorization': token}

    req = urllib.request.Request(url, headers=headers, data={})
    with urllib.request.urlopen(req) as response:
        return response.read()

if __name__ == "__main__":
    tokens = logins("ryusm150", "@0816i7594")
    print(tokens)
    washer_info = washer_tables(tokens)
    washer = washer_info[0]['_id']
    time = washer_info[0]['applies'][0]['_id']
    print(washer_apply(washer,time, tokens))