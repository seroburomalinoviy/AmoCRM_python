from pprint import pprint
import json
import requests

def auth(amo_domain):
    url = amo_domain + "/oauth2/access_token"
    data = {
  "client_id": "e1ef3912-72e6-4827-b3dd-cd276be2fbf4",
  "client_secret": "im09Vvb3gvFOsnB7IXDNFKJqKhUIWVltjnczYrX4Wuf4iczxEIkHRJI3B8OyJD98",
  "grant_type": "authorization_code",
  "code": "def502003e2f527d6ef33f63046c28b8f447c1c9492d2d8719d14e56ec3078989f911f4d26b19b70cac40b339cdf723d82e2bc85e15b72cf32a64b5f38764464855433d81a4390a439c87a83b44dd59ab06a7890d617a99f4691ef204575738495e383b3cf8d53fffaded42b2f2d5981c11a0ea3701e64e27b624851d5eec636058d98991d6b38789815a4d725b811e46f0956b8d2b7e91f7e6b08fcceb87fec79d796f66566943bd34e44c3ad5fb34d3baf3eb645249887713e53398d8a070d845a0a99d6c5420ea40ab905ed0b7cb338e0191235ac566fc5b9986939b8ac9eb83b1944aa2f41d9dd08efdc2e5c9066955ac34606b0c96aa15eb3bbeacb5aa710fdd78e2d5ee3a5965a275679c24f7ce61655faaa17639ba0b9800ca9ecd56a1a46bfef4c82b4cf2071e524c1dc3349a8854dcca38fed5a29bf647b97a9336a7e1e009013cf647dd66372bed3cc7be2d2676e0fbcb33645af1122e1d81d5bb494110cd269dce30d66545a2d8fe8ab93b5c62d647176bab9a4fe46cfe441d05174f436934cec43a9be8cc1344a0f53acfecae88fe11e686bc34d38756c0a7f4db2538eccbceb0e52c707f6f4799fe0d55416fbf1c5cd0bb7b59e6b8f3fba532bad08019a40",
  "redirect_uri": "https://antidirt.amocrm.com"
}
    res = requests.post(url, data=data, params={'type':'json'})

    print('status code', res.status_code)

    if res.status_code == 200:
      pprint(res.json())
      with open('tokens.txt', 'w') as tok:
          json.dump(res.json(), tok)
    else:
      pprint(res.content)

