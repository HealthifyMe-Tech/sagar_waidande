from models import UserGoals
import datetime




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


    if user_goals.type == "action_x_times":
        user_goals.count_times = user_goals.count_times + 1
        if user_goals.count_times >=  goal_obj.total_times:
            user_goals.state = "completed"

        else:
            user_goals.state = "active"
            if (user_goals.updated_at - user_goals.updated_at).hours > 24:
                user_goals.state = "expired"

            
            

        




    user_goals.updated_at = datetime.datetime.utcnow()

    

    


    
    
