#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (device.profile.json) on 2014-10-17.
#  2014, SMART Platforms.

# We need to support importing other generated classes without relying on the
# models being part of a specific module. To do so we prepend the current
# directory sys.path - better solutions are welcome!
import sys
import os.path
abspath = os.path.abspath(os.path.dirname(__file__))
if abspath not in sys.path:
    sys.path.insert(0, abspath)


import CodeableConcept
import Contact
import FHIRDate
import FHIRReference
import FHIRResource
import Identifier
import Location
import Narrative
import Organization
import Patient


class Device(FHIRResource.FHIRResource):
    """ An instance of a manufactured thing that is used in the provision of
    healthcare.
    
    Scope and Usage This resource is primarily used for recording which device
    performed an action and can also be used to track device location. It is
    also used for prescribing and dispensing devices for patient use. If the
    device is implanted in a patient, then the patient element will be present,
    and there would be no location.
    
    Devices that are implanted in a patient differ from medications because
    they are not "used up" - they remain active in a patient in an ongoing
    fashion. The Medication resource SHOULD not be used to represent implanted
    devices.
    """
    
    resource_name = "Device"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.contact = None
        """ Details for human/organization for support.
        List of `Contact` items (represented as `dict` in JSON). """
        
        self.expiry = None
        """ Date of expiry of this device (if applicable).
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.identifier = None
        """ Instance id from manufacturer, owner and others.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.location = None
        """ Where the resource is found.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """
        
        self.lotNumber = None
        """ Lot number of manufacture.
        Type `str`. """
        
        self.manufacturer = None
        """ Name of device manufacturer.
        Type `str`. """
        
        self.model = None
        """ Model id assigned by the manufacturer.
        Type `str`. """
        
        self.owner = None
        """ Organization responsible for device.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.patient = None
        """ If the resource is affixed to a person.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.text = None
        """ Text summary of the resource, for human interpretation.
        Type `Narrative` (represented as `dict` in JSON). """
        
        self.type = None
        """ What kind of device this is.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.udi = None
        """ FDA Mandated Unique Device Identifier.
        Type `str`. """
        
        self.url = None
        """ Network address to contact device.
        Type `str`. """
        
        self.version = None
        """ Version number (i.e. software).
        Type `str`. """
        
        super(Device, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Device, self).update_with_json(jsondict)
        if 'contact' in jsondict:
            self.contact = Contact.Contact.with_json(jsondict['contact'])
        if 'expiry' in jsondict:
            self.expiry = FHIRDate.FHIRDate.with_json(jsondict['expiry'])
        if 'identifier' in jsondict:
            self.identifier = Identifier.Identifier.with_json(jsondict['identifier'])
        if 'location' in jsondict:
            self.location = FHIRReference.FHIRReference.with_json_and_owner(jsondict['location'], self, Location.Location)
        if 'lotNumber' in jsondict:
            self.lotNumber = jsondict['lotNumber']
        if 'manufacturer' in jsondict:
            self.manufacturer = jsondict['manufacturer']
        if 'model' in jsondict:
            self.model = jsondict['model']
        if 'owner' in jsondict:
            self.owner = FHIRReference.FHIRReference.with_json_and_owner(jsondict['owner'], self, Organization.Organization)
        if 'patient' in jsondict:
            self.patient = FHIRReference.FHIRReference.with_json_and_owner(jsondict['patient'], self, Patient.Patient)
        if 'text' in jsondict:
            self.text = Narrative.Narrative.with_json(jsondict['text'])
        if 'type' in jsondict:
            self.type = CodeableConcept.CodeableConcept.with_json(jsondict['type'])
        if 'udi' in jsondict:
            self.udi = jsondict['udi']
        if 'url' in jsondict:
            self.url = jsondict['url']
        if 'version' in jsondict:
            self.version = jsondict['version']

