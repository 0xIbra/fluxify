from mapper import Mapper
import yaml, json

yamlmapping = """
maker.original:
    col: 1
model.original:
    col: 2
generation.original:
    col: 3
gearbox.original:
    col: 4
energy.original:
    value: 'ESSENCE'
price:
    col: 5
    transformations:
        - { transformer: 'number' }
started_at.date:
    col: 6
    transformations:
        - { transformer: 'date', in_format: '%Y-%m-%d %H:%M', out_format: '%d/%m/%Y' }
started_at.time:
    col: 6
    transformations:
        - { transformer: 'date', in_format: '%Y-%m-%d %H:%M', out_format: '%H:%M' }
is_essence:
    conditions:
        - 
            condition: 'exists("subject.energy.original") and matches("(essence)", subject["energy"]["original"], "i")'
            returnOnSuccess: 'true'
            returnOnFail: 'false'
"""

Map = yaml.load(yamlmapping, Loader=yaml.FullLoader)

mapper = Mapper()
data = mapper.map('./examples/flux1.csv', Map)
print(json.dumps(data))