from fluxify.transformers import (split, number, date, replace, equipments_from_string, options_from_string,
                                  dividor, multiplicator, type_converter, prefix, suffix,
                                  str_to_bool, right, left, array_walk, remove_html_tag, trim,
                                  search_files, capture, array_from_multiple_values)

from fluxify.transformers import (planet_vo_equipments)
from fluxify.transformers import (parot_vi_equipments, parot_vi_options)
from fluxify.transformers import vpn_price_promo
from fluxify.transformers import (publicar_equipments_from_array, publicar_equipments_from_sub_array,
                                  publicar_equipments_from_multiple_values, publicar_equipments_from_array_string_values,
                                  publicar_options_from_multiple_values, publicar_options_from_array_string_values,
                                  publicar_options_from_array)
from fluxify.transformers import (neowebcar_type, neowebcar_images, neowebcar_options, neowebcar_equipments)
from fluxify.transformers import kepler_equipments, kepler_images, kepler_options
from fluxify.transformers import dcsnet_equipments
from fluxify.transformers import (ubiflow_options, ubiflow_equipments)
from fluxify.transformers import (auto123_images, auto123_equipments, auto123_prices)
from fluxify.transformers import edp_images
from fluxify.transformers import eurolinea_options, eurolinea_equipments
from fluxify.transformers import selectup_images, selectup_options, selectup_equipments
from fluxify.transformers import starterre_images
from fluxify.transformers import v12_options, v12_equipments, v12_conditions
from fluxify.transformers import vulcain_equipments, vulcain_images
from fluxify.transformers import (bee2link_equipments, bee2link_images, bee2link_options)

from fluxify.exceptions import (UnsupportedTransformerException, InvalidArgumentException, ArgumentNotFoundException,
                                ConditionNotFoundException)

TRANSFORMERS = {
    'number': number,
    'DDFactory\\Component\\Mapper\\Adapter\\ExplodeAdapter': split,
    'DDFactory\\Component\\Mapper\\Adapter\\DateFormatAdapter': date,
    'DDFactory\\Component\\Mapper\\Adapter\\DividorAdapter': dividor,
    'DDFactory\\Component\\Mapper\\Adapter\\MultiplicatorAdapter': multiplicator,
    'DDFactory\\Component\\Mapper\\Adapter\\ReplaceAdapter': replace,
    'DDFactory\\Component\\Mapper\\Adapter\\TypeConvertAdapter': type_converter,
    'DDFactory\\Component\\Mapper\\Adapter\\PrefixAdapter': prefix,
    'DDFactory\\Component\\Mapper\\Adapter\\SuffixAdapter': suffix,
    'DDFactory\\Component\\Mapper\\Adapter\\StringToBoolAdapter': str_to_bool,
    'DDFactory\\Component\\Mapper\\Adapter\\RightAdapter': right,
    'DDFactory\\Component\\Mapper\\Adapter\\LeftAdapter': left,
    'DDFactory\\Component\\Mapper\\Adapter\\ArrayWalkAdapter': array_walk,
    'DDFactory\\Component\\Mapper\\Adapter\\RemoveHtmlTagAdapter': remove_html_tag,
    'DDFactory\\Component\\Mapper\\Adapter\\TrimAdapter': trim,
    'DDFactory\\Component\\Mapper\\Adapter\\SearchFilesAdapter': search_files,
    'DDFactory\\Component\\Mapper\\Adapter\\CaptureAdapter': capture,
    'DDFactory\\Component\\Mapper\\Adapter\\ArrayFromMultipleValuesAdapter': array_from_multiple_values,
    'equipments_from_string': equipments_from_string,
    'options_from_string': options_from_string,

    # Vehicle transformers
    'DDFactory\\Component\\Mapper\\Adapter\\Vehicle\\PlanetVo\\EquipmentsAdapter': planet_vo_equipments,

    'DDFactory\\Component\\Mapper\\Adapter\\Vehicle\\PlanetVo\\ParotVI\\EquipmentsAdapter': parot_vi_equipments,
    'DDFactory\\Component\\Mapper\\Adapter\\Vehicle\\PlanetVo\\ParotVI\\OptionsAdapter': parot_vi_options,

    'DDFactory\\Component\\Mapper\\Adapter\\Vehicle\\PlanetVo\\VPN\\PricePromoAdapter': vpn_price_promo,

    'DDFactory\\Component\\Mapper\\Adapter\\Vehicle\\Publicar\\EquipmentsFromArrayAdapter': publicar_equipments_from_array,
    'DDFactory\\Component\\Mapper\\Adapter\\Vehicle\\Publicar\\EquipmentsFromArrayStringValuesAdapter': publicar_equipments_from_array_string_values,
    'DDFactory\\Component\\Mapper\\Adapter\\Vehicle\\Publicar\\EquipmentsFromMultipleValuesAdapter': publicar_equipments_from_multiple_values,
    'DDFactory\\Component\\Mapper\\Adapter\\Vehicle\\Publicar\\EquipmentsFromSubArrayAdapter': publicar_equipments_from_sub_array,
    'DDFactory\\Component\\Mapper\\Adapter\\Vehicle\\Publicar\\OptionsFromArrayAdapter': publicar_options_from_array,
    'DDFactory\\Component\\Mapper\\Adapter\\Vehicle\\Publicar\\OptionsFromArrayStringValuesAdapter': publicar_options_from_array_string_values,
    'DDFactory\\Component\\Mapper\\Adapter\\Vehicle\\Publicar\\OptionsFromMultipleValuesAdapter': publicar_options_from_multiple_values,

    'DDFactory\\Component\\Mapper\\Adapter\\Vehicle\\Neowebcar\\EquipmentsAdapter': neowebcar_equipments,
    'DDFactory\\Component\\Mapper\\Adapter\\Vehicle\\Neowebcar\\OptionsAdapter': neowebcar_options,
    'DDFactory\\Component\\Mapper\\Adapter\\Vehicle\\Neowebcar\\TypeAdapter': neowebcar_type,
    'DDFactory\\Component\\Mapper\\Adapter\\Vehicle\\Neowebcar\\ImagesAdapter': neowebcar_images,

    'DDFactory\\Component\\Mapper\\Adapter\\Vehicle\\Kepler\\ImagesAdapter': kepler_images,
    'DDFactory\\Component\\Mapper\\Adapter\\Vehicle\\Kepler\\EquipmentsAdapter': kepler_equipments,
    'DDFactory\\Component\\Mapper\\Adapter\\Vehicle\\Kepler\\OptionsAdapter': kepler_options,

    'DDFactory\\Component\\Mapper\\Adapter\\Vehicle\\DCSNet\\EquipmentsAdapter': dcsnet_equipments,

    'DDFactory\\Component\\Mapper\\Adapter\\Vehicle\\Ubiflow\\EquipmentsAdapter': ubiflow_equipments,
    'DDFactory\\Component\\Mapper\\Adapter\\Vehicle\\Ubiflow\\OptionsAdapter': ubiflow_options,

    'DDFactory\\Component\\Mapper\\Adapter\\Vehicle\\Auto123\\ImagesAdapter': auto123_images,
    'DDFactory\\Component\\Mapper\\Adapter\\Vehicle\\Auto123\\EquipmentsAdapter': auto123_equipments,
    'DDFactory\\Component\\Mapper\\Adapter\\Vehicle\\Auto123\\PricesAdapter': auto123_prices,

    'DDFactory\\Component\\Mapper\\Adapter\\Vehicle\\Edp\\ImagesAdapter': edp_images,

    'DDFactory\\Component\\Mapper\\Adapter\\Vehicle\\Eurolinea\\EquipmentsAdapter': eurolinea_equipments,
    'DDFactory\\Component\\Mapper\\Adapter\\Vehicle\\Eurolinea\\OptionsAdapter': eurolinea_options,

    'DDFactory\\Component\\Mapper\\Adapter\\Vehicle\\Selectup\\EquipmentsAdapter': selectup_equipments,
    'DDFactory\\Component\\Mapper\\Adapter\\Vehicle\\Selectup\\OptionsAdapter': selectup_options,
    'DDFactory\\Component\\Mapper\\Adapter\\Vehicle\\Selectup\\ImagesAdapter': selectup_images,

    'DDFactory\\Component\\Mapper\\Adapter\\Vehicle\\Starterre\\ImagesAdapter': starterre_images,

    'DDFactory\\Component\\Mapper\\Adapter\\Vehicle\\V12\\ConditionsAdapter': v12_conditions,
    'DDFactory\\Component\\Mapper\\Adapter\\Vehicle\\V12\\EquipmentsAdapter': v12_equipments,
    'DDFactory\\Component\\Mapper\\Adapter\\Vehicle\\V12\\OptionsAdapter': v12_options,

    'DDFactory\\Component\\Mapper\\Adapter\\Vehicle\\Vulcain\\EquipmentsAdapter': vulcain_equipments,
    'DDFactory\\Component\\Mapper\\Adapter\\Vehicle\\Vulcain\\ImagesAdapter': vulcain_images,

    'DDFactory\\Component\\Mapper\\Adapter\\Vehicle\\Bee2link\\EquipmentsAdapter': bee2link_equipments,
    'DDFactory\\Component\\Mapper\\Adapter\\Vehicle\\Bee2link\\OptionsAdapter': bee2link_options,
    'DDFactory\\Component\\Mapper\\Adapter\\Vehicle\\Bee2link\\ImagesAdapter': bee2link_images
}


def handle_transformations(transformations, value, error_tolerance=False):
    finalvalue = value
    for transformation in transformations:
        try:
            transformation['value'] = finalvalue
        except:
            print('\n')
            print(transformations)
            exit()
        transformation['error_tolerance'] = error_tolerance

        transformer = transformation['class']
        if transformer not in TRANSFORMERS:
            raise UnsupportedTransformerException('Unsupported transformer: "{}"'.format(transformer))

        invoker = TRANSFORMERS[transformer]
        if error_tolerance:
            try:
                finalvalue = invoker(transformation)
            except (InvalidArgumentException, ArgumentNotFoundException, ConditionNotFoundException, UnsupportedTransformerException, Exception) as e:
                print('[warning] ', e)
        else:
            finalvalue = invoker(transformation)

    return finalvalue
