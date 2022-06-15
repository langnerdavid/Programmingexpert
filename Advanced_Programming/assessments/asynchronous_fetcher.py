import asyncio

class BatchFetcher:
    # The `database` has an `async_fetch` method
    # that you should use in your code. This method
    # takes in a record id and returns a record.
    def __init__(self, database):
        self.database = database
        

    async def fetch_records(self,record_ids):
        records = []

        for _id in record_ids:
            #data = {"data": None}
            storage = asyncio.create_task(self.database.async_fetch(_id))
            #data["data"] = storage
            #await storage -> not possible because of runtime
            records.append(storage)

        rec = []  
        for r in records:
            rec.append(await r) 

        #return(await asyncio.gather(*records))
        return rec
