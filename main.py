import os

from jinja2 import Environment, FileSystemLoader
import xml.etree.ElementTree  as ET

def parseAndRender(xmlFile):
    tree = ET.parse(xmlFile)
    root = tree.getroot()

    data = {}

    for item in root:
        className = item.attrib['class_name']
        data['className'] = className
        data['members'] = []
        for field in item:
            data['members'].append({'type': field.attrib['type'], 'name': field.attrib['name']})

        output = template.render(data = data)
        with open(f"{className}.h", "w") as f:
            f.write(output)


file_loader = FileSystemLoader('./templates')
env = Environment(loader = file_loader)

template = env.get_template('class_one.jinja')

parseAndRender("data.xml")