#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 () on 2015-06-19.
#  2015, SMART Health IT.


import os
import io
import unittest
import json
import referralrequest
from fhirdate import FHIRDate


class ReferralRequestTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
        return referralrequest.ReferralRequest(js)
    
    def testReferralRequest1(self):
        inst = self.instantiate_from("referralrequest-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ReferralRequest instance")
        self.implReferralRequest1(inst)
        inst2 = referralrequest.ReferralRequest(inst.as_json())
        self.implReferralRequest1(inst2)
    
    def implReferralRequest1(self, inst):
        self.assertEqual(inst.dateSent.date, FHIRDate("2014-02-14").date)
        self.assertEqual(inst.dateSent.as_json(), "2014-02-14")
        self.assertEqual(inst.description, "In the past 2 years Beverly has had 6 instances of r) sided Otitis media. She is     falling behind her peers at school, and displaying some learning difficulties.")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.identifier[0].system, "http://orionhealth.com/fhir/apps/referralids")
        self.assertEqual(inst.identifier[0].value, "ret4421")
        self.assertEqual(inst.priority.coding[0].code, "med")
        self.assertEqual(inst.priority.coding[0].display, "Medium")
        self.assertEqual(inst.priority.coding[0].system, "http://orionhealth.com/fhir/apps/prioritycodes")
        self.assertEqual(inst.reason.text, "For consideration of Grommets")
        self.assertEqual(inst.serviceRequested[0].coding[0].code, "172676009")
        self.assertEqual(inst.serviceRequested[0].coding[0].display, "Myringotomy and insertion of tympanic ventilation tube")
        self.assertEqual(inst.serviceRequested[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.serviceRequested[0].text, "Insertion of grommets")
        self.assertEqual(inst.specialty.coding[0].code, "ent")
        self.assertEqual(inst.specialty.coding[0].display, "ENT")
        self.assertEqual(inst.specialty.coding[0].system, "http://orionhealth.com/fhir/apps/specialties")
        self.assertEqual(inst.status, "requested")
        self.assertEqual(inst.text.div, "<div>Referral to Dr Dave for Beverly weaver to have grommets inserted in her r) ear</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "rfs")
        self.assertEqual(inst.type.coding[0].display, "Referral for service")
        self.assertEqual(inst.type.coding[0].system, "http://orionhealth.com/fhir/apps/referraltypes")
    
    def testReferralRequest2(self):
        inst = self.instantiate_from("referralrequest-qicore-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ReferralRequest instance")
        self.implReferralRequest2(inst)
        inst2 = referralrequest.ReferralRequest(inst.as_json())
        self.implReferralRequest2(inst2)
    
    def implReferralRequest2(self, inst):
        self.assertEqual(inst.dateSent.date, FHIRDate("2014-02-14").date)
        self.assertEqual(inst.dateSent.as_json(), "2014-02-14")
        self.assertEqual(inst.extension[0].url, "http://hl7.org/fhir/StructureDefinition/referralrequest-reasonRefused")
        self.assertEqual(inst.extension[0].valueCodeableConcept.coding[0].code, "609589008")
        self.assertEqual(inst.extension[0].valueCodeableConcept.coding[0].display, "Refused by parents of subject")
        self.assertEqual(inst.extension[0].valueCodeableConcept.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.id, "qicore")
        self.assertEqual(inst.priority.coding[0].code, "394848005")
        self.assertEqual(inst.priority.coding[0].display, "Normal priority")
        self.assertEqual(inst.priority.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.reason.coding[0].code, "65363002")
        self.assertEqual(inst.reason.coding[0].display, "Otitis media")
        self.assertEqual(inst.reason.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.serviceRequested[0].coding[0].code, "172676009")
        self.assertEqual(inst.serviceRequested[0].coding[0].display, "Myringotomy and insertion of short-term tympanic ventilation tube (procedure)")
        self.assertEqual(inst.serviceRequested[0].coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.specialty.coding[0].code, "417887005")
        self.assertEqual(inst.specialty.coding[0].display, "Pediatric otolaryngology")
        self.assertEqual(inst.specialty.coding[0].system, "http://snomed.info/sct")
        self.assertEqual(inst.status, "rejected")
        self.assertEqual(inst.text.div, "<div>Referral to Dr Dave for Beverly weaver to have grommets inserted in her r) ear</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type.coding[0].code, "700274009")
        self.assertEqual(inst.type.coding[0].display, "Referral for procedure")
        self.assertEqual(inst.type.coding[0].system, "http://snomed.info/sct")

