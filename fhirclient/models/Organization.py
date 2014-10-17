#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.0.82.2943 (organization.profile.json) on 2014-10-17.
#  2014, SMART Platforms.

# We need to support importing other generated classes without relying on the
# models being part of a specific module. To do so we prepend the current
# directory sys.path - better solutions are welcome!
import sys
import os.path
abspath = os.path.abspath(os.path.dirname(__file__))
if abspath not in sys.path:
    sys.path.insert(0, abspath)


import Address
import CodeableConcept
import Contact
import FHIRElement
import FHIRReference
import FHIRResource
import HumanName
import Identifier
import Location
import Narrative


class Organization(FHIRResource.FHIRResource):
    """ A grouping of people or organizations with a common purpose.
    
    Scope and Usage This resource may be used in a shared registry of contact
    and other information for various organizations or it can be used merely as
    a support for other resources that need to reference organizations, perhaps
    as a document, message or as a contained resource. If using a registry
    approach, it's entirely possible for multiple registries to exist, each
    dealing with different types or levels of organization.
    """
    
    resource_name = "Organization"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.active = False
        """ Whether the organization's record is still in active use.
        Type `bool`. """
        
        self.address = None
        """ An address for the organization.
        List of `Address` items (represented as `dict` in JSON). """
        
        self.contact = None
        """ Contact for the organization for a certain purpose.
        List of `OrganizationContact` items (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Identifies this organization  across multiple systems.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.location = None
        """ Location(s) the organization uses to provide services.
        List of `FHIRReference` items referencing `Location` (represented as `dict` in JSON). """
        
        self.name = None
        """ Name used for the organization.
        Type `str`. """
        
        self.partOf = None
        """ The organization of which this organization forms a part.
        Type `FHIRReference` referencing `Organization` (represented as `dict` in JSON). """
        
        self.telecom = None
        """ A contact detail for the organization.
        List of `Contact` items (represented as `dict` in JSON). """
        
        self.text = None
        """ Text summary of the resource, for human interpretation.
        Type `Narrative` (represented as `dict` in JSON). """
        
        self.type = None
        """ Kind of organization.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        super(Organization, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(Organization, self).update_with_json(jsondict)
        if 'active' in jsondict:
            self.active = jsondict['active']
        if 'address' in jsondict:
            self.address = Address.Address.with_json(jsondict['address'])
        if 'contact' in jsondict:
            self.contact = OrganizationContact.with_json(jsondict['contact'])
        if 'identifier' in jsondict:
            self.identifier = Identifier.Identifier.with_json(jsondict['identifier'])
        if 'location' in jsondict:
            self.location = FHIRReference.FHIRReference.with_json_and_owner(jsondict['location'], self, Location.Location)
        if 'name' in jsondict:
            self.name = jsondict['name']
        if 'partOf' in jsondict:
            self.partOf = FHIRReference.FHIRReference.with_json_and_owner(jsondict['partOf'], self, Organization)
        if 'telecom' in jsondict:
            self.telecom = Contact.Contact.with_json(jsondict['telecom'])
        if 'text' in jsondict:
            self.text = Narrative.Narrative.with_json(jsondict['text'])
        if 'type' in jsondict:
            self.type = CodeableConcept.CodeableConcept.with_json(jsondict['type'])


class OrganizationContact(FHIRElement.FHIRElement):
    """ Contact for the organization for a certain purpose.
    """
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.address = None
        """ Visiting or postal addresses for the contact.
        Type `Address` (represented as `dict` in JSON). """
        
        self.gender = None
        """ Gender for administrative purposes.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.name = None
        """ A name associated with the contact.
        Type `HumanName` (represented as `dict` in JSON). """
        
        self.purpose = None
        """ The type of contact.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.telecom = None
        """ Contact details (telephone, email, etc)  for a contact.
        List of `Contact` items (represented as `dict` in JSON). """
        
        super(OrganizationContact, self).__init__(jsondict)
    
    def update_with_json(self, jsondict):
        super(OrganizationContact, self).update_with_json(jsondict)
        if 'address' in jsondict:
            self.address = Address.Address.with_json(jsondict['address'])
        if 'gender' in jsondict:
            self.gender = CodeableConcept.CodeableConcept.with_json(jsondict['gender'])
        if 'name' in jsondict:
            self.name = HumanName.HumanName.with_json(jsondict['name'])
        if 'purpose' in jsondict:
            self.purpose = CodeableConcept.CodeableConcept.with_json(jsondict['purpose'])
        if 'telecom' in jsondict:
            self.telecom = Contact.Contact.with_json(jsondict['telecom'])

