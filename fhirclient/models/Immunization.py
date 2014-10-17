#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (immunization.profile.json) on 2014-10-17.
#  2014, SMART Platforms.

# We need to support importing other generated classes without relying on the
# models being part of a specific module. To do so we prepend the current
# directory sys.path - better solutions are welcome!
import sys
import os.path
abspath = os.path.abspath(os.path.dirname(__file__))
if abspath not in sys.path:
    sys.path.insert(0, abspath)


import AdverseReaction
import CodeableConcept
import FHIRDate
import FHIRElement
import FHIRReference
import FHIRResource
import Identifier
import Location
import Narrative
import Organization
import Patient
import Practitioner
import Quantity


class Immunization(FHIRResource.FHIRResource):
    """ Immunization event information.
    
    Scope and Usage The immunization resource is intended to cover the
    administration of vaccines to patients across all healthcare disciplines in
    all care settings and all regions. This includes immunization of both
    humans and animals but does not include the administration of non-vaccine
    agents, even those that may have or claim immunological effects.
    
    Additionally, the immunization resource is expected to cover key concepts
    related to the creation, revision and querying of a patient's immunization
    history. This resource - through consultation with the PHER work group - is
    believed to meet key use cases and information requirements as defined in
    the existing HL7 v2.x immunization implementation guide, HL7 v3 POIZ domain
    and Immunization Domain Analysis Model.
    """
    
    resource_name = "Immunization"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.date = None
        """ Vaccination administration date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.doseQuantity = None
        """ Amount of vaccine administered.
        Type `Quantity` (represented as `dict` in JSON). """
        
        self.expirationDate = None
        """ Vaccine expiration date.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.explanation = None
        """ Administration / refusal reasons.
        Type `ImmunizationExplanation` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.location = None
        """ Where did vaccination occur?.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """
        
        self.lotNumber = None
        """ Vaccine lot number.
        Type `str`. """
        
        self.manufacturer = None
        """ Vaccine manufacturer.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.performer = None
        """ Who administered vaccine?.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.reaction = None
        """ Details of a reaction that follows immunization.
        List of `ImmunizationReaction` items (represented as `dict` in JSON). """
        
        self.refusedIndicator = False
        """ Was immunization refused?.
        Type `bool`. """
        
        self.reported = False
        """ Is this a self-reported record?.
        Type `bool`. """
        
        self.requester = None
        """ Who ordered vaccination?.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.route = None
        """ How vaccine entered body.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.site = None
        """ Body site vaccine  was administered.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.subject = None
        """ Who was immunized?.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.text = None
        """ Text summary of the resource, for human interpretation.
        Type `Narrative` (represented as `dict` in JSON). """
        
        self.vaccinationProtocol = None
        """ What protocol was followed.
        List of `ImmunizationVaccinationProtocol` items (represented as `dict` in JSON). """
        
        self.vaccineType = None
        """ Vaccine product administered.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(Immunization, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Immunization, self).update_with_json(jsondict)
        if 'date' in jsondict:
            self.date = FHIRDate.FHIRDate.with_json(jsondict['date'])
        if 'doseQuantity' in jsondict:
            self.doseQuantity = Quantity.Quantity.with_json(jsondict['doseQuantity'])
        if 'expirationDate' in jsondict:
            self.expirationDate = FHIRDate.FHIRDate.with_json(jsondict['expirationDate'])
        if 'explanation' in jsondict:
            self.explanation = ImmunizationExplanation.with_json(jsondict['explanation'])
        if 'identifier' in jsondict:
            self.identifier = Identifier.Identifier.with_json(jsondict['identifier'])
        if 'location' in jsondict:
            self.location = FHIRReference.FHIRReference.with_json_and_owner(jsondict['location'], self, Location.Location)
        if 'lotNumber' in jsondict:
            self.lotNumber = jsondict['lotNumber']
        if 'manufacturer' in jsondict:
            self.manufacturer = FHIRReference.FHIRReference.with_json_and_owner(jsondict['manufacturer'], self, Organization.Organization)
        if 'performer' in jsondict:
            self.performer = FHIRReference.FHIRReference.with_json_and_owner(jsondict['performer'], self, Practitioner.Practitioner)
        if 'reaction' in jsondict:
            self.reaction = ImmunizationReaction.with_json(jsondict['reaction'])
        if 'refusedIndicator' in jsondict:
            self.refusedIndicator = jsondict['refusedIndicator']
        if 'reported' in jsondict:
            self.reported = jsondict['reported']
        if 'requester' in jsondict:
            self.requester = FHIRReference.FHIRReference.with_json_and_owner(jsondict['requester'], self, Practitioner.Practitioner)
        if 'route' in jsondict:
            self.route = CodeableConcept.CodeableConcept.with_json(jsondict['route'])
        if 'site' in jsondict:
            self.site = CodeableConcept.CodeableConcept.with_json(jsondict['site'])
        if 'subject' in jsondict:
            self.subject = FHIRReference.FHIRReference.with_json_and_owner(jsondict['subject'], self, Patient.Patient)
        if 'text' in jsondict:
            self.text = Narrative.Narrative.with_json(jsondict['text'])
        if 'vaccinationProtocol' in jsondict:
            self.vaccinationProtocol = ImmunizationVaccinationProtocol.with_json(jsondict['vaccinationProtocol'])
        if 'vaccineType' in jsondict:
            self.vaccineType = CodeableConcept.CodeableConcept.with_json(jsondict['vaccineType'])


class ImmunizationExplanation(FHIRElement.FHIRElement):
    """ Administration / refusal reasons.
    
    Reasons why a vaccine was administered or refused.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.reason = None
        """ Why immunization occurred.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.refusalReason = None
        """ Why immunization did not occur.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        super(ImmunizationExplanation, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ImmunizationExplanation, self).update_with_json(jsondict)
        if 'reason' in jsondict:
            self.reason = CodeableConcept.CodeableConcept.with_json(jsondict['reason'])
        if 'refusalReason' in jsondict:
            self.refusalReason = CodeableConcept.CodeableConcept.with_json(jsondict['refusalReason'])


class ImmunizationReaction(FHIRElement.FHIRElement):
    """ Details of a reaction that follows immunization.
    
    Categorical data indicating that an adverse event is associated in time to
    an immunization.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.date = None
        """ When did reaction start?.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.detail = None
        """ Additional information on reaction.
        Type `FHIRReference` referencing `AdverseReaction` (represented as `dict` in JSON). """
        
        self.reported = False
        """ Was reaction self-reported?.
        Type `bool`. """
        
        super(ImmunizationReaction, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ImmunizationReaction, self).update_with_json(jsondict)
        if 'date' in jsondict:
            self.date = FHIRDate.FHIRDate.with_json(jsondict['date'])
        if 'detail' in jsondict:
            self.detail = FHIRReference.FHIRReference.with_json_and_owner(jsondict['detail'], self, AdverseReaction.AdverseReaction)
        if 'reported' in jsondict:
            self.reported = jsondict['reported']


class ImmunizationVaccinationProtocol(FHIRElement.FHIRElement):
    """ What protocol was followed.
    
    Contains information about the protocol(s) under which the vaccine was
    administered.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.authority = None
        """ Who is responsible for protocol.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.description = None
        """ Details of vaccine protocol.
        Type `str`. """
        
        self.doseSequence = None
        """ What dose number within series?.
        Type `int`. """
        
        self.doseStatus = None
        """ Does dose count towards immunity?.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.doseStatusReason = None
        """ Why does does count/not count?.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.doseTarget = None
        """ Disease immunized against.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.series = None
        """ Name of vaccine series.
        Type `str`. """
        
        self.seriesDoses = None
        """ Recommended number of doses for immunity.
        Type `int`. """
        
        super(ImmunizationVaccinationProtocol, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ImmunizationVaccinationProtocol, self).update_with_json(jsondict)
        if 'authority' in jsondict:
            self.authority = FHIRReference.FHIRReference.with_json_and_owner(jsondict['authority'], self, Organization.Organization)
        if 'description' in jsondict:
            self.description = jsondict['description']
        if 'doseSequence' in jsondict:
            self.doseSequence = jsondict['doseSequence']
        if 'doseStatus' in jsondict:
            self.doseStatus = CodeableConcept.CodeableConcept.with_json(jsondict['doseStatus'])
        if 'doseStatusReason' in jsondict:
            self.doseStatusReason = CodeableConcept.CodeableConcept.with_json(jsondict['doseStatusReason'])
        if 'doseTarget' in jsondict:
            self.doseTarget = CodeableConcept.CodeableConcept.with_json(jsondict['doseTarget'])
        if 'series' in jsondict:
            self.series = jsondict['series']
        if 'seriesDoses' in jsondict:
            self.seriesDoses = jsondict['seriesDoses']

