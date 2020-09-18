from models import UserGoals, Goals
import datetime


# age - 10
# gender - M
def get_goals(user_id, age , gender):
    # filter_by
    ret_res = []
    
    for each in CategoryEligibilty.objects():
        each =  each.to_mongo().to_dict()
        criteria = each["criteria"]
        if "gt" in criteria.get("age", {}) :
                if age > criteria["age"]["gt"]:
                    categ = Categories.objects(title = each["category"]).first().to_mongo.to_dict()
                    ret_res.append(categ)



   cat_names = map(lambda ele: ele["title"], ret_res)
   goals = list(Goals.objects(category__in= cat_names))


   return {"categories": ret_res, "goals": goals}
       
                    
                    


       
            
    
    




def store_user_goal(data):
    user_id = data["user_id"]
    goal = data["goal_name"]

    goal_obj = Goal.objects(goal_name=goal).first()
    if not goal_obj:
        return {"success": False, "msg": "Goal is Invalid"}

    # check for user present later.
    
    user_goals = UserGoals.objects(user_id = user_id, goal=goal).first()
    if not user_goals:
        user_goals = UserGoals(user_id = user_id, goal=goal)

    state = getattr(user_goals, state)
    if  state == "active" or state == None :
        if user_goals.type == "action_x_times":
            user_goals.count_times = user_goals.count_times + 1
            if user_goals.count_times >=  goal_obj.total_days:
                user_goals.state = "completed"

        else:
            user_goals.state = "active"
            if (user_goals.updated_at - datetime.datetime.utcnow()).hours > 24:
                user_goals.state = "expired"
            
    user_goals.updated_at = datetime.datetime.utcnow()
    user_goals.save()

    return {"success": True}

    


    
    
