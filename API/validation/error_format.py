import json

class FormatValidationError():
    def __init__(self, error):
        self.error = error

    def schema_validation_error(self):
        # If the error is schema validation related, the below should help the user narrow down the issue
        try:
            # If the schema specifies a length e.g. Array must have 1 element
            if isinstance(self.error.validator_value, int):
                message = ("Error caused by '{}' attribute must be at least {} in length").format(self.error.path[0], self.error.validator_value)
            else:
                # Otherwise, it's most likely a type issue
                message = ("Error caused by '{}' attribute not being a {}").format(self.error.path[0], self.error.validator_value)
        except IndexError:
            # If we get this far, it's as an element is missing e.g. Service is missing from OD
            message = ("Error caused as {} is {}").format(self.error.validator_value, self.error.validator)
        except:
            # Otherwise, who knows?!
            message = ("Unknown Error, all I know for sure is {} caused it").format(self.error.validator_value)
        finally:
            # We can then spit out our message
            return (json.dumps({
                'success': False,
                'message' : message
            }), 400, {'ContentType': 'application/json'})

class UnknownError():
    def __init__(self, error):
        self.error = error
    
    def unknown_error(self):
        #({'success': True}), 201, {'ContentType': 'application/json'}
        message = ("{}").format(self.error)
        return (json.dumps({
            'success': False,
            'message' : message
        }), 500, {'ContentType': 'application/json'})