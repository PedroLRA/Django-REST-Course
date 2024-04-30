from django.utils.translation import gettext_lazy as _

# In this file we should use gettext_lazy instead of gettext because we still
# don't have the language set up.
class ErrorMessages:
    NAME_SHOULD_BE_ONLY_LETTERS = _("Name should contain only letters.")
    CPF_SHOULD_CONTAIN_11_DIGITS = _('The CPF should contain 11 digits.')
    CPF_MUST_BE_VALID = _('The CPF must be valid.')
    RG_SHOULD_CONTAIN_9_DIGITS = _('The RG should contain 9 digits.')
    BIRTH_DATE_SHOULD_BE_PAST = _('The birth date should be in the past.')
    INVALID_COURSE_CODE_FORMAT = _('The course code should contain up to 5 letters followed up to 5 digits only.')
