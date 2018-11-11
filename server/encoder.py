# from https://stackoverflow.com/questions/5160077/encoding-nested-python-object-in-json
import json
class encoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj,'encoder'):
            return obj.encoder()
        else:
            return json.JSONEncoder.default(self, obj)