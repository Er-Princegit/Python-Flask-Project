import csv

bugs = []
BUGS_FILE = 'bugs.csv'

def load_bugs():
    try:
        with open(BUGS_FILE, 'r', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['priority'] = int(row['priority'])
                row['id'] = int(row['id'])
                bugs.append(row)
    except FileNotFoundError:
        pass

def save_bugs():
    with open(BUGS_FILE, 'w', newline='') as f:
        fieldnames = ['id', 'title', 'desc', 'priority', 'status', 'reportedby']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for b in bugs:
            writer.writerow({
                'id': b['id'], 'title': b['title'], 'desc': b['desc'],
                'priority': b['priority'], 'status': b['status'], 'reportedby': b['reportedby']
            })

def report_bug(username):
    print("--- Report Bug ---")
    title = input("Title: ").strip().title()
    desc = input("Description: ").strip()
    while True:
        try:
            priority = int(input("Priority (1-5): "))
            if 1 <= priority <= 5:
                break
            else:
                print("Priority must be 1 to 5.")
        except:
            print("Invalid input.")
    bug_id = max([b['id'] for b in bugs], default=0) + 1
    bug = {
        'id': bug_id,
        'title': title,
        'desc': desc,
        'priority': priority,
        'status': 'New',
        'reportedby': username,
    }
    bugs.append(bug)
    print(f"Bug {bug_id} reported! Status: New.")

def view_my_bugs(username):
    print("--- My Bugs ---")
    found = False
    for b in bugs:
        if b['reportedby'] == username and b['status'] != 'Resolved':
            print(f"ID: {b['id']}, Title: {b['title']}, Priority: {b['priority']}, Status: {b['status']}")
            found = True
    if not found:
        print("No open bugs reported by you.")

def add_comment():
    print("--- Add Comment (simplified, not persistent after restart) ---")
    bug_id = int(input("Bug ID: "))
    comment = input("Comment: ").strip()
    for b in bugs:
        if b['id'] == bug_id:
            if 'comments' not in b:
                b['comments'] = []
            b['comments'].append(comment)
            print("Comment added.")
            return
    print("Bug not found.")

def tester_menu(username):
    while True:
        print("--- Tester Menu ---")
        print("1. Report Bug 2.⁠ ⁠View My Bugs 3.⁠ ⁠Add Comment 4.⁠ ⁠Save & Exit")
        choice = input("Choice: ")
        if choice == '1':
            report_bug(username)
        elif choice == '2':
            view_my_bugs(username)
        elif choice == '3':
            add_comment()
        elif choice == '4':
            save_bugs()
            print("Saved. Exiting.")
            break
        else:
            print("Invalid choice.")

# Main entry
if __name__ == "__main__":

    load_bugs()
    username = input("Enter your Tester username: ")
    tester_menu(username)
