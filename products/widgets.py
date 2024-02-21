'''Code from Boutique Ado walkthrough:
https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/
f5880efee43b3b9ea1276a09ca972f4588001c59/products/widgets.py '''

from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = 'products/custom_widget_templates/custom_clearable_file_input.html'