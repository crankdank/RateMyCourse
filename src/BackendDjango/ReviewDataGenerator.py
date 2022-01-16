import names
import random
import lorem
import json 
import datetime

f = open("demofile2.txt", "a")
dictionary_to_JSON = {}

for i in range(10):
    f_name = names.get_first_name()
    l_name = names.get_last_name()
    professor = "Dr. " + f_name + " " + l_name
    print(professor)
    f_name = f_name[0:random.randint(1,len(f_name))]
    max_length = 12
    max_length = max_length - len(f_name)
    l_name = l_name[0:max_length]    
    ccid = f_name.lower() + l_name.lower()
    print("FULL CCID: " + ccid)
    course_number = ["CMPUT174","CMPUT401"]
    chosen_course = course_number[random.randint(0,len(course_number)-1)]
    
    Seasons = ["FALL", "WINTER","SPRING","SUMMER"]
    SeasonNumber = ["19","20","21","22"]
    
    chosen_season = Seasons[random.randint(0,len(Seasons)-1)]   
    chosen_season_num = SeasonNumber[random.randint(0,len(Seasons)-1)] 
    chosen_season = chosen_season + chosen_season_num
    print(chosen_season)
    
    overall_rate = random.randint(1,5)
    difficulty = random.randint(1,5)
    usefulness = random.randint(1,5)
    workload = random.randint(1,5)
    interest = random.randint(1,5)
    comment = lorem.paragraph()
    print(comment)
    
    date = datetime.datetime.now()
    date = date.strftime("%Y-%m-%d")
    
    dictionary_to_JSON = { "professor": professor,
                           "semester": chosen_season,
                           "course_num": chosen_course,
                           "overall_rate": overall_rate,
                           "difficulty": difficulty,
                           "usefulness": usefulness,
                           "workload" : workload,
                           "interest": interest,
                           "comment": comment,
                           "ccid": ccid,
                           "date": date}
    # Serializing json  
    json_object = json.dumps(dictionary_to_JSON, indent = 4) 
    print(json_object)
    
    f.write(json_object)
    f.write("\n")

f.close()
    
    
    
    
    
    