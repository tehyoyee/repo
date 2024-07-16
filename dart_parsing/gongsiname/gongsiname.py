import requests
import zipfile
import os
import xml.etree.ElementTree as ET
import zipfile
from collections import defaultdict

report_no_corp_name_map = dict()
report_no_report_name_map = dict()
corp_code_corn_name_map = dict()

def getCorpList():
    # 외부 XML 파일 경로
    file_path = './CORPCODE.xml'

    # XML 파일을 읽어들여 파싱
    tree = ET.parse(file_path)
    root = tree.getroot()
    # corp_list = dict()
    corp_list = []
    for list_elem in root.findall('.//list'):
        corp_code = list_elem.find('corp_code').text
        corp_name = list_elem.find('corp_name').text
        stock_code = list_elem.find('stock_code').text.strip()  # 공백 제거
        modify_date = list_elem.find('modify_date').text 
        # 출력
        if stock_code:
            # corp_list[corp_code] = corp_name
            corp_list.append(corp_code)
            corp_code_corn_name_map[corp_code] = corp_name
    return corp_list

def getReportList():
    file_path = './document.xml'
    tree = ET.parse(file_path)
    root = tree.getroot()
    # report_no_list = dict()
    # report_name_list = dict()
    for list_elem in root.findall('.//list'):
        rcept_no = list_elem.find('rcept_no').text
        corp_name =  list_elem.find('flr_nm').text
        report_nm = list_elem.find('report_nm').text
        # report_no_list[rcept_no] = corp_name
        # report_name_list[rcept_no] = report_nm
        report_no_corp_name_map[rcept_no] = corp_name
        report_no_report_name_map[rcept_no] = report_nm

    # return report_no_list, report_name_list

corp_list = getCorpList()

cnt = 0
cntMinus = 0
# for key, value in corp_list.items():
for corp_no in corp_list[700:710]:
    cnt += 1
    print(cnt, corp_code_corn_name_map[corp_no])
    # if corp_code_corn_name_map[corp_no] != '카카오뱅크':
    #     continue
    # if cnt == 300:
    #     continue
    # if cnt == 400:
    #     break


    url = "https://opendart.fss.or.kr/api/list.xml"
    api_key = "ae5c9c5b6c926588c55cd34dea4f48f133ccc868"

    params = {
        'crtfc_key': api_key,
        'corp_code': corp_no,
        'bgn_de': 20230101,
        # 'end_de': 20241231,
        'corp_cls': 'Y',
        'pblntf_detail_ty': 'A001',
        'page_no': 1,
        'page_count': 100
    }

    doc_zip_path = os.path.abspath('./document.xml')
    response = requests.get(url, params=params)
    with open(doc_zip_path, 'wb') as fp:
        fp.write(response.content)
    # report_no_list, report_name_list = getReportList()
    getReportList()
    fp.close()
    
    # for no, name in report_no_list.items():
    #     report_no_corp_name_map[no] = name
    # for no, name in report_no_list.items():
    #     report_no_report_name_map[no] = name
    

# print(report_no_report_name_map)
# print(report_no_corp_name_map)
    ##################################
cnt = 0
for report_no, corp_name in report_no_corp_name_map.items():

    url = "https://opendart.fss.or.kr/api/document.xml"
    api_key = "ae5c9c5b6c926588c55cd34dea4f48f133ccc868"
    rcept_no = report_no

    params = {
        'crtfc_key': api_key,
        'rcept_no': rcept_no
    }
    doc_zip_path = os.path.abspath('./temp/document.zip')



    response = requests.get(url, params=params)
    with open(doc_zip_path, 'wb') as fp:
        fp.write(response.content)



    # ZIP 파일 열기

#     try:
#         with zipfile.ZipFile(doc_zip_path, 'r') as zf:
#             for file_info in zf.infolist():
#                 cnt+=1
#                 print(cnt)
#                 # 원본 파일 이름
#                 original_file_name = file_info.filename
                
#                 # 새 파일 이름을 생성하는 방법 (여기서는 예시로 'prefix_'를 붙임)
#                 new_file_name =  corp_name + '_' + report_no_report_name_map[report_no] \
#                     + os.path.basename(original_file_name)
                
#                 # 새 파일 경로 생성
#                 new_file_path = os.path.join('./reports/', new_file_name)
                
#                 # 파일을 추출
#                 with zf.open(file_info) as source:
#                     # # euc-kr로 읽어서 utf-8로 변환
#                     # print(corp_name)
#                     # content = source.read().decode('euc-kr')
                    
#                     # # 새 파일을 utf-8 인코딩으로 저장
#                     # with open(new_file_path, 'w', encoding='utf-8') as target:
#                     #     target.write(content)
#                     try:
#                         content = source.read().decode('euc-kr')
#                     except UnicodeDecodeError as e:
#                         # EUC-KR 인코딩 실패 시 대체 로직
#                         print(f"Error decoding file {original_file_name} with EUC-KR: {e}")
#                         try:
#                             content = source.read().decode('utf-8')
#                         except UnicodeDecodeError as e:
#                             # UTF-8 인코딩 실패 시 대체 로직
#                             try:
#                                 print(f"Error decoding file {original_file_name} with UTF-8: {e}")
#                                 content = source.read().decode('latin-1')  # 다른 인코딩으로 시도 (예: Latin-1)
#                             except:
#                                 content = source.read()

#                 # 새 파일을 utf-8 인코딩으로 저장
#                 with open(new_file_path, 'w', encoding='utf-8') as target:
#                     target.write(content)
#     except:
#         cntMinus += 1
#         continue

# print("누락("+cntMinus+")("+cnt+"개)")









    with zipfile.ZipFile(doc_zip_path, 'r') as zf:
        # file_info = zf.infolist()[0]
        for file_info in zf.infolist():
            # 원본 파일 이름
            original_file_name = file_info.filename
            if original_file_name.endswith('_00760.xml') or original_file_name.endswith('_00761.xml'):
                continue
            
            # 새 파일 이름을 생성하는 방법 (여기서는 예시로 'prefix_'를 붙임)
            new_file_name =  corp_name + '_' + report_no_report_name_map[report_no]
                # + os.path.basename(original_file_name)
            
            # 새 파일 경로 생성
            new_file_path = os.path.join('.', new_file_name)
            
            # 파일을 추출
            with zf.open(file_info) as source, open(new_file_path, 'wb') as target:
                target.write(source.read())














    # response = requests.get(url, params=params)
    # response.raise_for_status()  # 요청이 실패한 경우 예외를 발생시킵니다.

    # # 다운로드한 ZIP 파일 저장
    # with open(doc_zip_path, 'wb') as fp:
    #     fp.write(response.content)

    # # ZIP 파일 열기
    # with zipfile.ZipFile(doc_zip_path, 'r') as zf:
    #     for file_info in zf.infolist():
    #         # 원본 파일 이름
    #         original_file_name = file_info.filename
            
    #         # 새 파일 이름을 생성하는 방법 (여기서는 예시로 'prefix_'를 붙임)
    #         new_file_name =  corp_name + '_' + report_no_report_name_map[report_no] \
    #             + os.path.basename(original_file_name)
            
    #         # 새 파일 경로 생성
    #         new_file_path = os.path.join('.', new_file_name)
            
    #         # 파일을 추출
    #         with zf.open(file_info) as source:
    #             # euc-kr로 읽어서 utf-8로 변환
    #             content = source.read().decode('euc-kr')
                
    #             # 새 파일을 utf-8 인코딩으로 저장
    #             with open(new_file_path, 'w', encoding='utf-8') as target:
    #                 target.write(content)













# 다운로드한 ZIP 파일 저장
    # with open(doc_zip_path, 'wb') as fp:
    #     fp.write(response.content)

    # # ZIP 파일 열기 및 한글 파일 이름 처리
    # with pyzipper.AESZipFile(doc_zip_path, 'r', compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as zf:
    #     for file_info in zf.infolist():
    #         # 원본 파일 이름을 한글이 포함된 경우 UTF-8로 디코딩
    #         original_file_name = file_info.filename.encode('cp437').decode('utf-8')

    #         # 새 파일 이름을 생성하는 방법 (여기서는 예시로 'prefix_'를 붙임)
    #         new_file_name = corp_name + '_' + report_no_report_name_map[report_no] + '_' + os.path.basename(original_file_name)

    #         # 새 파일 경로 생성
    #         new_file_path = os.path.join('.', new_file_name)

    #         # 파일을 추출
    #         with zf.open(file_info) as source, open(new_file_path, 'wb') as target:
    #             target.write(source.read())








# response.raise_for_status()  # 요청이 실패한 경우 예외를 발생시킵니다.

    # 다운로드한 ZIP 파일 저장
    # with open(doc_zip_path, 'wb') as fp:
    #     fp.write(response.content)

    # # ZIP 파일 열기 및 UTF-8 인코딩 지정
    # with zipfile.ZipFile(doc_zip_path, 'r', encoding='utf-8') as zf:
    #     for file_info in zf.infolist():
    #         # 원본 파일 이름
    #         original_file_name = file_info.filename

    #         # 새 파일 이름을 생성하는 방법 (여기서는 예시로 'prefix_'를 붙임)
    #         new_file_name = corp_name + '_' + report_no_report_name_map[report_no] + '_' + os.path.basename(original_file_name)

    #         # 새 파일 경로 생성
    #         new_file_path = os.path.join('.', new_file_name)

    #         # 파일을 추출
    #         with zf.open(file_info) as source, open(new_file_path, 'wb') as target:
    #             target.write(source.read())





