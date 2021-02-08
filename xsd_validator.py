import sys
from lxml import etree

def Validate(xml_file, xsd_file):
    xsd = etree.parse(xsd_file)
    xmlschema = etree.XMLSchema(xsd)
    xml = etree.parse(xml_file)    
    if not xmlschema(xml):
        log = xmlschema.error_log
        error = log.last_error
        logfile = open("log.txt", "w+")
        logfile.write(str(error))
    else:
        print("SUCCESS")

if __name__=="__main__":
    Validate(sys.argv[1], sys.argv[2])