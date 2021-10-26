import json
from json import JSONDecodeError
from typing import Any, Union
from pydantic import BaseModel, validator
from tracardi.domain.entity import Entity


class MongoConfiguration(BaseModel):
    uri: str
    timeout: int = 5000


class PluginConfiguration(BaseModel):
    source: Entity
    database: str
    collection: str
    query: Union[str, Any] = "{}"

    @validator("query")
    def is_json(cls, value):
        try:
            return json.loads(value)
        except JSONDecodeError as e:
            raise ValueError("Can not parse this data as JSON. Error: `{}`".format(str(e)))
