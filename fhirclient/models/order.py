#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/Order) on 2015-06-19.
#  2015, SMART Health IT.


import codeableconcept
import domainresource
import fhirdate
import fhirelement
import fhirreference
import identifier
import timing


class Order(domainresource.DomainResource):
    """ A request to perform an action.
    """
    
    resource_name = "Order"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.authority = None
        """ If required by policy.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        self.date = None
        """ When the order was made.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.detail = None
        """ What action is being ordered.
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Identifiers assigned to this order by the orderer or by the
        receiver.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.reasonCodeableConcept = None
        """ Text - why the order was made.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ Text - why the order was made.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        self.source = None
        """ Who initiated the order.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.subject = None
        """ Patient this order is about.
        Type `FHIRReference` referencing `Patient, Group, Device, Substance` (represented as `dict` in JSON). """
        
        self.target = None
        """ Who is intended to fulfill the order.
        Type `FHIRReference` referencing `Organization, Device, Practitioner` (represented as `dict` in JSON). """
        
        self.when = None
        """ When order should be fulfilled.
        Type `OrderWhen` (represented as `dict` in JSON). """
        
        super(Order, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(Order, self).elementProperties()
        js.extend([
            ("authority", "authority", fhirreference.FHIRReference, False),
            ("date", "date", fhirdate.FHIRDate, False),
            ("detail", "detail", fhirreference.FHIRReference, True),
            ("identifier", "identifier", identifier.Identifier, True),
            ("reasonCodeableConcept", "reasonCodeableConcept", codeableconcept.CodeableConcept, False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, False),
            ("source", "source", fhirreference.FHIRReference, False),
            ("subject", "subject", fhirreference.FHIRReference, False),
            ("target", "target", fhirreference.FHIRReference, False),
            ("when", "when", OrderWhen, False),
        ])
        return js


class OrderWhen(fhirelement.FHIRElement):
    """ When order should be fulfilled.
    """
    
    resource_name = "OrderWhen"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.code = None
        """ Code specifies when request should be done. The code may simply be
        a priority code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.schedule = None
        """ A formal schedule.
        Type `Timing` (represented as `dict` in JSON). """
        
        super(OrderWhen, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(OrderWhen, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False),
            ("schedule", "schedule", timing.Timing, False),
        ])
        return js

