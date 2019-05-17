import facebook
import codes 
# defined cfs with page_id and access_token
# in separate file
# cfg = {
#     "page_id"      : "VALUE",  # Step 1
#     "access_token" : "VALUE"   # Step 3
#     }

def main(message):
  # Fill in the values noted in previous steps here

  api = get_api(cfg)
  msg = message
  status = api.put_wall_post(msg)
  things = api.get_object()

def get_api(cfg):
  graph = facebook.GraphAPI(cfg['access_token'])
  return graph

if __name__ == "__main__":
  main()