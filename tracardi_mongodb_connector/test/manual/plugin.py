from tracardi_mongodb_connector.plugin import MongoConnectorAction
from tracardi_plugin_sdk.service.plugin_runner import run_plugin


init = {
        "source": {
            "id": id
        },
        "mongo": {
            "database": "local",
            "collection": "startup_log"
        }
    }

payload = {}

result = run_plugin(MongoConnectorAction, init, payload)
print(result)
# async def main():
#     id = 'a3de6e9e-6558-45bd-a78f-d4ffc0346005'
#
#     plugin = await MongoConnectorAction.build(**{
#         "source": {
#             "id": id
#         },
#         "mongo": {
#             "database": "local",
#             "collection": "startup_log"
#         }
#     })
#
#     print(await plugin.run({}))
#
# asyncio.run(main())
