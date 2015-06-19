#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 () on 2015-06-19.
#  2015, SMART Health IT.


import os
import io
import unittest
import json
import imagingstudy
from fhirdate import FHIRDate


class ImagingStudyTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
        return imagingstudy.ImagingStudy(js)
    
    def testImagingStudy1(self):
        inst = self.instantiate_from("imagingstudy-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ImagingStudy instance")
        self.implImagingStudy1(inst)
        inst2 = imagingstudy.ImagingStudy(inst.as_json())
        self.implImagingStudy1(inst2)
    
    def implImagingStudy1(self, inst):
        self.assertEqual(inst.id, "example")
        self.assertEqual(inst.numberOfInstances, 1)
        self.assertEqual(inst.numberOfSeries, 1)
        self.assertEqual(inst.series[0].bodySite.code, "67734004")
        self.assertEqual(inst.series[0].bodySite.display, "Upper Trunk Structure")
        self.assertEqual(inst.series[0].bodySite.system, "http://snomed.info/sct")
        self.assertEqual(inst.series[0].description, "CT Surview 180")
        self.assertEqual(inst.series[0].instance[0].content[0].url, "http://localhost/fhir/Binary/1.2.840.11361907579238403408700.3.0.14.19970327150033")
        self.assertEqual(inst.series[0].instance[0].number, 1)
        self.assertEqual(inst.series[0].instance[0].sopclass, "urn:oid:1.2.840.10008.5.1.4.1.1.2")
        self.assertEqual(inst.series[0].instance[0].uid, "urn:oid:2.16.124.113543.6003.189642796.63084.16748.2599092903")
        self.assertEqual(inst.series[0].modality, "CT")
        self.assertEqual(inst.series[0].number, 3)
        self.assertEqual(inst.series[0].numberOfInstances, 1)
        self.assertEqual(inst.series[0].uid, "urn:oid:2.16.124.113543.6003.2588828330.45298.17418.2723805630")
        self.assertEqual(inst.started.date, FHIRDate("2011-01-01T11:01:20+03:00").date)
        self.assertEqual(inst.started.as_json(), "2011-01-01T11:01:20+03:00")
        self.assertEqual(inst.text.div, "<div>Image 1 from Series 3: CT Images on Patient MINT (MINT1234) taken at 1-Jan 2011 01:20 AM</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.uid, "urn:oid:2.16.124.113543.6003.1154777499.30246.19789.3503430045")
    
    def testImagingStudy2(self):
        inst = self.instantiate_from("imagingstudy-qicore-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ImagingStudy instance")
        self.implImagingStudy2(inst)
        inst2 = imagingstudy.ImagingStudy(inst.as_json())
        self.implImagingStudy2(inst2)
    
    def implImagingStudy2(self, inst):
        self.assertEqual(inst.extension[0].url, "http://hl7.org/fhir/StructureDefinition/imagingstudy-radiationDose")
        self.assertEqual(inst.extension[0].valueRange.high.units, "Gy")
        self.assertEqual(inst.extension[0].valueRange.high.value, 1234.5)
        self.assertEqual(inst.extension[0].valueRange.low.units, "Gy")
        self.assertEqual(inst.extension[0].valueRange.low.value, 200.0)
        self.assertEqual(inst.extension[1].url, "http://hl7.org/fhir/StructureDefinition/imagingstudy-radiationDuration")
        self.assertEqual(inst.extension[1].valueQuantity.code, "s")
        self.assertEqual(inst.extension[1].valueQuantity.system, "http://unitsofmeasure.org")
        self.assertEqual(inst.extension[1].valueQuantity.units, "sec")
        self.assertEqual(inst.extension[1].valueQuantity.value, 25)
        self.assertEqual(inst.id, "qicore")
        self.assertEqual(inst.numberOfInstances, 1)
        self.assertEqual(inst.numberOfSeries, 1)
        self.assertEqual(inst.series[0].bodySite.code, "67734004")
        self.assertEqual(inst.series[0].bodySite.display, "Upper Trunk Structure")
        self.assertEqual(inst.series[0].bodySite.system, "http://snomed.info/sct")
        self.assertEqual(inst.series[0].description, "CT Surview 180")
        self.assertEqual(inst.series[0].instance[0].content[0].url, "http://localhost/fhir/Binary/1.2.840.11361907579238403408700.3.0.14.19970327150033")
        self.assertEqual(inst.series[0].instance[0].number, 1)
        self.assertEqual(inst.series[0].instance[0].sopclass, "urn:oid:1.2.840.10008.5.1.4.1.1.2")
        self.assertEqual(inst.series[0].instance[0].uid, "urn:oid:2.16.124.113543.6003.189642796.63084.16748.2599092903")
        self.assertEqual(inst.series[0].modality, "CT")
        self.assertEqual(inst.series[0].number, 3)
        self.assertEqual(inst.series[0].numberOfInstances, 1)
        self.assertEqual(inst.series[0].uid, "urn:oid:2.16.124.113543.6003.2588828330.45298.17418.2723805630")
        self.assertEqual(inst.started.date, FHIRDate("2011-01-01T11:01:20+03:00").date)
        self.assertEqual(inst.started.as_json(), "2011-01-01T11:01:20+03:00")
        self.assertEqual(inst.text.div, "<div>Image 1 from Series 3: CT Images on Patient MINT (MINT1234) taken at 1-Jan 2011 01:20 AM</div>")
        self.assertEqual(inst.text.status, "generated")
        self.assertEqual(inst.uid, "urn:oid:2.16.124.113543.6003.1154777499.30246.19789.3503430045")

