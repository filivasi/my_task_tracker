import json
import os
FILE_PATH = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE_PATH):
        return[]
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return[]
def save_tasks(tasks):
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(tasks, f,ensure_ascii=False, indent=2)

def list_tasks(tasks):
    if not tasks:
        print("\n[!] Η λίστα είναι άδεια.")
    for task in tasks:
        status = "[✓]" if task["done"] else "[ ]"
        print(f"{task['id']}. {status} {task['title']}")

def add_task(tasks):
    title = input("\nΤίτλος εργασίας: ").strip()
    if not title:
        print("Ο Τίτλος εργασίας δεν μπορεί να είναι κενός.")
        return
    
    new_id = max([t["id"]for t in tasks], default=0) + 1
    tasks.append({"id": new_id, "title": title, "done": False})

    save_tasks(tasks)
    print(f"Η εργασία '{title}' αποθηκεύτηκε!")

def complete_tasks(tasks):
    list_tasks(tasks)
    if not tasks:
        return
    try: 
        task_id = int(input("\nΔώσε το ID της εργασίας προς ολοκλήρωση: "))
        for task in tasks:
            if task["id"] == task_id:
                task["done"] = True
                save_tasks(tasks)
                print(f"Η εργασία {task_id} σημειώθηκε ως ολοκληρωμένη")
                return
            print("Δεν βρέθηκε εργασία με αυτό το ID.")
    except ValueError:
        print("Παρακαλώ δώσε έγκυρο αριθμό.")

def delete_task(tasks):
    list_tasks(tasks)
    if not tasks:
        return
    try:
        task_id = int(input("\nΔώσε το ID της εργασίας προς διαγραφή: "))
        for i, task in enumerate(tasks):
            if task["id"] == task_id:
                removed = tasks.pop(i)
                save_tasks(tasks)
                print(f"Η εργασία '{removed['title']}' διαγράφηκε επιτυχώς!")
                return
        print("Δεν βρέθηκε εργασία με αυτό το ID.")
    except ValueError:
        print("Παρακαλώ δώσε έγκυρο αριθμό.")

def main():
    tasks = load_tasks()

    while True:
        print("\n=== TASK TRACKER ===")
        print("1. Προβολή εργασιών")
        print("2. Προσθήκη ερασίας")
        print("3. Ολοκλήρωση εργασίας")
        print("4. Διαγραφή εργασίας")
        print("5. Έξοδος")

        choice = input("Επίλεξε (1-5): ").strip()

        if choice == "1":
            list_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_tasks(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Αντίο!")
            break
        else:
            print("Λάθος επιλογή, προσπάθησε ξανά.")

if __name__ == "__main__":
    main()
