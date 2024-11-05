# Helper function to format the error messages
def format_error(error_type, key_path):
    return f"{error_type}: {key_path}"

def validate(data, template, path=''):
    """
    Validates if the structure of `data` matches the `template`.
    Args:
        data (dict): The dictionary to validate.
        template (dict): The template dictionary to validate against.
        path (str): The path to the current key, used for error reporting.

    Returns:
        tuple: A tuple (state, error), where `state` is a boolean indicating if validation passed,
               and `error` is an error message or an empty string if validation passed.
    """    
    # Iterate over each key-value pair in the template
    for key, expected_type in template.items():
        current_path = f"{path}.{key}" if path else key  # Construct the current key path
        
        # Check if the key exists in data
        if key not in data:
            return False, format_error("mismatched keys", current_path)
        
        # Check if the expected type is a dictionary
        if isinstance(expected_type, dict):
            # Recursively validate nested dictionaries
            if not isinstance(data[key], dict):
                return False, f'bad type: {current_path}'
            valid, error = validate(data[key], expected_type, current_path)
            if not valid:
                return valid, error
        else:
            # Check if the type of data[key] matches the expected type
            if not isinstance(data[key], expected_type):
                return False, format_error("bad type", current_path)
    
    # Check for any extra keys in data that are not in the template
    for key in data:
        if key not in template:
            current_path = f"{path}.{key}" if path else key
            return False, format_error("mismatched keys", current_path)
    
    # If no issues found, return True
    return True, ''
