import xml.etree.ElementTree as ET

FILE = "./akizuki_library/Akizuki.lbr"

tree = ET.parse(FILE)
root = tree.getroot()

# 最上位階層のタグと中身
print(root.tag)
for neighbor in root.iter('deviceset'):
    print(neighbor.attrib["name"])
root.find("deviceset")
print(root[0][1].text)