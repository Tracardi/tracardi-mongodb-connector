from tracardi_mongodb_connector.plugin import MongoConnectorAction
from tracardi_plugin_sdk.service.plugin_runner import run_plugin

init = {
    "source": {
        "id": "x"
    },
    "database": "None",
    "collection": "None",
    "query": "{}"

}

payload = {}

result = run_plugin(MongoConnectorAction, init, payload)
print(result)
