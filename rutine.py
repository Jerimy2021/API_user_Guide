# Description: This file contains the function calculate that calculates the position of the sun in the sky.
from math import radians, cos, sin

def calculate(distance,right_ascension, declination):
    """
    Calculate the position of the sun in the sky.

    Parameters
    ----------
    right_ascension : float
        Right ascension of the sun in degrees.
    declination : float
        Declination of the sun in degrees.
    distance : float
        Distance of the sun in astronomical units.

    Returns
    -------
    point x : float
        The x coordinate of the sun in the sky.
    point y : float
        The y coordinate of the sun in the sky.
    point z : float
        The z coordinate of the sun in the sky.

    """
    distance = float(distance)
    right_ascension = float(right_ascension)
    declination = float(declination)

    ra_radians = radians(right_ascension)
    dec_radians = radians(declination)
    x = distance * cos(dec_radians) * cos(ra_radians)
    y = distance * sin(dec_radians)
    z = distance * cos(dec_radians) * sin(ra_radians)

    value = [x, y, z]
    return value



d = ['47 UMa d', '13.7967000', '164.8647611', '40.4304931']
c = ['47 UMa c', '13.7967000', '164.8647611', '40.4304931']
b = ['47 UMa b', '13.7967000', '164.8647611', '40.4304931']

data = []

data.append(calculate(b[1], b[2], b[3]))
data.append(calculate(c[1], c[2], c[3]))
data.append(calculate(d[1], d[2], d[3]))
print(data)


b_ = ['14 Her b', '17.9323000', '242.6021014', '43.8163621']

print(calculate(b_[1], b_[2], b_[3]))
