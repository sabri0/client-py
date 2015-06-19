#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/Provenance) on 2015-06-19.
#  2015, SMART Health IT.


import codeableconcept
import coding
import domainresource
import fhirdate
import fhirelement
import fhirreference
import period
import signature


class Provenance(domainresource.DomainResource):
    """ Who, What, When for a set of resources.
    
    Provenance of a resource is a record that describes entities and processes
    involved in producing and delivering or otherwise influencing that
    resource. Provenance provides a critical foundation for assessing
    authenticity, enabling trust, and allowing reproducibility. Provenance
    assertions are a form of contextual metadata and can themselves become
    important records with their own provenance. Provenance statement indicates
    clinical significance in terms of confidence in authenticity, reliability,
    and trustworthiness, integrity, and stage in lifecycle (e.g., Document
    Completion - has the artifact been legally authenticated), all of which may
    impact Security, Privacy, and Trust policies.
    """
    
    resource_name = "Provenance"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.agent = None
        """ Agents involved in creating resource.
        List of `ProvenanceAgent` items (represented as `dict` in JSON). """
        
        self.entity = None
        """ An entity used in this activity.
        List of `ProvenanceEntity` items (represented as `dict` in JSON). """
        
        self.location = None
        """ Where the activity occurred, if relevant.
        Type `FHIRReference` referencing `Location` (represented as `dict` in JSON). """
        
        self.period = None
        """ When the activity occurred.
        Type `Period` (represented as `dict` in JSON). """
        
        self.policy = None
        """ Policy or plan the activity was defined by.
        List of `str` items. """
        
        self.reason = None
        """ Reason the activity is occurring.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.recorded = None
        """ When the activity was recorded / updated.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.signature = None
        """ Signature on target.
        List of `Signature` items (represented as `dict` in JSON). """
        
        self.target = None
        """ Target Reference(s) (usually version specific).
        List of `FHIRReference` items referencing `Resource` (represented as `dict` in JSON). """
        
        super(Provenance, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(Provenance, self).elementProperties()
        js.extend([
            ("agent", "agent", ProvenanceAgent, True),
            ("entity", "entity", ProvenanceEntity, True),
            ("location", "location", fhirreference.FHIRReference, False),
            ("period", "period", period.Period, False),
            ("policy", "policy", str, True),
            ("reason", "reason", codeableconcept.CodeableConcept, False),
            ("recorded", "recorded", fhirdate.FHIRDate, False),
            ("signature", "signature", signature.Signature, True),
            ("target", "target", fhirreference.FHIRReference, True),
        ])
        return js


class ProvenanceAgent(fhirelement.FHIRElement):
    """ Agents involved in creating resource.
    
    An agent takes a role in an activity such that the agent can be assigned
    some degree of responsibility for the activity taking place. An agent can
    be a person, an organization, software, or other entities that may be
    ascribed responsibility.
    """
    
    resource_name = "ProvenanceAgent"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.display = None
        """ Human description of participant.
        Type `str`. """
        
        self.referenceReference = None
        """ Identity of agent.
        Type `FHIRReference` referencing `Practitioner, RelatedPerson, Patient, Device` (represented as `dict` in JSON). """
        
        self.referenceUri = None
        """ Identity of agent.
        Type `str`. """
        
        self.role = None
        """ Agents Role.
        Type `Coding` (represented as `dict` in JSON). """
        
        self.type = None
        """ Agent Type.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(ProvenanceAgent, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ProvenanceAgent, self).elementProperties()
        js.extend([
            ("display", "display", str, False),
            ("referenceReference", "referenceReference", fhirreference.FHIRReference, False),
            ("referenceUri", "referenceUri", str, False),
            ("role", "role", coding.Coding, False),
            ("type", "type", coding.Coding, False),
        ])
        return js


class ProvenanceEntity(fhirelement.FHIRElement):
    """ An entity used in this activity.
    """
    
    resource_name = "ProvenanceEntity"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.agent = None
        """ Entity is attributed to this agent.
        Type `ProvenanceAgent` (represented as `dict` in JSON). """
        
        self.display = None
        """ Human description of entity.
        Type `str`. """
        
        self.reference = None
        """ Identity of entity.
        Type `str`. """
        
        self.role = None
        """ derivation | revision | quotation | source.
        Type `str`. """
        
        self.type = None
        """ Entity Type.
        Type `Coding` (represented as `dict` in JSON). """
        
        super(ProvenanceEntity, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(ProvenanceEntity, self).elementProperties()
        js.extend([
            ("agent", "agent", ProvenanceAgent, False),
            ("display", "display", str, False),
            ("reference", "reference", str, False),
            ("role", "role", str, False),
            ("type", "type", coding.Coding, False),
        ])
        return js

