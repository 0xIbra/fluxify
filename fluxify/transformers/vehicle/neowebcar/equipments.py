from fluxify.transformers import validate_transformation_args


def neowebcar_equipments(transformation: dict):
    validate_transformation_args(transformation)

    value = transformation['value']
    equipments = []

    equipment_list = {
      'item_12v_power_outlets_count': 'nombre de prise 12v',
      'abs': 'abs',
      'adj_count_dr_seat': 'nombre de réglage du siège conducteur',
      'adj_count_psgr_seat': 'nombre de réglage siège passager',
      'air_conditioning': 'climatisation',
      'automatic_locking_doors': 'verrouillage automatique des ouvrants',
      'cd_changer': 'chargeur cd',
      'cd_player': 'lecteur cd',
      'cellphone_preparation': 'préparation téléphone',
      'cellphone_preparation_bluetooth téléphone': 'bluetooth',
      'cellphone_preparation_voice_activation': 'commande vocale du téléphone',
      'cellphone_with_bluetooth': 'téléphone bluetooth',
      'central_locking': 'fermeture centralisée',
      'centre_armrest_2nd_row': 'disponibilité accoudoir central arrière',
      'centre_armrest_fr': 'accoudoir central avant',
      'cruise_control': 'régulateur de vitesse',
      'daytime_running_lights': 'feux de jour',
      'driver_airbag': 'airbag conducteur',
      'driver_knee_airbag': 'airbag genoux conducteur',
      'driver_seat_height_adjustment': 'siège conducteur réglable en hauteur',
      'driver_vanity_mirror': 'miroir de courtoisie pour le conducteur',
      'driving_mirrors_electric_adjustment': 'rétros extérieurs : électriques',
      'driving_mirrors_heated': 'rétros extérieurs chauffants',
      'dvd_player_front': 'disponibilité dvd avant',
      'elec_adj_count_dr_seat': 'nombre de réglage électrique du siège conducteur',
      'elec_adj_count_psgr_seat': 'nombre de réglage électrique du siège passager',
      'electronic_stability_control': 'contrôle électronique de stabilité',
      'electronic_traction_control': 'contrôle électronique de traction',
      'emergency_brake_assist': "assistance au freinage d'urgence",
      'first_sunroof': 'toit ouvrant',
      'front_cup_holders': 'porte gobelets avant',
      'front_curtain_airbags': "airbags rideaux à l'avant",
      'front_electric_windows': 'vitres avant électriques',
      'front_fog_lights': 'feux anti-brouillard avant',
      'front_park_sensor': 'aide au stationnement avant',
      'front_side_airbags': "airbags latéraux à l'avant",
      'front_tyre_profile': 'série des pneus avant',
      'front_tyre_width': 'largeur des pneus avant',
      'front_wheel_diameter': 'diamètre des jantes avant (en pouce)',
      'front_windscreen_rain_sensor': 'détecteur de pluie',
      'headlight_cleaners': 'laves-phares avant',
      'heated_dr_seat': 'siège conducteur chauffant',
      'heated_psgr_seat': 'siège passager chauffant',
      'hill_descent_control': 'contrôle de descente',
      'ice_system_auxilliary': 'usb prise audio auxiliaire : usb',
      'immobiliser': 'antidémarrage',
      'isofix_preparation': 'préparation isofix',
      'lumbar_dr_seat': 'réglage lombaire du siège conducteur',
      'mp3_player': 'lecteur mp3',
      'multi_function_display': 'ecran multifonction',
      'navigation_system': 'système de navigation',
      'parcel_shelf_luggage_cover': 'cache bagages',
      'passenger_airbag': 'airbag passager',
      'passenger_airbag_deactivation': 'airbag passager déconnectable',
      'passenger_knee_airbag': 'airbag genoux passager',
      'passenger_seat_height_adjustment': 'réglage en hauteur du siège passager',
      'passenger_vanity_mirror': 'miroir de courtoisie pour le passager',
      'power_steering': 'direction assistée',
      'power_steering_speed_proportional': 'direction assistée asservie à la vitesse',
      'rds': 'rds',
      'rear_cup_holders': 'porte gobelets arrière',
      'rear_curtain_airbags': "airbags rideaux à l'arrière",
      'rear_electric_windows': 'vitres arrière électriques',
      'rear_entertainment_dvd_player': 'système multimedia arrière : lecteur dvd',
      'rear_fog_light': 'feux antibrouillard arrière',
      'rear_park_sensor': 'aide au stationnement arrière',
      'rear_seat_folding': '2ème rangée de sièges : rabattables',
      'rear_side_airbags': "airbags latéraux à l'arrière",
      'rear_window_wiper': 'essuie-glace arrière',
      'remote_boot_hatch_tailgate_release': 'ouverture du coffre à distance',
      'run_flat_tyres': 'pneus à roulage à plat',
      'spare_wheel_type': 'type de roue de secours',
      'speakers_count': 'nombre de haut-parleur',
      'speed_limiter': 'limiteur de vitesse',
      'steering_wheel_audio_control': 'volant à réglages audio',
      'steering_wheel_cellular_phone_control': 'volant à réglages téléphone',
      'steering_wheel_height_adjustment': 'volant réglable en hauteur',
      'steering_wheel_telescopic_adjustment': 'volant réglable en profondeur',
      'steering_wheel_trim': 'finition du volant',
      'thermal_windscreen': 'pare-brise athermique',
      'trip_computer': 'ordinateur de bord',
      'type_2nd_row': 'type de la 2ième rangée',
      'tyre_pressure_indicator': 'indicateur de sous-pression des pneus',
      'tyres_type': 'type de pneus',
      'ventilation_control_zones': 'nombre de zones de contôle de la climatisation',
      'wheel_name': 'nom des jantes',
      'wheel_type': 'type des jantes',
      'xenon': 'xénon'
    }

    try:
        for item in value.getchildren():
            original = item.tag
            name = item.tag
            if original in equipment_list:
                name = equipment_list[original]

            equipments.append({
                'name': name,
                'original': original,
                'value': item.text,
                'group': None
            })
    except:
        pass

    return equipments
