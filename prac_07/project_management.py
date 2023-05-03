import datetime
from project import Project

MENU = "\n(L)oad projects\n(S)ave projects\n(D)isplay projects\n(F)ilter projects by date\n(A)dd new project\n(" \
       "U)pdate project\n(Q)uit\n"


def main():
    filename = "projects.txt"
    projects = load_projects(filename)

    while True:
        print(MENU)
        choice = input(">>> ").lower()
        if choice == "l":
            filename = input("Enter filename to load projects from: ")
            projects = load_projects(filename)
        elif choice == "s":
            filename = input("Enter filename to save projects to: ")
            save_projects(filename, projects)
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            date_string = input("Show projects that start after date (dd/mm/yy): ")
            date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            filter_projects_by_date(projects, date)
        elif choice == "a":
            add_new_project
            add_new_project(projects)
        elif choice == "u":
            update_project(projects)
        elif choice == "q":
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid choice. Please try again.")


def load_projects(filename):
    projects = []
    with open(filename, "r") as file:
        file.readline()
        for line in file:
            name, start_date, priority, cost_estimate, completion = line.strip().split("\t")
            start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
            projects.append(Project(name, start_date, int(priority), float(cost_estimate), int(completion)))
    return projects


def save_projects(filename, projects):
    with open(filename, "w") as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(
                f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.cost_estimate}\t{project.completion}\n")


def display_projects(projects):
    incomplete_projects = sorted([project for project in projects if project.completion < 100],
                                 key=lambda p: p.priority)
    completed_projects = sorted([project for project in projects if project.completion == 100],
                                key=lambda p: p.priority)

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(project)

    print("\nCompleted projects:")
    for project in completed_projects:
        print(project)


def filter_projects_by_date(projects, date):
    filtered_projects = sorted([project for project in projects if project.start_date > date],
                               key=lambda p: p.start_date)
    for project in filtered_projects:
        print(project)


def add_new_project(projects):
    print("Lets add a new project")
    name = input("Name: ")
    start_date = datetime.datetime.strptime(input("Start date (dd/mm/yy): "), "%d/%m/%Y").date()
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, cost_estimate, completion))


def update_project(projects):
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    project_choice = int(input("Project choice: "))
    project = projects[project_choice]
    print(project)
    new_completion = input("New Percentage: ")
    new_priority = input("New Priority: ")
    if new_completion:
        project.completion = int(new_completion)
    if new_priority:
        project.priority = int(new_priority)


main()
