import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
base_url = "https://www.digikala.com/"
credentials = {
    'user1': {"phone_number": "09306823848"},
    'user2': {"email": "mrmehrdad@rocketmail.com","password":"Mr.mehrdad94"},
    'invalid_users':[ {"email": "wrong@email.com", "password": "wrongpass"}]
    }
default_wait_time = 10