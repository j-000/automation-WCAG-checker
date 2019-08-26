from server import ma
from custommodels import User, Checkpoint, Report

class UserSchema(ma.ModelSchema):
  class Meta:
    model = User
    fields = ('id', 'token', 'name', 'is_admin', 'scan_quota')

class CheckpointSchema(ma.ModelSchema):
  class Meta:
    model = Checkpoint
    # all fields public

class ReportSchema(ma.ModelSchema):
  class Meta:
    model = Report
    # all fields public
