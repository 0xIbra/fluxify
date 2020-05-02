from fluxify.transformers import validate_transformation_args
from fluxify.utils import Utils


def vpn_price_promo(transformation: dict):
    validate_transformation_args(transformation)

    value = transformation['value']
    price_promo = None
    expected = {'FLASH': 'FLASH', 'PROMO': 'PROMO'}

    try:
        type_str = value[38]
        price = value[41]
        if not Utils.empty(type_str) and not Utils.empty(price) and type_str in expected:
            price_promo = int(price)
    except:
        # TODO: Log something maybe
        pass

    return price_promo
