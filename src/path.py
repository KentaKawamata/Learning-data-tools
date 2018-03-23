import xml.etree.ElementTree as et

def file_path():
    
    tree = et.ElementTree(file='path.xml')
    root = tree.getroot()

    image_path = root.findtext("image_path")
    label_path = root.findtext("label_path")

    return image_path, label_path
