from fluxify import LazyMapper, Mapper
import yaml, json, os

with open('./fluxify/examples/json2.yaml', 'r') as fh:
    jsonMap = yaml.load(fh.read(), Loader=yaml.FullLoader)

mapper = LazyMapper(_type='json', error_tolerance=True)


def callback(data):
    print('DATA : ', data)
    exit()


mapper.set_callback(callback)
mapper.map('./fluxify/examples/flux2.json', jsonMap, root_node='data')
