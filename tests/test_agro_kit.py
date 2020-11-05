#!/usr/bin/env python

"""Tests for `agro_kit` package."""

import pytest
from agro_kit.agro_kit import AgroKit
import pymnea2 as nmea

myAG = AgroKit()  #initialise AgroKit object
gll = "$GPGLL,4916.45,N,12311.12,W,225444,A,*1D"

def testRMC():
    x = myAG.getRMC()
    assert x.__class__.__name__ == "RMC"

def testGGA():
    x = myAG.geGGA()
    assert x.__class__.__name__ == "GGA"

def testGLL():
    x = myAG.getGLL()
    assert x.__class__.__name__ == "GLL"

def testGSV():
    x = myAG.getGSV()
    assert x.__class__.__name__ == "GSV"

def testGSA():
    x = myAG.getGSA()
    assert x.__class__.__name__ == "GSA"

def testVTG():
    x = myAG.getVTG()
    assert x.__class__.__name__ == "VTG"

def testGetLongLat():
    nmea_obj = nmea.parse(gll)
    res = myAG.GPS.getLongLat()
    assert res == "49.274166666666666,N,-123.18533333333333,W"

def testLoadProfile():
    myAG.loadProfile("pytest")
    assert myAG.MIN_MOISTURE == 0
    assert myAG.MAX_MOISTURE == 10
    assert myAG.MIN_LUX == 20
    assert myAG.MAX_LUX == 30
