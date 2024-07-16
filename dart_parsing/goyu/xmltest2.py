import xml.etree.ElementTree as ET
from collections import defaultdict


    
# 외부 XML 파일 경로
file_path = './CORPCODE.xml'

# XML 파일을 읽어들여 파싱
tree = ET.parse(file_path)
root = tree.getroot()

corp_list = dict()

def getCorpList():
    corp_list = dict()
    list_elem in root.findall('.//list'):
    corp_code = list_elem.find('corp_code').text
    corp_name = list_elem.find('corp_name').text
    stock_code = list_elem.find('stock_code').text.strip()  # 공백 제거
    modify_date = list_elem.find('modify_date').text

    # 출력
    if stock_code:
        corp_list[corp_code] = corp_name


# 모든 list 요소를 찾아서 데이터 추출
# for list_elem in root.findall('.//list'):
#     corp_code = list_elem.find('corp_code').text
#     corp_name = list_elem.find('corp_name').text
#     stock_code = list_elem.find('stock_code').text.strip()  # 공백 제거
#     modify_date = list_elem.find('modify_date').text

#     # 출력
#     if stock_code:
#         corp_list[corp_code] = corp_name
        # print(f"Corp Code: {corp_code}")
        # print(f"Corp Name: {corp_name}")
        # print(f"Stock Code: '{stock_code}'")  # Stock Code가 비어있음을 확인하기 위해 따옴표 추가
        # print(f"Modify Date: {modify_date}")
        # print('-' * 40)






