# 특정 문구 정의
target_phrase = "&cr"

# XML 파일 경로 정의
xml_file_path = './qwer.xml'
cleaned_xml_file_path = './asdf.xml'

# 파일 읽기 및 특정 문구가 포함된 줄 제거
with open(xml_file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 특정 문구가 포함된 줄을 제외하고 새로운 파일에 저장
with open(cleaned_xml_file_path, 'w', encoding='utf-8') as cleaned_file:
    for line in lines:
        if target_phrase not in line:
            cleaned_file.write(line)

print(f"Lines containing '{target_phrase}' have been removed and saved to '{cleaned_xml_file_path}'.")

