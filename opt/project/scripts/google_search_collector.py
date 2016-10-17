import json
import datetime

word_to_search = "pentaho"

from googleapiclient.discovery import build

def main():
  service = build("customsearch", "v1",
            developerKey="PUT_HERE")

  res = service.cse().list(
      q=word_to_search, #Search words
      cx='PUT_HERE',  #CSE Key
      lr='lang_pt', #Search language
    ).execute()


  filename = "/opt/file_mgmt/to_process/output_google_search_" + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ".json"

  print (filename)

  # with open('output_pdi.json', 'w') as outfile:
  with open(filename, 'w') as outfile:
    json.dump(res, outfile)

main()
