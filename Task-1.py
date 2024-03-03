class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks to display.")
        else:
            print("===== To-Do List =====")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
            print("=======================")

    def remove_task(self, task_number):
        try:
            task_index = int(task_number) - 1
            removed_task = self.tasks.pop(task_index)
            print(f"Task '{removed_task}' removed successfully!")
        except (IndexError, ValueError):
            print("Invalid task number.")

def main():
    todo_list = TodoList()

    while True:
        print("\nCommands:")
        print("- To add a task: add <task>")
        print("- To view tasks: view")
        print("- To remove a task: remove <task number>")
        print("- To quit: quit")

        user_input = input("Enter command: ").strip().split(maxsplit=1)

        if user_input[0] == "add":
            if len(user_input) > 1:
                todo_list.add_task(user_input[1])
            else:
                print("Please provide a task description.")
        elif user_input[0] == "view":
            todo_list.view_tasks()
        elif user_input[0] == "remove":
            if len(user_input) > 1:
                todo_list.remove_task(user_input[1])
            else:
                print("Please provide the task number to remove.")
        elif user_input[0] == "quit":
            print("Exiting...")
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
          
