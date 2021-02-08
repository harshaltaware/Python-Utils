import xmltodict, json
fp1 = open("xml file", 'r')
s = fp1.read()
# dict1 = xmltodict.parse('<e> <a>text</a> <a>text</a> </e>')
dict2 = xmltodict.parse(s,force_list={'intervention_browse'})
print json.dumps(dict2)
with open('sample.json','wb') as fb:
    json.dumps(dict2, fb)

    
import json
import xmlschema
xs = xmlschema.XMLSchema('schema.xml')
path = '<file>.xml'
print xs.is_valid(path)
print json.dumps(xs.to_dict(path))
