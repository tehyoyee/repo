import requests
import zipfile
import os
import xml.etree.ElementTree as ET

xml_file_path = os.path.join(os.getcwd(), './CORPCODE.xml')
tree = ET.parse(xml_file_path)
root = tree.getroot()

for child in root:
    # print({child.corp_name})
    print(child.attrib)
    # print(f'Tag: {child.tag}, Attributes: {child.attrib}, Text: {child.text}')