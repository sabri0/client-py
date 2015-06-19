#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 () on 2015-06-19.
#  2015, SMART Health IT.


import os
import io
import unittest
import json
import structuredefinition
from fhirdate import FHIRDate


class StructureDefinitionTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
        return structuredefinition.StructureDefinition(js)
    
    def testStructureDefinition1(self):
        inst = self.instantiate_from("structuredefinition-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a StructureDefinition instance")
        self.implStructureDefinition1(inst)
        inst2 = structuredefinition.StructureDefinition(inst.as_json())
        self.implStructureDefinition1(inst2)
    
    def implStructureDefinition1(self, inst):
        self.assertFalse(inst.abstract)
        self.assertEqual(inst.contact[0].telecom[0].system, "url")
        self.assertEqual(inst.contact[0].telecom[0].value, "grahame@healthintersections.com.au")
        self.assertEqual(inst.date.date, FHIRDate("2012-05-12").date)
        self.assertEqual(inst.date.as_json(), "2012-05-12")
        self.assertEqual(inst.description, "Describes how the lab report is used for a standard Lipid Profile - Cholesterol, Triglyceride and Cholesterol fractions. Uses LOINC codes")
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.name, "Example Lipid Profile")
        self.assertEqual(inst.publisher, "Grahame Grieve")
        self.assertEqual(inst.snapshot.element[0].definition, "The findings and interpretation of a general lipd lab profile.")
        self.assertFalse(inst.snapshot.element[0].isModifier)
        self.assertEqual(inst.snapshot.element[0].max, "1")
        self.assertEqual(inst.snapshot.element[0].min, 1)
        self.assertEqual(inst.snapshot.element[0].name, "LipidProfile")
        self.assertEqual(inst.snapshot.element[0].path, "DiagnosticReport")
        self.assertEqual(inst.snapshot.element[0].short, "Lipid Lab Report")
        self.assertEqual(inst.snapshot.element[0].type[0].code, "Resource")
        self.assertFalse(inst.snapshot.element[1].isModifier)
        self.assertEqual(inst.snapshot.element[1].max, "*")
        self.assertEqual(inst.snapshot.element[1].min, 0)
        self.assertEqual(inst.snapshot.element[1].path, "DiagnosticReport.extension")
        self.assertEqual(inst.snapshot.element[1].short, "Additional Content defined by implementations")
        self.assertEqual(inst.snapshot.element[1].slicing.discriminator[0], "url")
        self.assertFalse(inst.snapshot.element[1].slicing.ordered)
        self.assertEqual(inst.snapshot.element[1].slicing.rules, "open")
        self.assertEqual(inst.snapshot.element[1].type[0].code, "Extension")
        self.assertEqual(inst.snapshot.element[2].alias[0], "narrative")
        self.assertEqual(inst.snapshot.element[2].alias[1], "html")
        self.assertEqual(inst.snapshot.element[2].alias[2], "xhtml")
        self.assertEqual(inst.snapshot.element[2].alias[3], "display")
        self.assertEqual(inst.snapshot.element[2].comments, "Contained resources do not have narrative. Resources that are not contained SHOULD have a narrative.")
        self.assertFalse(inst.snapshot.element[2].isModifier)
        self.assertEqual(inst.snapshot.element[2].max, "1")
        self.assertEqual(inst.snapshot.element[2].min, 0)
        self.assertEqual(inst.snapshot.element[2].path, "DiagnosticReport.text")
        self.assertEqual(inst.snapshot.element[2].short, "Text summary of the resource, for human interpretation")
        self.assertEqual(inst.snapshot.element[2].type[0].code, "Narrative")
        self.assertEqual(inst.snapshot.element[3].alias[0], "inline resources")
        self.assertEqual(inst.snapshot.element[3].alias[1], "anonymous resources")
        self.assertEqual(inst.snapshot.element[3].alias[2], "contained resources")
        self.assertEqual(inst.snapshot.element[3].comments, "This should never be done when the content can be identified properly, as once identification is lost, it is extremely difficult (and context dependent) to restore it again.")
        self.assertFalse(inst.snapshot.element[3].isModifier)
        self.assertEqual(inst.snapshot.element[3].max, "*")
        self.assertEqual(inst.snapshot.element[3].min, 0)
        self.assertEqual(inst.snapshot.element[3].path, "DiagnosticReport.contained")
        self.assertEqual(inst.snapshot.element[3].short, "Contained, inline Resources")
        self.assertEqual(inst.snapshot.element[3].type[0].code, "Resource")
        self.assertEqual(inst.snapshot.element[4].binding.name, "ObservationStatus")
        self.assertEqual(inst.snapshot.element[4].binding.strength, "required")
        self.assertEqual(inst.snapshot.element[4].comments, "This is labeled as \"Is Modifier\" because applications need to take appropriate action if a report is withdrawn.")
        self.assertEqual(inst.snapshot.element[4].definition, "The status of the diagnostic report as a whole.")
        self.assertFalse(inst.snapshot.element[4].isModifier)
        self.assertEqual(inst.snapshot.element[4].max, "1")
        self.assertEqual(inst.snapshot.element[4].min, 1)
        self.assertEqual(inst.snapshot.element[4].path, "DiagnosticReport.status")
        self.assertEqual(inst.snapshot.element[4].short, "registered|interim|final|amended|cancelled|withdrawn")
        self.assertEqual(inst.snapshot.element[4].type[0].code, "code")
        self.assertEqual(inst.snapshot.element[5].comments, "May be different from the update time of the resource itself, because that is the status of the record (potentially a secondary copy), not the actual release time of the report.")
        self.assertEqual(inst.snapshot.element[5].definition, "The date and/or time that this version of the report was released from the source diagnostic service.")
        self.assertFalse(inst.snapshot.element[5].isModifier)
        self.assertEqual(inst.snapshot.element[5].max, "1")
        self.assertEqual(inst.snapshot.element[5].min, 1)
        self.assertEqual(inst.snapshot.element[5].path, "DiagnosticReport.issued")
        self.assertEqual(inst.snapshot.element[5].short, "Date this version was released")
        self.assertEqual(inst.snapshot.element[5].type[0].code, "dateTime")
        self.assertEqual(inst.snapshot.element[6].definition, "The subject of the report. Usually, but not always, this is a patient. However diagnostic services also perform analyses on specimens collected from a variety of other sources.")
        self.assertFalse(inst.snapshot.element[6].isModifier)
        self.assertEqual(inst.snapshot.element[6].max, "1")
        self.assertEqual(inst.snapshot.element[6].min, 1)
        self.assertEqual(inst.snapshot.element[6].path, "DiagnosticReport.subject")
        self.assertEqual(inst.snapshot.element[6].short, "The subject of the report")
        self.assertEqual(inst.snapshot.element[6].type[0].code, "Reference(Patient|Group|Device)")
        self.assertEqual(inst.snapshot.element[7].comments, "This is not necessarily the source of the atomic data items - it's the entity that takes responsibility for the clinical report.")
        self.assertEqual(inst.snapshot.element[7].definition, "The diagnostic service that is responsible for issuing the report.")
        self.assertFalse(inst.snapshot.element[7].isModifier)
        self.assertEqual(inst.snapshot.element[7].max, "1")
        self.assertEqual(inst.snapshot.element[7].min, 1)
        self.assertEqual(inst.snapshot.element[7].path, "DiagnosticReport.performer")
        self.assertEqual(inst.snapshot.element[7].short, "Responsible Diagnostic Service")
        self.assertEqual(inst.snapshot.element[7].type[0].code, "Reference(Organization)")
        self.assertEqual(inst.snapshot.element[8].definition, "The local ID assigned to the report by the order filler, usually by the Information System of the diagnostic service provider.")
        self.assertFalse(inst.snapshot.element[8].isModifier)
        self.assertEqual(inst.snapshot.element[8].max, "1")
        self.assertEqual(inst.snapshot.element[8].min, 0)
        self.assertEqual(inst.snapshot.element[8].path, "DiagnosticReport.reportId")
        self.assertEqual(inst.snapshot.element[8].short, "Id for external references to this report")
        self.assertEqual(inst.snapshot.element[8].type[0].code, "Identifier")
        self.assertEqual(inst.snapshot.element[9].definition, "Details concerning a single pathology test requested.")
        self.assertFalse(inst.snapshot.element[9].isModifier)
        self.assertEqual(inst.snapshot.element[9].max, "*")
        self.assertEqual(inst.snapshot.element[9].min, 0)
        self.assertEqual(inst.snapshot.element[9].path, "DiagnosticReport.requestDetail")
        self.assertEqual(inst.snapshot.element[9].short, "What was requested")
        self.assertEqual(inst.status, "draft")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.type, "constraint")
        self.assertEqual(inst.url, "http://hl7.org/fhir/StructureDefinition/example")

