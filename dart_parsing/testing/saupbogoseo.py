import requests
import zipfile
import os
import xml.etree.ElementTree as ET
file_path = './CORPCODE.xml'


url = "https://opendart.fss.or.kr/api/document.xml"
# url = "https://opendart.fss.or.kr/api/fnlttXbrl.xml"
api_key = "ae5c9c5b6c926588c55cd34dea4f48f133ccc868"
rcept_no = "20240320001487"

params = {
    'crtfc_key': api_key,
    'rcept_no': rcept_no,
    # 'reprt_code': 11011
}

doc_zip_path = os.path.abspath('./document.zip')

if not os.path.isfile(doc_zip_path):
    response = requests.get(url, params=params)
    with open(doc_zip_path, 'wb') as fp:
        fp.write(response.content)

# zf = zipfile.ZipFile(doc_zip_path)
# zf.extractall()

with zipfile.ZipFile(doc_zip_path, 'r') as zf:
    for file_info in zf.infolist():
        # 원본 파일 이름
        original_file_name = file_info.filename
        
        # 새 파일 이름을 생성하는 방법 (여기서는 예시로 'prefix_'를 붙임)
        new_file_name = '카카오_' + os.path.basename(original_file_name)
        
        # 새 파일 경로 생성
        new_file_path = os.path.join('.', new_file_name)
        
        # 파일을 추출
        with zf.open(file_info) as source, open(new_file_path, 'wb') as target:
            target.write(source.read())



# zipinfo = zf.infolist()
# filenames = [x.filename for x in zipinfo]
# filename = filenames[0]
# zf.extract(filename)
# zf.close()

# with open(f'./{filename}', 'r', encoding='euc-kr') as fp:
#     lines = fp.readlines()
# with open('./temp.xml', 'w', encoding='utf-8') as fp:
#     fp.writelines(lines)
