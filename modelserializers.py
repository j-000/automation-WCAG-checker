from server import ma
from custommodels import User, Checkpoint, Report, Invoice, Scan

class UserSchema(ma.ModelSchema):
  class Meta:
    model = User
    # all fields public

class CheckpointSchema(ma.ModelSchema):
  class Meta:
    model = Checkpoint
    # all fields public

class ReportSchema(ma.ModelSchema):
  class Meta:
    model = Report
    # all fields public

class ScanSchema(ma.ModelSchema):
  class Meta:
    model = Scan
    # all fields public

class InvoiceSchema(ma.ModelSchema):
  class Meta:
    model = Invoice
    # all fields public
