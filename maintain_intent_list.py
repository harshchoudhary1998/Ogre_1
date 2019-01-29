"""
Steps:
1. Download intent_list.csv and store in intent_list
2. Download recent_search.csv and store in recent_search
3. all the categories in the recent_search are to be moved to intent_list with a value = 0,<NO REPETITION>
4. Clear data of recent_search.csv.
5. Download noti_action.csv and store in noti_action
6. for every category in noti_action
    --> if action is "YES" -> value of this category in intent_list -> +1 <but always less than 1>
    -->
"""
