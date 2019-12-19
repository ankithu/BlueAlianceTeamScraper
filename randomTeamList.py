import requests
import json
import random
import csv
compCheckYear = "2020"
#[1,999],[1000,2287],[2330,4440],[4450,6248],[6300,7331],
teamRanges = [[6300,7331],[7400,7915]]
selectionCount = 25
selections = []
baseUrl = 'https://www.thebluealliance.com/api/v3/'
key = {"X-TBA-Auth-Key":"RHbM1E1LepvMNctmJZBxFw30DovOcdPONB5rMHMMtGvC4Omu7vyK2PM8HeEcOrkJ"}
for group in teamRanges:
	rangeSelectionCount = 0
	rangeSelections = []
	while rangeSelectionCount < selectionCount:
		selection = random.randint(group[0],group[1]+1)
		if selection not in rangeSelections:
			teamID = "frc"+str(selection)
			r = requests.get(baseUrl + 'team/'+teamID+'/events/'+compCheckYear, headers=key)
			if len(r.json()) != 0 and type(r.json()) is list:
				rangeSelections.append(selection)
				rangeSelectionCount += 1
				print("adding " + teamID + " to group")
	selections.append(rangeSelections)
with open("randomTeamData.csv","w+") as teamCSV:
    csvWriter = csv.writer(teamCSV,delimiter=',')
    csvWriter.writerows(selections)
	
	