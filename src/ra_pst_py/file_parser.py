from lxml import etree
import os

def parse_process_file(process_file) -> etree._Element:
    if isinstance(process_file, etree._Element):
        process = process_file
    elif os.path.isfile(process_file):
        with open(process_file, "r") as f:
           process = etree.fromstring(f.read())
    elif type(process_file) is str:
        process = etree.fromstring(process_file)
    else:
        raise TypeError(" 'process_file' must be a path to a file, an xml-str, or etree._Element")
    proc_ns = {'cpee1':'http://cpee.org/ns/description/1.0'}
    process = process.xpath("//cpee1:description", namespaces = proc_ns)[0]
    return process

def parse_resource_file(resource_file) -> etree._Element:
    if isinstance(resource_file, etree._Element):
        resource =  resource_file
    elif os.path.isfile(resource_file):
        with open(resource_file, "r") as f:
           resource = etree.fromstring(f.read())
    elif type(resource_file) is str:
        resource = etree.fromstring(resource_file)
    else:
        raise TypeError("'process_file' must be of type path to a file, xml-str, or etree._Element")
    return resource
        

    