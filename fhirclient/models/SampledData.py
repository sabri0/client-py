#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (type-SampledData.profile.json) on 2014-10-17.
#  2014, SMART Platforms.

# We need to support importing other generated classes without relying on the
# models being part of a specific module. To do so we prepend the current
# directory sys.path - better solutions are welcome!
import sys
import os.path
abspath = os.path.abspath(os.path.dirname(__file__))
if abspath not in sys.path:
    sys.path.insert(0, abspath)


import FHIRElement
import Quantity


class SampledData(FHIRElement.FHIRElement):
    """ A series of measurements taken by a device.
    """
    
    resource_name = "SampledData"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.data = None
        """ Decimal values with spaces, or "E" | "U" | "L".
        Type `str`. """
        
        self.dimensions = None
        """ Number of sample points at each time point.
        Type `int`. """
        
        self.factor = None
        """ Multiply data by this before adding to origin.
        Type `float`. """
        
        self.lowerLimit = None
        """ Lower limit of detection.
        Type `float`. """
        
        self.origin = None
        """ Zero value and units.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.period = None
        """ Number of milliseconds between samples.
        Type `float`. """
        
        self.upperLimit = None
        """ Upper limit of detection.
        Type `float`. """
        
        super(SampledData, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(SampledData, self).update_with_json(jsondict)
        if 'data' in jsondict:
            self.data = jsondict['data']
        if 'dimensions' in jsondict:
            self.dimensions = jsondict['dimensions']
        if 'factor' in jsondict:
            self.factor = jsondict['factor']
        if 'lowerLimit' in jsondict:
            self.lowerLimit = jsondict['lowerLimit']
        if 'origin' in jsondict:
            self.origin = Quantity.Quantity.with_json(jsondict['origin'])
        if 'period' in jsondict:
            self.period = jsondict['period']
        if 'upperLimit' in jsondict:
            self.upperLimit = jsondict['upperLimit']

