from fluxify.mapper import Mapper
import yaml, json, os

with open('./fluxify/examples/json.yaml', 'r') as fh:
    jsonMap = yaml.load(fh.read(), Loader=yaml.FullLoader)

mapper = Mapper(_type='json', error_tolerance=True)
data = mapper.map('./fluxify/examples/flux.json', jsonMap)
print(json.dumps(data))
print('STATS : ', mapper.get_stats())
