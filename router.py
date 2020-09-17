from flask import Flask , request, jsonify
import json
from controller import store_user_goal



app = Flask(__name__)


# input -> None
# output -. #list of dictionary->  [{"title": <string> , "description": <string>, "image_url": <url>, "type": <string>}]

# @app.route("/list_categories", )



# input -> category<string>
# @app.route("list_goals/<category>")
# output -> {"success": true , "data": [{"category": <string>, "goal_name": <string>, "description": <string>, "type": <string>, "order": <int>}]}



# input -> category<user>
# @app.route("list_goals/<user>")
# output -> {"success": true,  "data" : [{"category": <string>, "goal_name": <string>, "description": <string>, "type": <string>, "order": <int>}]}




# input -> {user_id: <string>, goal_id: <string>}
@app.route("store_goal/<user>", methods = ["POST", "PUT"]) # POST OR PUT.
def store_goal():
    data = json.loads(request.data)
    if not data:
        return {"success": False, "msg": "PLease provide valid data"}

    result = store_user_goal(data)

    return jsonify(result)
    
    
    
    
    


output -> {"success": true, "message": "stored_successfully"}



input -> 
