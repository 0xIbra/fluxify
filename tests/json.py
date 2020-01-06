from fluxify.mapper import Mapper
import yaml, json

with open('../fluxify/examples/json.yaml', 'r') as fh:
    jsonMap = yaml.load(fh.read(), Loader=yaml.FullLoader)

mapper = Mapper()
# data = mapper.map('./examples/flux1.csv', Map)
data = mapper.map('../fluxify/examples/flux.json', jsonMap, Type='json')
print(json.dumps(data))