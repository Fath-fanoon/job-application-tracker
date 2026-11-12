from job_application import JobApplication
from application_manager import ApplicationManager


manager = ApplicationManager()

while True:

    print("====Job Application Tracker====\n")
    print("1.Add Application")
    print("2.View Application")
    print("3.Search Application")
    print("4.Update Status")
    print("5.Delete Application")
    print("6.Filter by Status")
    print("7.Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        
        app_id = int(input("Enter Application ID: "))
        company = input("Enter Company Name: ")
        position = input("Enter Job Position: ")
        location = input("Enter Location: ")
        app_date = input("Enter Application Date: ")

        application = JobApplication(
            app_id, company, position, location, app_date
        )

        manager.add_application(application)

    elif choice == "2":
        manager.view_applications()
        
    elif choice == "3":
        company_name = input("Enter company name to search: ")
        manager.search_application(company_name)

    elif choice == "4":
        app_id = int(input("Enter Application ID: "))
        new_status = input("Enter new status: ")

        manager.update_application_status(app_id, new_status)

    elif choice == "5":
        app_id = int(input("Enter Application ID to delete: "))
        manager.delete_application(app_id)

    elif choice == "6":
        status = input("Enter status to filter: ")
        manager.filter_bystatus(status)

    elif choice == "7":
        print("Thank you for using Job Application Tracker!")
        break
