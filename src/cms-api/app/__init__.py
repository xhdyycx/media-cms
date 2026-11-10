import urllib3.fields
if not hasattr(urllib3.fields, 'format_header_param') and hasattr(urllib3.fields, 'format_header_param_rfc2231'):
    urllib3.fields.format_header_param = urllib3.fields.format_header_param_rfc2231


# Note: Decompiled code can be incomplete and incorrect.

