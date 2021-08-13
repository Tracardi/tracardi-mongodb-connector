import asyncio

from tracardi_mongodb_connector.plugin import MongoConnectorAction


async def main():
    id = '396f2f2b-82f9-44f0-ac71-fadec010ef18'

    plugin = await MongoConnectorAction.build(**{
        "source": {
            "id": id
        },
        "mongo": {
            "database": "local",
            "collection": "startup_log"
        }
    })

    print(await plugin.run({}))

asyncio.run(main())
