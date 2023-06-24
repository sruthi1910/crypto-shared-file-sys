
import pymongo


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = myclient["file-split"]


collection = db["poa"] # POA = Proof of authencity


def insert_into_mongo(filename, merkle_root):
    data = {
        "filename" : filename,
        "merkle_root" : merkle_root
    }
    is_exist = list(collection.find({"filename" : filename}))
    print(is_exist)
    if is_exist == []:
        print("New file")
        done = collection.insert_one(data)
        print(done)
        if done == None:
            print ("Some problem with Mongo DB. Check the database")
    else:
        query = {"filename" : filename}
        update = {"$set" : {"merkle_root" : merkle_root}}
        done = collection.update_one(query, update)
        print(done)
        if done == None:
            print("Some problem with Mongo DB. Check the database")


def find_mongo(filename):
    query = {
        "filename" : filename,
    }


    data = list(collection.find(query))
    if data == {}:
        return None
    else:
        return data[0]["merkle_root"]
