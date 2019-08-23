import requests

MS_API_POST_URL = "http://192.168.0.109/convert/"
source_file = "samplepptx.pptx"
file_ext = "pptx"

file_content = {'input_file': open(source_file, 'rb')}
data_content = {'file_ext': file_ext, "file_name": "ajhsdfh"}
res = requests.post(MS_API_POST_URL, data=data_content, files=file_content)
print(res.content)
