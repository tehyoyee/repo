import requests
import zipfile
import os


# url = "https://opendart.fss.or.kr/api/document.xml"
url = "https://opendart.fss.or.kr/api/corpCode.xml"
api_key = "ae5c9c5b6c926588c55cd34dea4f48f133ccc868"
# rcept_no = "20240320001487"

params = {
    'crtfc_key': api_key,
    # 'rcept_no': rcept_no,
    # 'reprt_code': 11011
}

doc_zip_path = os.path.abspath('./document.zip')

if not os.path.isfile(doc_zip_path):
    response = requests.get(url, params=params)
    with open(doc_zip_path, 'wb') as fp:
        fp.write(response.content)

zf = zipfile.ZipFile(doc_zip_path)
zf.extractall()

zipinfo = zf.infolist()
filenames = [x.filename for x in zipinfo]
filename = filenames[0]
zf.extract(filename)
zf.close()

with open(f'./{filename}', 'r', encoding='euc-kr') as fp:
    lines = fp.readlines()
with open('./temp.xml', 'w', encoding='utf-8') as fp:
    fp.writelines(lines)
