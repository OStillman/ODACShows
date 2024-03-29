import jsonschema
from API.validation import error_format

class Validate_AddOD():
    def __init__(self, data):
        self.data = data
        self.schema = {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "service": {"type": "number"},
                "watching": {"type": "string"},
                "episode": {"type": "number"},
                "series": {"type": "number"},
                "tags":{
                    "type": "array",
                    "items": {"type": "string"},
                    "minItems": 1,
                    "uniqueItems": True
                }
            },
            "required": ["name", "service", "watching", "tags"]
        }

    def validate_data(self):
        try:
            jsonschema.validate(instance=self.data, schema=self.schema)
            return True
        except jsonschema.exceptions.ValidationError as error:
            # If the error is from jsonSchema there's been a validation error so we can give a good error output
            return error_format.FormatValidationError(error).schema_validation_error()
        except Exception as e:
            # Otherwise, something else has happened, and we need to figure out what...
            print(e)
            return error_format.UnknownError(str(e)).unknown_errorunknown_error()

            
        
        

