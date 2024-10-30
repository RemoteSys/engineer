# coding: utf-8
import xml.etree.ElementTree as ET


def parse_my_xml(path):
    tree = ET.parse(ad1)
    root = tree.getroot()
    return root, tree


def scan_my_xml(element, level=0, seen=None):
    if seen is None:
        seen = []
    atrs = [a.strip() for a in sorted(element.attrib.keys())]
    atrs = ','.join(atrs)
    ide = f"{element.tag.strip()},{atrs}"
    
    if ide not in seen:
        print(f"{level: >{level*2}}: {element.tag}, ({atrs})")
        seen.append(ide)
        # breakpoint()
    for child in element:
        scan_my_xml(child, level+1, seen)
        

def get_data(root):
    res = {'id': [], 'name': [], 'age': [], 'role': []}
    for id_elem in root.findall('id'):
        res['id'].append(id_elem.attrib.get('id_num'))
        for person in id_elem.findall('person'):
            name = person.find('name').text
            age = person.find('age').tag
            role = person.attrib.get('role', None)
            res['name'].append(name)
            res['age'].append(age)
            res['role'].append(role)
    return res        
