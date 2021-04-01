
from pymongo import MongoClient

db_address = 'mongodb://127.0.0.1:27017/'

def insert(**var_args):

    with MongoClient(db_address) as client:		# your ip

        db_name = var_args['db_name']
        target_db = client[db_name]						# get Database

        collaction_name = var_args['collaction_name']
        if (collaction_name not in target_db.list_collection_names()):
            target_db.create_collection(collaction_name)

        data = var_args['data']
        if not data :
            result = 'empty data'
        else :
            try:                
                if len(data) <= 1 :
                    result = target_db[collaction_name].insert_one(data)
                else :
                    result = target_db[collaction_name].insert_many(data)
            except:
                pass
    
    return result

def find(**var_args):

    with MongoClient(db_address)  as client:		# your ip
        db_name = var_args['db_name']
        target_db = client[db_name]						# get Database

        collaction_name = var_args['collaction_name']
        if (collaction_name not in target_db.list_collection_names()):
            target_db.create_collection(collaction_name)

        result = target_db[collaction_name].find({})     # get Collection with find()
    
    return result

def remove(**var_args):

    with MongoClient(db_address)  as client:		# your ip
        db_name = var_args['db_name']
        target_db = client[db_name]						# get Database

        collaction_name = var_args['collaction_name']
        if (collaction_name not in target_db.list_collection_names()):
            target_db.create_collection(collaction_name)

        result = target_db[collaction_name].remove({})     # get Collection with find()
    
    return result

def update(**var_args):

    with MongoClient(db_address)  as client:		# your ip
        db_name = var_args['db_name']
        target_db = client[db_name]						# get Database

        collaction_name = var_args['collaction_name']
        if (collaction_name not in target_db.list_collection_names()):
            target_db.create_collection(collaction_name)

        result = target_db[collaction_name].update({})     # get Collection with find()
    
    return result
