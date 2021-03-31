#!/usr/bin/env python3
from math import log, floor, ceil


def E_fwd(series: int, idx: int) -> float:
    """ Returns the value for a given E-series at the given index

    Args:
        series (int): The E series to target
        idx (int): The index of the series to get the value of [0 to series-1]

    Returns:
        float: E-series base value
    """
    if series in [3, 6, 12, 24]:
        p = 1
    else:
        p = 2
    return round((10**idx)**(1 / series), p)  # Return the (range)-root of 10^idx


def E_inv(series: int, val: float) -> float:
    """Returns the exact (continous) index for a given value on a given series.

    Args:
        series (int): The E series to target
        val (float): The value to find a base for

    Returns:
        float: The floating idx the value corrosponds to.
    """

    return log(val**series) / log(10)


def get_base(val: float) -> (float, float):
    """Get the base of a float [0-10[ float

    Args:
        val (float): The float to reduce to a single digit value

    Returns:
        float: The single digit representation of the float
        float: The exponent the value was reduced by. Negative for <0 values
    """

    exponent = 0
    while val >= 10:
        exponent += 1
        val /= 10

    while val < 0:
        exponent -= 1
        val *= 10
    return val, exponent


class EEValue(float):
    """ Class that provides EE friendly numbers
    Provides with automatic prefixing and standard value fitting
    """

    E24_series_overrides = ((10, 11, 12, 13, 14, 15, 16, 22), (2.7, 3.0, 3.3, 3.6, 3.9, 4.3, 4.7, 8.2))

    def __new__(cls, value):
        return super(EEValue, EEValue).__new__(cls, value)

    def E(self, series: int = 96, mode: str = 'round', legacy: bool = True) -> float:

        val = float(self)
        base, exponent = get_base(val)
        idx = E_inv(series, base)

        if mode == "round":
            idx = round(idx)
        elif mode == "ceil":
            idx = ceil(idx)
        elif mode == "floor":
            idx = floor(idx)
        else:
            raise ValueError('Mode has to be either "round", "ceil" or "floor". {} is not a valid mode'.format(mode))

        if series in [3, 6, 12, 24]:
            if idx in self.E24_series_overrides[0]:
                return self.E24_series_overrides[1][self.E24_series_overrides[0].index(idx)] * 10**exponent

        return E_fwd(series, idx) * 10**exponent

    # Arithmetic overloads
    def __add__(self, other):
        res = super(EEValue, self).__add__(other)
        return self.__class__(res)

    def __sub__(self, other):
        res = super(EEValue, self).__sub__(other)
        return self.__class__(res)

    def __mul__(self, other):
        res = super(EEValue, self).__mul__(other)
        return self.__class__(res)

    def __div__(self, other):
        res = super(EEValue, self).__div__(other)
        return self.__class__(res)

    def __floordiv__(self, other):
        res = super(EEValue, self).__floordiv__(other)
        return self.__class__(res)

    def __truediv__(self, other):
        res = super(EEValue, self).__truediv__(other)
        return self.__class__(res)

    def __mod__(self, other):
        res = super(EEValue, self).__mod__(other)
        return self.__class__(res)

    def __divmod__(self, other):
        res = super(EEValue, self).__divmod__(other)
        return self.__class__(res)

    def __pow__(self, other):
        res = super(EEValue, self).__pow__(other)
        return self.__class__(res)

    def __radd__(self, other):
        res = super(EEValue, self).__radd__(other)
        return self.__class__(res)

    def __rsub__(self, other):
        res = super(EEValue, self).__rsub__(other)
        return self.__class__(res)

    def __rmul__(self, other):
        res = super(EEValue, self).__rmul__(other)
        return self.__class__(res)

    def __rfloordiv__(self, other):
        res = super(EEValue, self).__rfloordiv__(other)
        return self.__class__(res)

    def __rtruediv__(self, other):
        res = super(EEValue, self).__rtruediv__(other)
        return self.__class__(res)

    def __rmod__(self, other):
        res = super(EEValue, self).__rmod__(other)
        return self.__class__(res)

    def __rdivmod__(self, other):
        res = super(EEValue, self).__rdivmod__(other)
        return self.__class__(res)

    def __rpow__(self, other):
        res = super(EEValue, self).__rpow__(other)
        return self.__class__(res)

    def __str__(self):
        return "%f" % float(self)

    def __repr__(self):
        return "EEValue(%f)" % int(self)
