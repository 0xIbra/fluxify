from fluxify.lazy_mapper import LazyMapper
import yaml, json

with open('./fluxify/examples/xml.yaml', 'r') as fh:
    Map = yaml.load(fh.read(), Loader=yaml.FullLoader)


def callback(results):
    print(f'Count: {len(results)}', 'Result callback', results)


mapper = LazyMapper(_type='xml')
mapper.set_callback(callback)
mapper.set_bulksize(10)

mapper.map('./fluxify/examples/flux-large.xml', Map, item_node='person')
