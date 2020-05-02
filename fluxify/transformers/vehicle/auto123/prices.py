from fluxify.transformers import validate_transformation_args


def auto123_prices(transformation: dict):
    validate_transformation_args(transformation)

    value = transformation['value']
    prices = {}

    if 'VehiclePrice' in value:
        prices['default'] = int(value['VehiclePrice'][0])
    else:
        for arr in value:
            if arr['VehiclePricingType'][0] == 'internet':
                prices['default'] = int(arr['VehiclePrice'][0])

    return prices
