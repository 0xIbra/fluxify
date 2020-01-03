from mapper import Mapper
import yaml, json

# with open('./examples/csv.yaml', 'r') as fh:
#     Map = yaml.load(fh.read(), Loader=yaml.FullLoader)

with open('./examples/json.yaml', 'r') as fh:
    jsonMap = yaml.load(fh.read(), Loader=yaml.FullLoader)

mapper = Mapper()
# data = mapper.map('./examples/flux1.csv', Map)
data = mapper.map('./examples/flux.json', jsonMap, Type='json')
print(json.dumps(data))