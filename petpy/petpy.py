"""
Petrophysics equations needs more work
"""


def gardner(vp, alpha=310, beta=0.25):
    """
    Compute bulk density (in kg/m^3) from vp (in m/s).
    """
    return alpha * vp**beta


def impedance(vp, rho):
    """
    missing docstring
    """
    return vp * rho
