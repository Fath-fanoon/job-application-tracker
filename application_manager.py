from job_application import JobApplication

class ApplicationManager:

    def __init__(self):
        self.applications = []

#to add application

    def add_application(self,application):
        self.applications.append(application)

#to view all applications

    def view_applications(self):
        if not self.applications:
            print("You haven't applied to any jobs.")
        else:
            for i in self.applications:
                i.display_details()


#to search job applications
    def search_application(self,company_name):
        found = False
        for i in self.applications:
            if i.company.lower() == company_name.lower():
                i.display_details()
                found = True
        if not found:
            print("No match found!")


#delete applications
    def delete_application(self,app_id):

        found = False

        for i in self.applications:
            if i.app_id == app_id:
                self.applications.remove(i)
                found=True
                print("Application deleted successfully.")
                break

        if not found:
            print("Application not found!")

#filter applications by status:

    def filter_bystatus(self,status):
        found = False
        for i in self.applications:
            
            if i.status.lower() == status.lower():
                i.display_details()
                found = True

        if not found:
            print("No applications under this status.")

    # Update application status
    def update_application_status(self, app_id, new_status):
        found = False

        for i in self.applications:
            if i.app_id == app_id:
                i.update_status(new_status)
                found = True
                print("Status updated successfully!")
                break

        if not found:
            print("Application not found!")