import requests
response = requests.get("https://httpbin.org/get")
print(type(response.content))

print(response.text)

respinse2 = requests.post("https://httpbin.org/post",
                          data="Test data",
                          headers={"h1":"Test title"}
                          )

print(respinse2.text)