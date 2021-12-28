from pprint import pprint
import json
import requests

def auth(amo_domain):
    url = amo_domain + "/oauth2/access_token"
    data = {
  "client_id": "e1ef3912-72e6-4827-b3dd-cd276be2fbf4",
  "client_secret": "im09Vvb3gvFOsnB7IXDNFKJqKhUIWVltjnczYrX4Wuf4iczxEIkHRJI3B8OyJD98",
  "grant_type": "authorization_code",
  "code": "def50200549bae22255b1fad435eca4d81df02a2d44d44eff278a653323de0e9572cfcf2f5de98389e87cf7927097d273a1003ef07d54efb4b70501e254274f4de589d0ceb68b4700a9575388b95ef5009bf43d52761413186d935053ca2e4055d5a77e6a2d7e0801fca2fdc58894a4e02ad4797044479ea6078ee347dec19ad456fd4ac64137652e1514608959c917bae6e6a0ceaea3fe58fc561e19566fbd45a349f1eb8dd7526b8d58850fda5e35af65bab733f7c28a1294833c0b149173ce33ebdfbb3d1b00e41ffae5481b9e2d0903e239040b4081beac1bba3756451a27d4a62b9b47a8436e4af0dfbe6b337a1447a61154a52038f7ed02b53c9b756c26b2155ce66e59552feff99e11b630be5681ae4ed2dc8f6d6042d7be9b9babb26184dcfcf0eada399a609791aa573cd9f7dff041147377b2a5038ed8f2925502a8787d71a71815e8d61a83f9186451bd7d41abc4b3c84a3e5ad009b8e051c5798d0b7bcf61d64653046cae681ff5846cd27cfc3955ae8ed28f799b92a8f6a005534dbf93a1c4414063a07e0def88138800fb39f0a922854cc091a3482403150660c7e5f0f8473c74d50d271856df310d9c7846c994c98de16f89926878acea3138aeb9333a6",
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

