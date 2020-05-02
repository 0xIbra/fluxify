from fluxify.mapper import Mapper
import yaml, json

with open('./tests/examples/csv.yaml', 'r') as fh:
    Map = yaml.load(fh.read(), Loader=yaml.FullLoader)

mapper = Mapper()
data = mapper.map('./tests/examples/flux1.csv', Map, skip_header=True)

print(json.dumps(data[0]))

# print('STATS : ', mapper.get_stats())
