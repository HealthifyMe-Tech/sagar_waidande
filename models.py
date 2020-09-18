from mongoengine import *
connect("test")


class User(DynamicDocument):
    user_id = StringField(unique = True)
    name = StringField(required = True) 
    email = StringField(required = True)
    phone = StringField()

    # user_id = index, email = index 




class Categories(DynamicDocument):
    title = StringField(unique = True)
    desc = StringField()
    image = StringField()
    # some goals to complete to get to next category.
    unlock_criteria = ListField()  # List of goals to complete.
    type = StringField() # Locked or Unlocked.

    # index type 
    

class CategoryEligibilty(DynamicDocument):
    category = StringField() # foreign key
    criteria = DictField() #keys can be lt eq gt.  Eg- {"age": {"gt": 18}}
    
    # composite key -> category, criteria 
    



class Goals(DynamicDocument):
    category = StringField() # foreign key
    goal_name = StringField()
    description = StringField(unique=True)
    type =  StringField() # can be "click" or "action_x_times"
    total_days = IntField(required=True, default= 0)  # action_x_times action count.
    order = IntField(required=True)

    # indexes
    # composite key -> category, goal_name
    


class UserGoals(DynamicDocument):
    user_id =  StringField()    # foreign key
    goal = StringField() # foreign_key
    state = StringField()   # can be "active" , "completed", "expired".
    start_date = DateTimeField(default=datetime.datetime.utcnow)
    updated_date = DateTimeField(default=datetime.datetime.utcnow)
    count_times = IntField(default= 0)


    # composite_key -> user_id, goal.
    # user_id.    
    
