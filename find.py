from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

client = MongoClient(os.environ.get('URI'))
db = client[os.environ.get('DB')]
collection = db[os.environ.get('COLLECTION')]

def write_query_results(pipeline, header, file_name):
    results = list(collection.aggregate(pipeline))
    
    with open(file_name, "a") as f:
        f.write(header + "\n")
        for result in results:
            day = result["_id"]["day"]
            time = result["_id"]["time"]
            count = result["count"]
            f.write(f"   Day: {day:<10} | Time: {time:<10} | Count: {count}\n")
        f.write("=======================================================================================================\n")

def write_creative_results(pipeline, header, file_name):
    results = list(collection.aggregate(pipeline))
    result = results[0] if results else {}

    with open(file_name, "a") as f:
        f.write(header + "\n")
        for key, value in result.items():
            f.write(f"   Sub-category: {key:<15} | Total Time: {value} hours\n")
        f.write("=======================================================================================================\n")

def write_time_results(pipeline, header, file_name):
    results = list(collection.aggregate(pipeline))
    
    with open(file_name, "a") as f:
        f.write(header + "\n")
        for result in results:
            day = result["_id"]
            work_time = result["work_time"]
            personal_time = result["personal_time"]
            f.write(f"   Day: {day:<10} | Work Time: {work_time} hours | Personal Time: {personal_time} hours\n")
        f.write("=======================================================================================================\n")

def write_participant_results(pipeline, header, file_name):
    results = list(collection.aggregate(pipeline))
    
    with open(file_name, "a") as f:
        f.write(header + "\n")
        for result in results:
            participant = result["_id"]
            hours = result["total_hours"]
            f.write(f"   Participant: {participant:<5} | Total Hours: {hours} hours\n")
        f.write("=======================================================================================================\n")

def write_meeting_comparison_results(pipeline, header, file_name):
    results = list(collection.aggregate(pipeline))
    
    with open(file_name, "a") as f:
        f.write(header + "\n")
        for result in results:
            role = result["_id"]
            total_meeting_time = result["total_meeting_time"]
            f.write(f"   Role: {role:<10} | Total Meeting Time: {total_meeting_time} hours\n")
        f.write("=======================================================================================================\n")

def write_collab_time_results(pipeline, header, file_name):
    results = list(collection.aggregate(pipeline))
    
    with open(file_name, "a") as f:
        f.write(header + "\n")
        for result in results:
            field = result["_id"]
            total_collab_time = result["total_collab_time"]
            f.write(f"   Field: {field:<10} | Total Collaborative Time: {total_collab_time} hours\n")
        f.write("=======================================================================================================\n")

def write_manager_work_results(pipeline, header, file_name):
    results = list(collection.aggregate(pipeline))
    
    with open(file_name, "a") as f:
        f.write(header + "\n")
        for result in results:
            manager = result["_id"]
            hr_work_time = result["total_hr_work_time"]
            product_work_time = result["total_product_work_time"]
            f.write(f"   Manager: {manager:<10} | HR Work Time: {hr_work_time} hours | Product/Delivery Work Time: {product_work_time} hours\n")
        f.write("=======================================================================================================\n")

def write_developer_work_results(pipeline, header, file_name):
    results = list(collection.aggregate(pipeline))
    
    with open(file_name, "a") as f:
        f.write(header + "\n")
        for result in results:
            developer = result["_id"]
            coding_time = result["total_coding_time"]
            other_work_time = result["total_other_work_time"]
            f.write(f"   Developer: {developer:<10} | Coding Time: {coding_time} hours | Other Work Time: {other_work_time} hours\n")
        f.write("=======================================================================================================\n")

def write_role_meeting_results(pipeline, header, file_name):
    results = list(collection.aggregate(pipeline))
    
    with open(file_name, "a") as f:
        f.write(header + "\n")
        for result in results:
            role = result["_id"]
            meeting_time = result["total_meeting_time"]
            convo_time = result["total_convo_time"]
            f.write(f"   Role: {role:<15} | Meeting Time: {meeting_time} hours | Convo Time: {convo_time} hours\n")
        f.write("=======================================================================================================\n")

def write_role_work_results(pipeline, header, file_name):
    results = list(collection.aggregate(pipeline))
    
    with open(file_name, "a") as f:
        f.write(header + "\n")
        for result in results:
            role = result["_id"]
            coding_time = result["total_coding_time"]
            creative_time = result["total_creative_time"]
            f.write(f"   Role: {role:<15} | Coding Time: {coding_time} hours | Creative Time: {creative_time} hours\n")
        f.write("=======================================================================================================\n")

output_file = "query_results.txt"

one = [
    {
        "$group": {
            "_id": {"day": "$day", "time": "$time"},
            "count": {"$sum": {"$toInt": "$meeting (f)"}}
        }
    },
    {
        "$sort": {"count": -1}
    },
    {
        "$limit": 3
    }
]
write_query_results(one, "1. Top 3 popular days and times for meetings:", output_file)

two = [
    {
        "$group": {
            "_id": {"day": "$day", "time": "$time"},
            "count": {"$sum": {"$toInt": "$code"}}
        }
    },
    {
        "$sort": {"count": -1}
    },
    {
        "$limit": 3
    }
]
write_query_results(two, "2. Top 3 popular days and times for solo work (code):", output_file)

three = [
    {
        "$group": {
            "_id": {"day": "$day", "time": "$time"},
            "count": {"$sum": {"$toInt": "$lunch"}}
        }
    },
    {
        "$sort": {"count": -1}
    },
    {
        "$limit": 3
    }
]

write_query_results(three, "3. Top 3 popular days and times for lunch breaks:", output_file)

four = [
    {
        "$group": {
            "_id": {"day": "$day", "time": "$time"},
            "count": {"$sum": {"$toInt": "$creative"}}
        }
    },
    {
        "$sort": {"count": -1}
    },
    {
        "$limit": 3
    }
]
write_query_results(four, "4. Top 3 popular days and times for creativity:", output_file)

five = [
    {
        "$match": {"creative": {"$gt": "0"}} 
    },
    {
        "$group": {
            "_id": None,
            "total_slides": {"$sum": {"$toInt": "$slides"}},
            "total_design": {"$sum": {"$toInt": "$design"}},
            "total_hackathon": {"$sum": {"$toInt": "$hackathon"}},
            "total_architecture": {"$sum": {"$toInt": "$architecture"}},
            "total_feature": {"$sum": {"$toInt": "$feature"}},
            "total_data": {"$sum": {"$toInt": "$data"}},
            "total_tools": {"$sum": {"$toInt": "$tools"}},
            "total_effects": {"$sum": {"$toInt": "$effects"}},
            "total_plan": {"$sum": {"$toInt": "$plan"}},
            "total_learn": {"$sum": {"$toInt": "$learn"}},
            "total_replication": {"$sum": {"$toInt": "$replication"}}
        }
    },
    {
        "$project": {
            "_id": 0,
            "slides": "$total_slides",
            "design": "$total_design",
            "hackathon": "$total_hackathon",
            "architecture": "$total_architecture",
            "feature": "$total_feature",
            "data": "$total_data",
            "tools": "$total_tools",
            "effects": "$total_effects",
            "plan": "$total_plan",
            "learn": "$total_learn",
            "replication": "$total_replication"
        }
    }
]
write_creative_results(five, "5. Total time spent on creative work subcategories:", output_file)

six = [
    {
        "$match": {
            "day": {"$in": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]}
        }
    },
    {
        "$group": {
            "_id": "$day",
            "work_time": {
                "$sum": {
                    "$sum": [
                        {"$toInt": "$emails"},
                        {"$toInt": "$slack"},
                        {"$toInt": "$convo (i)"},
                        {"$toInt": "$meeting (f)"},
                        {"$toInt": "$collab"},
                        {"$toInt": "$1-1"},
                        {"$toInt": "$read"},
                        {"$toInt": "$document"},
                        {"$toInt": "$investigation"},
                        {"$toInt": "$prep/plan"},
                        {"$toInt": "$brainstorm"},
                        {"$toInt": "$infrastructure"},
                        {"$toInt": "$training"},
                        {"$toInt": "$demos"},
                        {"$toInt": "$proposal"},
                        {"$toInt": "$presentation"},
                        {"$toInt": "$feedback"},
                        {"$toInt": "$review"},
                        {"$toInt": "$code"},
                        {"$toInt": "$debug"},
                        {"$toInt": "$test"},
                        {"$toInt": "$triage"},
                        {"$toInt": "$prototype"},
                        {"$toInt": "$case work"},
                        {"$toInt": "$ML work"},
                        {"$toInt": "$design work"},
                        {"$toInt": "$event"},
                        {"$toInt": "$WFH"},
                        {"$toInt": "$office"},
                        {"$toInt": "$creative"}
                    ]
                }
            },
            "personal_time": {
                "$sum": {
                    "$sum": [
                        {"$toInt": "$breakfast"},
                        {"$toInt": "$lunch"},
                        {"$toInt": "$break"},
                        {"$toInt": "$pack up"},
                        {"$toInt": "$appt"},
                        {"$toInt": "$emergency"},
                        {"$toInt": "$life"},
                        {"$toInt": "$out"}
                    ]
                }
            }
        }
    },
    {
        "$project": {
            "_id": 1,
            "work_time": {"$round": [{"$divide": ["$work_time", 1]}, 2]}, 
            "personal_time": {"$round": [{"$divide": ["$personal_time", 1]}, 2]}
        }
    },
    {
        "$sort": {"_id": 1} 
    }
]
write_time_results(six, "6. Amount of time during the work-week actually doing 'work' vs personal stuff (and lunch):", output_file)

seven = [
    {
        "$group": {
            "_id": "$participant",
            "total_hours": {"$sum": {"$toInt": "$creative"}}
        }
    },
    {
        "$sort": {"total_hours": -1}
    },
    {
        "$limit": 3
    }
]

write_participant_results(seven, "7. Top 3 participants with the most hours in the 'creative' category:", output_file)

eight = [
     {
        "$group": {
            "_id": "$participant",
            "total_hours": {"$sum": {"$toInt": "$creative"}}
        }
    },
    {
        "$sort": {"total_hours": 1}
    },
    {
        "$limit": 3
    }
]

write_participant_results(eight, "8. Top 3 participants with the least hours in the 'creative' category:", output_file)

nine = [
    {
        "$match": {
            "$or": [
                {"managerial": "y"},
                {"technical": "y"}
            ]
        }
    },
    {
        "$project": {
            "participant": 1,
            "managerial": 1,
            "technical": 1,
            "meeting_time": {"$toInt": "$meeting (f)"}
        }
    },
    {
        "$group": {
            "_id": {
                "participant": "$participant",
                "managerial": "$managerial",
                "technical": "$technical"
            },
            "total_meeting_time": {"$sum": "$meeting_time"}
        }
    },
    {
        "$project": {
            "_id": {
                "$cond": [
                    {"$eq": ["$_id.managerial", "y"]},
                    "Manager",
                    "Technical"
                ]
            },
            "total_meeting_time": 1
        }
    },
    {
        "$group": {
            "_id": "$_id",
            "total_meeting_time": {"$sum": "$total_meeting_time"}
        }
    }
]

write_meeting_comparison_results(nine, "9. Managers vs Technical Roles: Total Meeting Time", output_file)

ten = [
    {
        "$match": {
            "collab": {"$gt": "0"} 
        }
    },
    {
        "$project": {
            "field": 1,
            "collab_time": {"$toInt": "$collab"}
        }
    },
    {
        "$group": {
            "_id": "$field",
            "total_collab_time": {"$sum": "$collab_time"}
        }
    },
    {
        "$sort": {"total_collab_time": -1}
    }
]

write_collab_time_results(ten, "10. Collaborative Work Time by Field", output_file)

eleven = [
    {
        "$match": {
            "managerial": "y"  # Ensures only managers are considered
        }
    },
    {
        "$project": {
            "participant": 1,
            "hr_work_time": {
                "$sum": [
                    {"$toInt": "$meeting (f)"},
                    {"$toInt": "$1-1"}
                ]
            },
            "product_work_time": {
                "$sum": [
                    {"$toInt": "$emails"},
                    {"$toInt": "$slack"},
                    {"$toInt": "$collab"},
                    {"$toInt": "$read"},
                    {"$toInt": "$document"},
                    {"$toInt": "$investigation"},
                    {"$toInt": "$prep/plan"},
                    {"$toInt": "$brainstorm"},
                    {"$toInt": "$infrastructure"},
                    {"$toInt": "$training"},
                    {"$toInt": "$demos"},
                    {"$toInt": "$proposal"},
                    {"$toInt": "$presentation"},
                    {"$toInt": "$feedback"},
                    {"$toInt": "$review"},
                    {"$toInt": "$code"},
                    {"$toInt": "$debug"},
                    {"$toInt": "$test"},
                    {"$toInt": "$triage"},
                    {"$toInt": "$prototype"},
                    {"$toInt": "$case work"},
                    {"$toInt": "$ML work"},
                    {"$toInt": "$design work"}
                ]
            }
        }
    },
    {
        "$group": {
            "_id": "$participant",
            "total_hr_work_time": {"$sum": "$hr_work_time"},
            "total_product_work_time": {"$sum": "$product_work_time"}
        }
    },
    {
        "$sort": {"_id": 1}
    }
]

write_manager_work_results(eleven, "11. HR Work vs Product/Delivery Work for Managers", output_file)

twelve = [
    {
        "$match": {
            "technical": "y",
            "managerial": "n"  
        }
    },
    {
        "$project": {
            "participant": 1,
            "coding_time": {"$toInt": "$code"},
            "other_work_time": {
                "$sum": [
                    {"$toInt": "$emails"},
                    {"$toInt": "$slack"},
                    {"$toInt": "$convo (i)"},
                    {"$toInt": "$meeting (f)"},
                    {"$toInt": "$collab"},
                    {"$toInt": "$1-1"},
                    {"$toInt": "$read"},
                    {"$toInt": "$document"},
                    {"$toInt": "$investigation"},
                    {"$toInt": "$prep/plan"},
                    {"$toInt": "$brainstorm"},
                    {"$toInt": "$infrastructure"},
                    {"$toInt": "$training"},
                    {"$toInt": "$demos"},
                    {"$toInt": "$proposal"},
                    {"$toInt": "$presentation"},
                    {"$toInt": "$feedback"},
                    {"$toInt": "$review"},
                    {"$toInt": "$debug"},
                    {"$toInt": "$test"},
                    {"$toInt": "$triage"},
                    {"$toInt": "$prototype"},
                    {"$toInt": "$case work"},
                    {"$toInt": "$ML work"},
                    {"$toInt": "$design work"}
                ]
            }
        }
    },
    {
        "$group": {
            "_id": "$participant",
            "total_coding_time": {"$sum": "$coding_time"},
            "total_other_work_time": {"$sum": "$other_work_time"}
        }
    },
    {
        "$sort": {"_id": 1}
    }
]

write_developer_work_results(twelve, "12. Coding vs Other Work for Developers", output_file)

thirteen = [
    {
        "$project": {
            "participant": 1,
            "managerial": {"$cond": [{"$eq": ["$managerial", "y"]}, 1, 0]},
            "technical": {"$cond": [{"$eq": ["$technical", "y"]}, 1, 0]},
            "product_focus": {"$cond": [{"$eq": ["$product focus", "y"]}, 1, 0]},
            "meeting_time": {"$toInt": "$meeting (f)"},
            "convo_time": {"$toInt": "$convo (i)"},
        }
    },
    {
        "$facet": {
            "managerial": [
                {"$match": {"managerial": 1}},
                {
                    "$group": {
                        "_id": "Managerial",
                        "total_meeting_time": {"$sum": "$meeting_time"},
                        "total_convo_time": {"$sum": "$convo_time"}
                    }
                }
            ],
            "technical": [
                {"$match": {"technical": 1}},
                {
                    "$group": {
                        "_id": "Technical",
                        "total_meeting_time": {"$sum": "$meeting_time"},
                        "total_convo_time": {"$sum": "$convo_time"}
                    }
                }
            ],
            "product_focus": [
                {"$match": {"product_focus": 1}},
                {
                    "$group": {
                        "_id": "Product Focus",
                        "total_meeting_time": {"$sum": "$meeting_time"},
                        "total_convo_time": {"$sum": "$convo_time"}
                    }
                }
            ]
        }
    },
    {
        "$project": {
            "results": {"$setUnion": ["$managerial", "$technical", "$product_focus"]}
        }
    },
    {
        "$unwind": "$results"
    },
    {
        "$replaceRoot": {
            "newRoot": "$results"
        }
    }
]

write_role_meeting_results(thirteen, "13. Time Spent in Meetings vs Convo by Role", output_file)

fourteen = [
    {
        "$project": {
            "participant": 1,
            "managerial": {"$cond": [{"$eq": ["$managerial", "y"]}, 1, 0]},
            "technical": {"$cond": [{"$eq": ["$technical", "y"]}, 1, 0]},
            "product_focus": {"$cond": [{"$eq": ["$product focus", "y"]}, 1, 0]},
            "coding_time": {"$toInt": "$code"},
            "creative_time": {"$toInt": "$creative"}
        }
    },
    {
        "$facet": {
            "managerial": [
                {"$match": {"managerial": 1}},
                {
                    "$group": {
                        "_id": "Managerial",
                        "total_creative_time": {"$sum": "$creative_time"},
                        "total_coding_time": {"$sum": "$coding_time"}
                    }
                }
            ],
            "technical": [
                {"$match": {"technical": 1}},
                {
                    "$group": {
                        "_id": "Technical",
                        "total_creative_time": {"$sum": "$creative_time"},
                        "total_coding_time": {"$sum": "$coding_time"}
                    }
                }
            ],
            "product_focus": [
                {"$match": {"product_focus": 1}},
                {
                    "$group": {
                        "_id": "Product Focus",
                        "total_creative_time": {"$sum": "$creative_time"},
                        "total_coding_time": {"$sum": "$coding_time"}
                    }
                }
            ]
        }
    },
    {
        "$project": {
            "results": {"$setUnion": ["$managerial", "$technical", "$product_focus"]}
        }
    },
    {
        "$unwind": "$results"
    },
    {
        "$replaceRoot": {
            "newRoot": "$results"
        }
    }
]

write_role_work_results(fourteen, "14. Time Spent in Coding vs Being Creative by Role", output_file)

print(f"Query results have been written to '{output_file}'")
