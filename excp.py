class InvalidAgeError(Exception):
    pass

def set(age):
    if age<18:
        raise InvalidAgeError("Age can't be less than 18")
    
    print(f"You are eligible for voting")
    
try:
    set(41  )
except InvalidAgeError as e:
    print(e)
    