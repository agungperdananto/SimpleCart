from flask_marshmallow import Schema
from flasgger import fields


# class WelcomeSchema(Schema):
#     class Meta:
#         # Fields to expose
#         fields = ["message", "id"]

#     message = fields.Str()
#     id = fields.Int()

class WelcomeSchema(Schema):
    messages = fields.Str()
# welcome_schema = {

#     "messages": "example messages"
# }