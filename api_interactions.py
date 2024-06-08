import exoplanet_api

def get_planets(system_solar):
    return exoplanet_api.fetch_name_planets(system_solar)

def get_stellar_systems():
    return exoplanet_api.fetch_stellar_hosts()

def get_textures_planets_planet_id(planet_id):
    return exoplanet_api.fetch_textures_planets(planet_id)
