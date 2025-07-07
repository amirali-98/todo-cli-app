class Task:
    def __init__(self, id, title, description=""):
        self.id = id
        self.title = title
        self.description = description
        self.done = False

    def mark_done(self):
        self.done = True


class TaskManager:
    def __init__(self):
        self.tasks = []

    def start_menu(self):
        print("\n")
        print("="*50)
        print("📝  Welcome to Your Personal Task Manager!")
        print("-"*50)
        print("Manage your daily tasks right from your terminal.")
        print("You can add, view, complete, and remove your tasks.")
        print()
        print("📌 Commands:")
        print("1. Show tasks")
        print("2. Add new task")
        print("3. Mark task as done")
        print("4. Edit task")
        print("5. Delete task")
        print("6. Exit")
        print("="*50)

    def show_tasks(self):
        if not self.tasks:
            print("\n🕳️ You have no tasks yet.")
            return

        print("\n📝 Your Tasks:")
        print("=" * 40)

        for index, task in enumerate(self.tasks, 1):
            status = "✅ Done" if task.done else "❌ Not done"
            print(f"{index}. {task.title} - {status}")

            if task.description:
                print(f"   🗒️ {task.description}")

            print("="*40)

    def add_task(self):
        print("\n➕ Let's add a new task!")
        title = input("📌 Enter task title: ").strip()

        if not title:
            print("⚠️ Title cannot be empty. Task not added.")
            return

        description = input(
            "📝 Optional - Enter a short description (or leave blank): ").strip()

        new_task = Task(len(self.tasks) + 1, title, description)
        self.tasks.append(new_task)

        print(f"✅ Task '{title}' added successfully!")

    def mark_done(self):
        if not self.tasks:
            print("\n🕳️ You have no tasks yet.")
            return

        self.show_tasks()

        item = int(input("✔️ Enter the task number to mark as done: "))

        if 1 <= item <= len(self.tasks):
            task = self.tasks[item - 1]

            if task.done:
                print(f"⚠️ Task '{task.title}' is already marked as done.")
            else:
                task.mark_done()
                print(f"✅ Task '{task.title}' marked as done!")
        else:
            print("❌ Invalid task number.")

    def remove_task(self):
        if not self.tasks:
            print("\n🕳️ You have no tasks yet.")
            return

        self.show_tasks()

        item = int(input("❌ Enter the task number to remove: "))

        if 1 <= item <= len(self.tasks):
            task = self.tasks[item - 1]

            removed_task = self.tasks.pop(item - 1)
            print(f"✅ Task '{removed_task.title}' removed successfully.")
        else:
            print("❌ Invalid task number.")

    def edit_task(self):
        if not self.tasks:
            print("\n🕳️ You have no tasks yet.")
            return

        self.show_tasks()

        item = int(input("✏️ Enter the task number to edit: "))

        if 1 <= item <= len(self.tasks):
            task = self.tasks[item - 1]
            new_title = input(
                "📝 New title (or press Enter to keep current): ").strip()
            new_description = input(
                "🗒️ New description (or press Enter to keep current): ").strip()

            if new_title:
                task.title = new_title
            if new_description:
                task.description = new_description

            print(f"✅ Task '{task.title}' updated successfully.")
        else:
            print("❌ Invalid task number.")


task_manager = TaskManager()

while True:
    task_manager.start_menu()
    command = input("Enter your choice (1-6): ")

    if command == "1":
        task_manager.show_tasks()
    elif command == "2":
        task_manager.add_task()
    elif command == "3":
        task_manager.mark_done()
    elif command == "4":
        task_manager.edit_task()
    elif command == "5":
        task_manager.remove_task()
    elif command == "6":
        break
