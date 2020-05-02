from fluxify.transformers import validate_transformation_args


def cars_online_equipments(transformation: dict):
    validate_transformation_args(transformation)

    value = transformation['value']
    equipments = []

    equipment_list = {
      '31': 'Climatisation',
      '32': 'Climatisation automatique',
      '33': 'Sellerie cuir',
      '34': 'Vitres électriques',
      '35': 'Système de navigation / GPS',
      '36': 'Sièges électriques',
      '37': 'Toit ouvrant',
      '38': 'Sièges chauffants',
      '39': 'CD',
      '40': 'ABS',
      '41': 'Airbag conducteur',
      '42': 'Airbag passager',
      '43': 'Airbags latéraux',
      '44': 'Lampes Xénon',
      '45': 'Verrouillage centralisé',
      '46': 'Alarme',
      '47': 'Anti-démarrage',
      '48': 'Anti-patinage',
      '49': '4x4',
      '50': 'Tuning',
      '51': 'Jantes aliage',
      '52': 'Porte-bagages',
      '53': 'Ordinateur de bord',
      '54': 'Radar de recul',
      '55': 'Feux antibrouillard',
      '56': 'Direction assistée',
      '57': 'Radio/Cassette',
      '63': 'Attache remorque',
      '64': 'Controle dynamique de Stabilité',
      '65': 'Régulateur de vitesse',
      '66': 'Equipement handicapé',
      '67': 'Label Dekra',
      '84': 'Chauffage auxiliaire',
      '85': 'Filtres à particules'
    }

    # TODO: Continue implementation

    return equipments
