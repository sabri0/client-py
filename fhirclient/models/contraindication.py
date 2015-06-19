#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/Contraindication) on 2015-06-19.
#  2015, SMART Health IT.


import codeableconcept
import domainresource
import fhirdate
import fhirelement
import fhirreference
import identifier


class Contraindication(domainresource.DomainResource):
    """ Clinical issue with action.
    
    Indicates an actual or potential clinical issue with or between one or more
    active or proposed clinical actions for a patient.  E.g. Drug-drug
    interaction, Ineffective treatment frequency, Procedure-condition conflict,
    etc.
    """
    
    resource_name = "Contraindication"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.author = None
        """ Who found issue?.
        Type `FHIRReference` referencing `Practitioner, Device` (represented as `dict` in JSON). """
        
        self.category = None
        """ E.g. Drug-drug, duplicate therapy, etc..
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.date = None
        """ When identified.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.detail = None
        """ Description and context.
        Type `str`. """
        
        self.identifier = None
        """ Unique id for the contraindication.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.implicated = None
        """ Problem resource.
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """
        
        self.mitigation = None
        """ Step taken to address.
        List of `ContraindicationMitigation` items (represented as `dict` in JSON). """
        
        self.patient = None
        """ Associated patient.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.reference = None
        """ Authority for issue.
        Type `str`. """
        
        self.severity = None
        """ high | medium | low.
        Type `str`. """
        
        super(Contraindication, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(Contraindication, self).elementProperties()
        js.extend([
            ("author", "author", fhirreference.FHIRReference, False),
            ("category", "category", codeableconcept.CodeableConcept, False),
            ("date", "date", fhirdate.FHIRDate, False),
            ("detail", "detail", str, False),
            ("identifier", "identifier", identifier.Identifier, False),
            ("implicated", "implicated", fhirreference.FHIRReference, True),
            ("mitigation", "mitigation", ContraindicationMitigation, True),
            ("patient", "patient", fhirreference.FHIRReference, False),
            ("reference", "reference", str, False),
            ("severity", "severity", str, False),
        ])
        return js


class ContraindicationMitigation(fhirelement.FHIRElement):
    """ Step taken to address.
    
    Indicates an action that has been taken or is committed to to reduce or
    eliminate the likelihood of the risk identified by the contraindicaiton
    from manifesting.  Can also reflect an observation of known mitigating
    factors that may reduce/eliminate the need for any action.
    """
    
    resource_name = "ContraindicationMitigation"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.action = None
        """ What mitigation?.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.author = None
        """ Who is committing?.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.date = None
        """ Date committed.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        super(ContraindicationMitigation, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ContraindicationMitigation, self).elementProperties()
        js.extend([
            ("action", "action", codeableconcept.CodeableConcept, False),
            ("author", "author", fhirreference.FHIRReference, False),
            ("date", "date", fhirdate.FHIRDate, False),
        ])
        return js

