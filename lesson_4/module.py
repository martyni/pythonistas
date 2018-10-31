from datetime import datetime

def multiply_numbers(int1, int2):
    answer = None #hint you might want to just delete this line
    return answer

def join_strings(string1, string2):
    answer = None #hint you might want to just delete this line
    return answer

def age_in_years(day, month, year):
   birthday = datetime(day=day, month=month, year=year)
   todays_date = datetime.utcnow()
   difference = todays_date - birthday
   age_in_days = difference.days
   return age_in_days

if __name__ == "__main__":
   print multiply_numbers(4, 3)
   print join_strings("hi ", "how are you?")
   print age_in_years(13, 4, 1989)  
