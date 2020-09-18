from models import UserGoals, Goals
from controller import get_goals , store_user_goals

class UnitTests:
    def __init__(self):
        return
    
    
    def test_get_goals(self, user_id, age):
        """
        TEST get categories and goals based on given criteria  functionality. 
        """
        
        # get all categories above given age
        all_categories = CategoryEligibilty.objects(criteria.age.gt__gte = age).serialize()
        cat_names =  map(lambda ele , ele["category"])
        goal_names = list(Goals.objects(category__in=cat_names).include("goal_name"))

        cat_goals = get_goals(user_id, age , gender)

        fun_categories = [each["title"] for  each in cat_goals["categories"]]
        fun_goals = [category["goal_name"] for  each in cat_goals["goals"]]

        assert set(fun_categories) == set(cat_names)
        assert set(fun_goals) == set(goal_names)
 




    def test_store_user_goal(self, user_id, goal_id):
        """
        TEST store goal for a user functionality 
        """
        # can be tested for both creation and updation.
        inp_data = {"user_id": user_id, "goal_id": goal_id} 
        assert store_user_goal(inp_data) == {"sucesss": True}
        goal_obj = Goal.objects(goal_name=goal_id).first()
        user_goal = UserGoals(user_id=user_id,  goal_id=goal_id).objects().first()

        assert  user_goal != None
        if (user_goals.updated_at - datetime.datetime.utcnow()).hours > 24:
            assert user_goal_res.state == "expired"


        elif user_goals.count_times >=  goal_obj.total_days:
            assert user_goals.state == "completed"


        else:
            assert user_goals.state == "active"


        
        

        

        
