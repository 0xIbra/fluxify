from fluxify.mapper import Mapper
import yaml, json

with open('./fluxify/examples/csv.yaml', 'r') as fh:
    Map = yaml.load(fh.read(), Loader=yaml.FullLoader)

mapper = Mapper()
data = mapper.map('./fluxify/examples/flux1.csv', Map, skip_header=True)
print(json.dumps(data))
print('STATS : ', mapper.get_stats())
