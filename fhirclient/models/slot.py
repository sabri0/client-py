#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/Slot) on 2015-06-19.
#  2015, SMART Health IT.


import codeableconcept
import domainresource
import fhirdate
import fhirreference
import identifier


class Slot(domainresource.DomainResource):
    """ A slot of time on a schedule that may be available for booking appointments.
    """
    
    resource_name = "Slot"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.comment = None
        """ Comments on the slot to describe any extended information. Such as
        custom constraints on the slot.
        Type `str`. """
        
        self.end = None
        """ Date/Time that the slot is to conclude.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.freeBusyType = None
        """ BUSY | FREE | BUSY-UNAVAILABLE | BUSY-TENTATIVE.
        Type `str`. """
        
        self.identifier = None
        """ External Ids for this item.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.overbooked = False
        """ This slot has already been overbooked, appointments are unlikely to
        be accepted for this time.
        Type `bool`. """
        
        self.schedule = None
        """ The schedule resource that this slot defines an interval of status
        information.
        Type `FHIRReference` referencing `Schedule` (represented as `dict` in JSON). """
        
        self.start = None
        """ Date/Time that the slot is to begin.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.type = None
        """ The type of appointments that can be booked into this slot (ideally
        this would be an identifiable service - which is at a location,
        rather than the location itself). If provided then this overrides
        the value provided on the availability resource.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(Slot, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(Slot, self).elementProperties()
        js.extend([
            ("comment", "comment", str, False),
            ("end", "end", fhirdate.FHIRDate, False),
            ("freeBusyType", "freeBusyType", str, False),
            ("identifier", "identifier", identifier.Identifier, True),
            ("overbooked", "overbooked", bool, False),
            ("schedule", "schedule", fhirreference.FHIRReference, False),
            ("start", "start", fhirdate.FHIRDate, False),
            ("type", "type", codeableconcept.CodeableConcept, False),
        ])
        return js

