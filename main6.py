# import requests

# d={
#     "shipments":[
#         {
#             "from":{
#                 "suburb": "MELBOURNE",
#                 "state": "VIC",
#                 "postcode": "3000"
#             },
#             "to":{
#                 "suburb":"SYDNEY",
#                 "state":"NSW",
#                 "postcode":"2000"
#             },
#             "items":[
#                 {
#                     "product_id":"7D55",
#                     "length":"5",
#                     "height":"1",
#                     "width":"10",
#                     "weight":"2"
#                 }
#             ]
#         }
#     ]
# }
# url=f"https://digitalapi.auspost.com.au/shipping/v1/prices/{d['shipments']}"


# response = requests.get(url)

# if response.status_code == 200:
#     data = response.json()
#     print(data)
# else:
#     print("Failed to fetch data. Response status code:", response.status_code)
