from datetime import datetime

# Define colors for terminal output (Color coding)
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    RESET = '\033[0m'



def display_menu():
    """Displays the menu options to the user."""
    print("\nWelcome to the To-Do List App!")
    print("\nMenu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Quit")

def add_task(task_list):
    """Adds a task to the task list with 'Incomplete' status."""
    task_title = input("Enter the task title: ")
    task_list.append({'title': task_title, 'status': 'Incomplete'})
    print(f"Task '{task_title}' added successfully!")

def view_tasks(task_list):
    """Displays all tasks with their titles and statuses."""
    if not task_list:
        print("No tasks available.")
    else:
        for i, task in enumerate(task_list, start=1):
            print(f"{i}. {task['title']} - {task['status']}")

def mark_task_complete(task_list):
    """Marks a task as complete based on the user's choice."""
    try:
        task_number = int(input("Enter the task number to mark as complete: "))
        if task_number < 1 or task_number > len(task_list):
            raise ValueError("Invalid task number.")
        task_list[task_number - 1]['status'] = 'Complete'
        print(f"Task '{task_list[task_number - 1]['title']}' marked as complete.")
    except ValueError as e:
        print(f"Error: {e}")
    except IndexError:
        print("Error: Task number out of range.")
    else:
        print("Task marked as complete.")
    finally:
        print("Operation complete.")

def delete_task(task_list):
    """Deletes a task from the task list based on the user's choice."""
    try:
        task_number = int(input("Enter the task number to delete: "))
        if task_number < 1 or task_number > len(task_list):
            raise ValueError("Invalid task number.")
        deleted_task = task_list.pop(task_number - 1)
        print(f"Task '{deleted_task['title']}' deleted successfully.")
    except ValueError as e:
        print(f"Error: {e}")
    except IndexError:
        print("Error: Task number out of range.")
    else:
        print("Task deleted.")
    finally:
        print("Operation complete.")

def main():
    """Main function to run the To-Do List Application."""
    task_list = []

    while True:
        display_menu()
        choice = input("Select an option (1-5): ")

        try:
            if choice == '1':
                add_task(task_list)
            elif choice == '2':
                view_tasks(task_list)
            elif choice == '3':
                mark_task_complete(task_list)
            elif choice == '4':
                delete_task(task_list)
            elif choice == '5':
                print("Exiting the application. Goodbye!")
                break
            else:
                raise ValueError("Invalid choice, please select a valid option.")
        except ValueError as e:
            print(f"Error: {e}")
        else:
            print("Operation successful.")
        finally:
            print("Returning to the main menu.")

if __name__ == "__main__":
    main()
