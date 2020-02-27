from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, BLOB
from datetime import datetime

Base = declarative_base()


class ttrf(Base):
    __tablename__ = 'ttrf'
    
    id = Column(Integer, primary_key=True)
    tech_owner = Column(String)
    owner_contact = Column(String)
    data_recipient = Column(String)
    recipient_location = Column(String)
    is_final_dst = Column(Boolean)
    final_dst = Column(String)
    export_requester = Column(String)
    date_req = Column(DateTime)
    method_export = Column(String)
    purpose_export = Column(String)
    ip_owner = Column(String)
    tech_describe = Column(String)
    ecl = Column(String)
    eccn = Column(String)
    usml = Column(String)
    cg = Column(String)
    sme_decision = Column(Boolean)
    sme_reason = Column(String)
    sme_name = Column(String)
    sme_decision_date = Column(DateTime)
    ecm_decision = Column(Boolean)
    ecm_reason = Column(String)
    ecm_name = Column(String)
    ecm_decision_date = Column(DateTime)
    ecm_license_req = Column(Boolean)
    ecm_license_no = Column(String)
    ecm_license_expiry_date = Column(DateTime)
    date_ini_export = Column(DateTime)
    export_recipient = Column(String)
    method_transfer = Column(String)
    exported_by = Column(String)
    export_is_completed = Column(Boolean)
    record_num = Column(Integer)
    uploaded_file = Column(BLOB)
    
    def __str__(self):
        return "tech_owner: %s, owner_contact: %s, data_recipient: %s, recipient_location: %s, is_final_dst: %s, final_dst: %s," \
            "export_requester: %s, date_req: %s, method_export: %s, purpose_export: %s, ip_owner: %s, tech_describe: %s, ecl: %s," \
            "eccn: %s, usml: %s, cg: %s, sme_decision: %s, sme_reason: %s, sme_name: %s, sme_signature: %s, sme_decision_date: %s," \
            "ecm_decision: %s, ecm_reason: %s, ecm_name: %s, ecm_signature: %s, ecm_decision_date: %s, ecm_license_req: %s, ecm_license_no: %s," \
            "ecm_license_expiry_date: %s, date_ini_export: %s, export_recipient: %s, method_transfer: %s, exported_by: %s, export_is_completed: %s," \
            "record_num: %s, uploaded_file: %s" % \
        (self.tech_owner, self.owner_contact, self.data_recipient, self.recipient_location, self.is_final_dst, self.final_dst, \
        self.export_requester, self.date_req, self.method_export, self.purpose_export, self.ip_owner, self.tech_describe, self.ecl, \
        self.eccn, self.usml, self.cg, self.sme_decision, self.sme_reason, self.sme_name, self.sme_signature, self.sme_decision_date, \
        self.ecm_decision, self.ecm_reason, self.ecm_name, self.ecm_signature, self.ecm_decision_date, self.ecm_license_req, self.ecm_license_no, \
        self.ecm_license_expiry_date, self.date_ini_export, self.export_recipient, self.method_transfer, self.exported_by, self.export_is_completed, \
        self.record_num, self.uploaded_file)

    def serialize(self):
        return {
            'tech_owner' : self.tech_owner,
            'owner_contact' : self.owner_contact,
            'data_recipient' : self.data_recipient,
            'recipient_location' : self.recipient_location,
            'is_final_dst' : self.is_final_dst,
            'final_dst' : self.final_dst,
            'export_requester' : self.export_requester,
            'date_req' : self.date_req,
            'method_export' : self.method_export,
            'purpose_export' : self.purpose_export,
            'ip_owner' : self.ip_owner,
            'tech_describe' : self.tech_describe,
            'ecl' : self.ecl,
            'eccn' : self.eccn,
            'usml' : self.usml,
            'cg' : self.cg,
            'sme_decision' : self.sme_decision,
            'sme_reason' : self.sme_reason,
            'sme_name' : self.sme_name,
            'sme_signature' : self.sme_signature,
            'sme_decision_date' : self.sme_decision_date,
            'ecm_decision' : self.ecm_decision,
            'ecm_reason' : self.ecm_reason,
            'ecm_name' : self.ecm_name,
            'ecm_signature' : self.ecm_signature,
            'ecm_decision_date' : self.ecm_decision_date,
            'ecm_license_req' : self.ecm_license_req,
            'ecm_license_no' : self.ecm_license_no,
            'ecm_license_expiry_date' : self.ecm_license_expiry_date,
            'date_ini_export' : self.date_ini_export,
            'export_recipient' : self.export_recipient,
            'method_transfer' : self.method_transfer,
            'exported_by' : self.exported_by,
            'export_is_completed' : self.export_is_completed,
            'record_num' : self.record_num,
            'uploaded_file' : self.uploaded_file
        }

    def StringToSqlType(self):
        self.is_final_dst = eval(self.is_final_dst)
        self.sme_decision = eval(self.sme_decision)
        self.ecm_decision = eval(self.ecm_decision)
        self.ecm_license_req = eval(self.ecm_license_req)
        self.export_is_completed = eval(self.export_is_completed)

        self.date_req = datetime.strptime(self.date_req, '%Y-%m-%d')
        self.sme_decision_date = datetime.strptime(self.sme_decision_date, '%Y-%m-%d')
        self.ecm_decision_date = datetime.strptime(self.ecm_decision_date, '%Y-%m-%d')
        self.ecm_license_expiry_date = datetime.strptime(self.ecm_license_expiry_date, '%Y-%m-%d')
        self.date_ini_export = datetime.strptime(self.date_ini_export, '%Y-%m-%d')

        self.record_num = int(self.record_num)