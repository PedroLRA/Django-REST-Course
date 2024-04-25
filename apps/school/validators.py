from rest_framework.serializers import ValidationError
from django.utils import timezone
from validate_docbr import CPF

import re

# Custom validation to Student model
def validate_name(name):
    if not name.isalpha():
        raise ValidationError('The name should only contain letters')
    return name

def validate_doc_cpf(doc_cpf):
    if len(doc_cpf) != 11:
        raise ValidationError('The CPF should contain 11 digits')
    if not CPF().validate(doc_cpf):
        raise ValidationError('The CPF must be valid')    
    return doc_cpf

def validate_doc_rg(doc_rg):
    if len(doc_rg) != 9:
        raise ValidationError('The RG should contain 9 digits')
    return doc_rg

def validate_birth(birth):
    if birth > timezone.now().date():
        raise ValidationError('The birth date should be in the past')
    return birth
