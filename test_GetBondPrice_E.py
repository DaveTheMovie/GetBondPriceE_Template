
import GetBondPrice_E

def test_GetBondPriceE():
    yc = [.010,.015,.020,.025,.030]
    face = 2000000
    couponRate = .04
    m = 10
    assert round(GetBondPrice_E.getBondPrice_E(face, couponRate, m, yc)) == 2098949 
