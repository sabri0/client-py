#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 0.5.0.5149 (http://hl7.org/fhir/StructureDefinition/DiagnosticReport) on 2015-06-19.
#  2015, SMART Health IT.


import attachment
import codeableconcept
import domainresource
import fhirdate
import fhirelement
import fhirreference
import identifier
import period


class DiagnosticReport(domainresource.DomainResource):
    """ A Diagnostic report - a combination of request information, atomic results,
    images, interpretation, as well as formatted reports.
    
    The findings and interpretation of diagnostic  tests performed on patients,
    groups of patients, devices, and locations, and/or specimens derived from
    these. The report includes clinical context such as requesting and provider
    information, and some mix of atomic results, images, textual and coded
    interpretation, and formatted representation of diagnostic reports.
    """
    
    resource_name = "DiagnosticReport"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.codedDiagnosis = None
        """ Codes for the conclusion.
        List of `CodeableConcept` items (represented as `dict` in JSON). """
        
        self.conclusion = None
        """ Clinical Interpretation of test results.
        Type `str`. """
        
        self.diagnosticDateTime = None
        """ Physiologically Relevant time/time-period for report.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.diagnosticPeriod = None
        """ Physiologically Relevant time/time-period for report.
        Type `Period` (represented as `dict` in JSON). """
        
        self.encounter = None
        """ Health care event when test ordered.
        Type `FHIRReference` referencing `Encounter` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Id for external references to this report.
        List of `Identifier` items (represented as `dict` in JSON). """
        
        self.image = None
        """ Key images associated with this report.
        List of `DiagnosticReportImage` items (represented as `dict` in JSON). """
        
        self.imagingStudy = None
        """ Reference to full details of imaging associated with the diagnostic
        report.
        List of `FHIRReference` items referencing `ImagingStudy` (represented as `dict` in JSON). """
        
        self.issued = None
        """ Date this version was released.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.name = None
        """ Name/Code for this diagnostic report.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.performer = None
        """ Responsible Diagnostic Service.
        Type `FHIRReference` referencing `Practitioner, Organization` (represented as `dict` in JSON). """
        
        self.presentedForm = None
        """ Entire Report as issued.
        List of `Attachment` items (represented as `dict` in JSON). """
        
        self.requestDetail = None
        """ What was requested.
        List of `FHIRReference` items referencing `DiagnosticOrder` (represented as `dict` in JSON). """
        
        self.result = None
        """ Observations - simple, or complex nested groups.
        List of `FHIRReference` items referencing `Observation` (represented as `dict` in JSON). """
        
        self.serviceCategory = None
        """ Biochemistry, Hematology etc..
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.specimen = None
        """ Specimens this report is based on.
        List of `FHIRReference` items referencing `Specimen` (represented as `dict` in JSON). """
        
        self.status = None
        """ registered | partial | final | corrected | appended | cancelled |
        entered-in-error.
        Type `str`. """
        
        self.subject = None
        """ The subject of the report, usually, but not always, the patient.
        Type `FHIRReference` referencing `Patient, Group, Device, Location` (represented as `dict` in JSON). """
        
        super(DiagnosticReport, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(DiagnosticReport, self).elementProperties()
        js.extend([
            ("codedDiagnosis", "codedDiagnosis", codeableconcept.CodeableConcept, True),
            ("conclusion", "conclusion", str, False),
            ("diagnosticDateTime", "diagnosticDateTime", fhirdate.FHIRDate, False),
            ("diagnosticPeriod", "diagnosticPeriod", period.Period, False),
            ("encounter", "encounter", fhirreference.FHIRReference, False),
            ("identifier", "identifier", identifier.Identifier, True),
            ("image", "image", DiagnosticReportImage, True),
            ("imagingStudy", "imagingStudy", fhirreference.FHIRReference, True),
            ("issued", "issued", fhirdate.FHIRDate, False),
            ("name", "name", codeableconcept.CodeableConcept, False),
            ("performer", "performer", fhirreference.FHIRReference, False),
            ("presentedForm", "presentedForm", attachment.Attachment, True),
            ("requestDetail", "requestDetail", fhirreference.FHIRReference, True),
            ("result", "result", fhirreference.FHIRReference, True),
            ("serviceCategory", "serviceCategory", codeableconcept.CodeableConcept, False),
            ("specimen", "specimen", fhirreference.FHIRReference, True),
            ("status", "status", str, False),
            ("subject", "subject", fhirreference.FHIRReference, False),
        ])
        return js


class DiagnosticReportImage(fhirelement.FHIRElement):
    """ Key images associated with this report.
    
    A list of key images associated with this report. The images are generally
    created during the diagnostic process, and may be directly of the patient,
    or of treated specimens (i.e. slides of interest).
    """
    
    resource_name = "DiagnosticReportImage"
    
    def __init__(self, jsondict=None):
        """ Initialize all valid properties.
        """
        
        self.comment = None
        """ Comment about the image (e.g. explanation).
        Type `str`. """
        
        self.link = None
        """ Reference to the image source.
        Type `FHIRReference` referencing `Media` (represented as `dict` in JSON). """
        
        super(DiagnosticReportImage, self).__init__(jsondict)
    
    def elementProperties(self):
        js = super(DiagnosticReportImage, self).elementProperties()
        js.extend([
            ("comment", "comment", str, False),
            ("link", "link", fhirreference.FHIRReference, False),
        ])
        return js

