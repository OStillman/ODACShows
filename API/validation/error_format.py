import json

class FormatValidationError():
    def __init__(self, error):
        self.error = error

    def schema_validation_error(self):
        #({'success': True}), 201, {'ContentType': 'application/json'}
        try:
            if isinstance(self.error.validator_value, int):
                message = ("Error caused by '{}' attribute must be at least {} in length").format(self.error.path[0], self.error.validator_value)
            else:
                message = ("Error caused by '{}' attribute not being a {}").format(self.error.path[0], self.error.validator_value)
        except IndexError:
            message = ("Error caused as {} is {}").format(self.error.validator_value, self.error.validator)
        except:
            message = ("Unknown Error, all I know for sure is {} caused it").format(self.error.validator_value)
        finally:
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