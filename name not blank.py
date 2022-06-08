# Fuctions go here

def not_blank(question):
      valid = False
  
      while not valid:
          response = input(question)
  
  # If name is not blank, program continues
      if response != "":
              return response
  
  # If name is blank, show error (& repeat loop)
      else:
        print("Sorry - this cant be blank, "
             "please enter your name")


# ********** Main Routine **********

# Set up ditcionaries / lists needed to hold data

# Ask user if they have used the program before & show instructions if necessary
