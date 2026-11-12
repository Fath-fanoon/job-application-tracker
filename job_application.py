
class JobApplication:

    def __init__(self,app_id,company,position,location,app_date):
        self.app_id = app_id
        self.company = company
        self.position = position
        self.location = location
        self.app_date = app_date
        self.status = "Applied"

    def update_status(self,new_status):
        self.status = new_status

    def display_details(self):
        print("Application ID:", self.app_id)
        print("Company:",self.company)
        print("Position:",self.position)
        print("Location:",self.location)
        print("Application Date:", self.app_date)
        print("Status:",self.status)
