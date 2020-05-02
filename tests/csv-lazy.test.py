from fluxify.lazy_mapper import LazyMapper
import yaml, json

with open('./tests/examples/csv.yaml', 'r') as fh:
    Map = yaml.load(fh.read(), Loader=yaml.FullLoader)

mapper = LazyMapper(_type='csv', error_tolerance=True)


def callback(results):
    print(results)
    print('======================')
    print('======================')


mapper.set_callback(callback)
mapper.set_bulksize(10)

mapper.map('./tests/examples/flux1-large.csv', Map, skip_header=True)
