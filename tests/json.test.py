from fluxify.mapper import Mapper
import yaml, json, os

with open('./fluxify/examples/json.yaml', 'r') as fh:
    jsonMap = yaml.load(fh.read(), Loader=yaml.FullLoader)

mapper = Mapper()
data = mapper.map('./fluxify/examples/flux.json', jsonMap, Type='json')
print(json.dumps(data))