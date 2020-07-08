  def create_actor_file( actor_data ):
    import json
    import os
    filename = actor_data["name"] + '_data.json'
    os.chdir('actors_data')
    with open(filename,"w") as f:
      f.write(json.dumps( actor_data ))
