import decimal

_KIN_TO_QUARKS = decimal.Decimal(10 ** 5)
_PRECISION = decimal.Decimal('0.00001')


def partition(l, size):
    """
    Partition the provided list into a list of sub-lists of the provided size. The last sub-list may be smaller if the
    length of the originally provided list is not evenly divisible by `size`.

    :param l: the list to partition
    :param size: the size of each sub-list

    :return: a list of sub-lists
    """
    return [l[i:i + size] for i in range(0, len(l), size)]


def kin_str_to_quarks(kin: str) -> int:
    """Converts a string kin amount to quarks. If the provided Kin amount contains more than 5 decimal places (i.e.
    it contains an inexact number of quarks), additional decimal places will be ignored.

    For example, passing in a value of "0.000009" will result in a value of 0 quarks being returned.

    :param kin: A string Kin amount.
    :return: An integer quark amount.
    """
    rounded = decimal.Decimal(kin).quantize(_PRECISION, decimal.ROUND_DOWN)
    return int((rounded * _KIN_TO_QUARKS).to_integral_value())


def quarks_to_kin_str(quarks: int) -> str:
    """Converts an integer quark amount into a string Kin amount.

    :param quarks: An amount, in quarks.
    :return: A string Kin amount.
    """
    kin = (decimal.Decimal(quarks) / _KIN_TO_QUARKS)
    return str(kin.normalize())
