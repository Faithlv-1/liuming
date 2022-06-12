import requests
# url = "http://59.110.45.28/m/api/search"
# headers = {
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
#     "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
#     "origin": "http://tool.liumingye.cn"
# }
# data = {
#     "data": "445b7M3Va_bn_Cxx0MGONnNi8CzJB7V5wIOLZdSjeZV2R90KjCPJAV43zFyastL5rOvolIy8d0aNzKVb",
#     "v": 2
# }
# resp = requests.post(url, data=data, headers=headers)
# print(resp.text)


url = "https://cdn-y.tencentmusic.com/musician/commonPic/cos_ZfyUHEbkm2ctbdYBE6xX3kuhgrppHwQa.png"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "origin": "https://omofun.tv/"
}

resp = requests.get(url, headers=headers)
with open("D:\\code\\p_code\\liuming\\aa.png",'wb') as f:
    f.write(resp.content)
print(resp.content)