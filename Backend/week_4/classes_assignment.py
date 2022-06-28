class UserProfile:
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname

    def update_firstname_and_lastname(self,lastname_update,firstname_update):
            self.lastname = lastname_update
            self.firstname = firstname_update
            return 

    def list_of_fullnames(self):
        self.firstname.upper()
        print(f"{self.firstname.upper()}  {}")
        return 


    
