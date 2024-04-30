from rest_framework.serializers import ValidationError
from django.utils import timezone
from validate_docbr import CPF
from apps.school.error_messages import ErrorMessages
import re

# Custom validation to Student model
def validate_name(name):
    if not name.isalpha():
        raise ValidationError(ErrorMessages.NAME_SHOULD_BE_ONLY_LETTERS)
    return name

def validate_doc_cpf(doc_cpf):
    if len(doc_cpf) != 11:
        raise ValidationError(ErrorMessages.CPF_SHOULD_CONTAIN_11_DIGITS)
    if not CPF().validate(doc_cpf):
        raise ValidationError(ErrorMessages.CPF_MUST_BE_VALID)    
    return doc_cpf

def validate_doc_rg(doc_rg):
    if len(doc_rg) != 9:
        raise ValidationError(ErrorMessages.RG_SHOULD_CONTAIN_9_DIGITS)
    return doc_rg

def validate_birth(birth):
    if birth > timezone.now().date():
        raise ValidationError(ErrorMessages.BIRTH_DATE_SHOULD_BE_PAST)
    return birth

# Custom validation to Course model
def validate_code(code):
    """
    Verify if the course code has:
        - max of 5 letters
        - max of 5 digits
    """

    #Regex expression to check 1 to 5 letters followed by 1 to 5 digits
    code_pattern = '^[a-zA-Z]{1,5}[0-9]{1,5}$'
    
    if not re.match(code_pattern, code):
        raise ValidationError(ErrorMessages.INVALID_COURSE_CODE_FORMAT)
    return code

# Function to run validations
def run_validators(data, validators):
    """
    Validate the data for each key in the validators dictionary where the key
    is the field name and the value is the validation function to be executed.
    """

    errors = {}

    for field, validator in validators.items():
        try:
            data[field] = validator(data[field])
        except ValidationError as e:
            errors[field] = e.detail

    if errors:
        raise ValidationError(errors)
