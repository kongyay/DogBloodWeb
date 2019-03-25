import json
from mongoengine import Document, EmbeddedDocument, connect
from mongoengine import StringField, ReferenceField, ListField, URLField, EmbeddedDocumentField, EmbeddedDocumentListField, DictField, BooleanField, IntField


class DogData(Document):
    owner_name = StringField(default='', required=True)
    dog_name = StringField(default='', required=True)
    dog_id = IntField(default=0, required=True, unique=True)

    def to_json(self):
        jsonObj = {}
        jsonObj["owner_name"] = self.owner_name
        jsonObj["dog_name"] = self.dog_name
        jsonObj["dog_id"] = self.dog_id
        return jsonObj


class Record(Document):
    dog_data = ReferenceField(DogData, required=True)
    classify_data = DictField(default={})

    def to_json(self):
        jsonObj = {}
        jsonObj["dog_data"] = self.dog_data.to_json()
        jsonObj["classify_data"] = self.classify_data or {}

        return jsonObj
