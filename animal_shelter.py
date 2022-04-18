from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self,username,password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://localhost:46776') #start wiht no auth
        #self.client = MongoClient('mongodb://%s:%s@localhost:46776/?authMechanism=DEFAULT&authSource=AAC'%(admin, admin))
        self.database = self.client['AAC']

# Method to implement the Create in CRUD
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data)  # data should be dictionary
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            return False
        
# Method to implement the Read (one) in CRUD 
    def read(self,data):
        return self.database.animals.find_one(data) #only returns one document as a python dictionary

# Method to implement the Read (all) in CRUD
    def read_all(self,data):
        cursor = self.database.animals.find(data,{'_id':False}) #a cursor which points to a list of results
        return cursor
        
# Method to implement the Update in CRUD
    def upd_one(self,data, new_data):
        if data is not None:
            updData = self.database.animals.update(data,{"$set":new_data})
            return True
        else:
            return False
        
# Method to implement the Delete (one) in CRUD
    def del_one(self,data):
        if data is not None:
            result = self.database.animals.find_one(data) # store data to be deleted in result
            self.database.animals.delete_one(data)  # data should be dictionary
            return result
        else:
            raise Exception("Nothing to delete, because data parameter is empty")
            return False
       
 # Method to implement the Delete (all) in CRUD
 #   def del_all(self,data):
 #       if data is not None:
 #           self.database.animals.delete_many(data)  # data should be dictionary
 #           return True
 #       else:
 #           raise Exception("Nothing to delete, because data parameter is empty")
 #           return False
