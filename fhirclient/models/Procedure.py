#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (procedure.profile.json) on 2014-10-17.
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
import DiagnosticReport
import Encounter
import FHIRElement
import FHIRReference
import FHIRResource
import Identifier
import Narrative
import Patient
import Period
import Practitioner


class Procedure(FHIRResource.FHIRResource):
    """ An action that is performed on a patient.
    
    Scope and Usage This resource is used to record the details of procedures
    performed on a patient. A procedure is an activity that is performed with
    or on a patient as part of the provision of care. Examples include surgical
    procedures, diagnostic procedures, endoscopic procedures, biopsies, and
    exclude things for which there are specific resources, such as
    immunizations, drug administrations.
    
    Note that many diagnostic processes are procedures that generate
    observations and reports. In many cases, the existence of the procedure is
    assumed, but where there are details of interest about how the diagnostic
    procedure was performed, the procedure resource is used to describe the
    activity.
    """
    
    resource_name = "Procedure"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.bodySite = None
        """ Precise location details.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.complication = None
        """ Complication following the procedure.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.date = None
        """ The date the procedure was performed.
        Type `Period` (represented as `dict` in JSON). """
        
        self.encounter = None
        """ The encounter when procedure performed.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """
        
        self.followUp = None
        """ Instructions for follow up.
        Type `str`. """
        
        self.identifier = None
        """ External Ids for this procedure.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.indication = None
        """ Reason procedure performed.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.notes = None
        """ Additional information about procedure.
        Type `str`. """
        
        self.outcome = None
        """ What was result of procedure?.
        Type `str`. """
        
        self.performer = None
        """ The people who performed the procedure.
        List of `ProcedurePerformer` items (represented as `dict` in JSON). """
        
        self.relatedItem = None
        """ A procedure that is related to this one.
        List of `ProcedureRelatedItem` items (represented as `dict` in JSON). """
        
        self.report = None
        """ Any report that results from the procedure.
        List of `FHIRReference` items referencing `DiagnosticReport` (represented as `dict` in JSON). """
        
        self.subject = None
        """ Who procedure was performed on.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.text = None
        """ Text summary of the resource, for human interpretation.
        Type `Narrative` (represented as `dict` in JSON). """
        
        self.type = None
        """ Identification of the procedure.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(Procedure, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Procedure, self).update_with_json(jsondict)
        if 'bodySite' in jsondict:
            self.bodySite = CodeableConcept.CodeableConcept.with_json(jsondict['bodySite'])
        if 'complication' in jsondict:
            self.complication = CodeableConcept.CodeableConcept.with_json(jsondict['complication'])
        if 'date' in jsondict:
            self.date = Period.Period.with_json(jsondict['date'])
        if 'encounter' in jsondict:
            self.encounter = FHIRReference.FHIRReference.with_json_and_owner(jsondict['encounter'], self, Encounter.Encounter)
        if 'followUp' in jsondict:
            self.followUp = jsondict['followUp']
        if 'identifier' in jsondict:
            self.identifier = Identifier.Identifier.with_json(jsondict['identifier'])
        if 'indication' in jsondict:
            self.indication = CodeableConcept.CodeableConcept.with_json(jsondict['indication'])
        if 'notes' in jsondict:
            self.notes = jsondict['notes']
        if 'outcome' in jsondict:
            self.outcome = jsondict['outcome']
        if 'performer' in jsondict:
            self.performer = ProcedurePerformer.with_json(jsondict['performer'])
        if 'relatedItem' in jsondict:
            self.relatedItem = ProcedureRelatedItem.with_json(jsondict['relatedItem'])
        if 'report' in jsondict:
            self.report = FHIRReference.FHIRReference.with_json_and_owner(jsondict['report'], self, DiagnosticReport.DiagnosticReport)
        if 'subject' in jsondict:
            self.subject = FHIRReference.FHIRReference.with_json_and_owner(jsondict['subject'], self, Patient.Patient)
        if 'text' in jsondict:
            self.text = Narrative.Narrative.with_json(jsondict['text'])
        if 'type' in jsondict:
            self.type = CodeableConcept.CodeableConcept.with_json(jsondict['type'])


class ProcedurePerformer(FHIRElement.FHIRElement):
    """ The people who performed the procedure.
    
    Limited to 'real' people rather than equipment.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.person = None
        """ The reference to the practitioner.
        Type `FHIRReference` referencing `Practitioner` (represented as `dict` in JSON). """
        
        self.role = None
        """ The role the person was in.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(ProcedurePerformer, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ProcedurePerformer, self).update_with_json(jsondict)
        if 'person' in jsondict:
            self.person = FHIRReference.FHIRReference.with_json_and_owner(jsondict['person'], self, Practitioner.Practitioner)
        if 'role' in jsondict:
            self.role = CodeableConcept.CodeableConcept.with_json(jsondict['role'])


class ProcedureRelatedItem(FHIRElement.FHIRElement):
    """ A procedure that is related to this one.
    
    Procedures may be related to other items such as procedures or medications.
    For example treating wound dehiscence following a previous procedure.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.target = None
        """ The related item - e.g. a procedure.
        Type `FHIRReference` referencing `AdverseReaction` (represented as `dict` in JSON). """
        
        self.type = None
        """ caused-by | because-of.
        Type `str`. """
        
        super(ProcedureRelatedItem, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(ProcedureRelatedItem, self).update_with_json(jsondict)
        if 'target' in jsondict:
            self.target = FHIRReference.FHIRReference.with_json_and_owner(jsondict['target'], self, AdverseReaction.AdverseReaction)
        if 'type' in jsondict:
            self.type = jsondict['type']

