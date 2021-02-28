import requests

def clients():
    token_h = "Token 95f8405c2d7b38ebc7ebbeb676fafd2908af451c"
    # credentials = {
    #     "username": "admin",
    #     "password": "admin123"
    # }
    # response = requests.post("http://127.0.0.1:8000/api/rest-auth/login/", data=credentials)
    headers = {"Authorization": token_h}
    response = requests.get("http://127.0.0.1:8000/api/profiles/", headers=headers)
    
    print("Status code: ", response.status_code)
    response_data = response.json()
    print(response_data)
    
if __name__ == "__main__":
    clients()
     