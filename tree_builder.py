class EmployeeNode:
    '''
    A class to represent a node in the binary tree.
    Attributes:
        name (str): The name of the employee.
        left (EmployeeNode): The left child node, representing the left subordinate.
        right (EmployeeNode): The right child node, representing the right subordinate.
    '''

    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

class TeamTree:
    '''
    A class to represent a binary tree for managing a team structure.
    Attributes:
        root (EmployeeNode): The root node of the tree, representing the team lead.
    Methods:
        insert(manager_name, employee_name, side, current_node=None): Inserts a new employee under the specified manager.
        print_tree(node=None, level=0): Prints the tree structure starting from the given node.
    '''
    
    def __init__(self):
        self.root = None

    def insert(self, manager_name, employee_name, side, current_node=None):
        inserted = False
        if current_node == None:
            current_node = self.root
            if current_node == None:
                print('Company directory is empty.')
                return

        if current_node.name == manager_name:
            if side == 'right' and current_node.right == None:
                current_node.right = EmployeeNode(employee_name)
                return
            elif side == 'left' and current_node.left == None:
                current_node.left = EmployeeNode(employee_name)
                return
            else:
                print(f'The {side} side is not available for {manager_name}.')
                return

        if current_node.left:
            self.insert(manager_name, employee_name, side, current_node.left)
            return
        if current_node.right:
            self.insert(manager_name, employee_name, side, current_node.right)
            return
        
        print('Manager does not exist in directory.')

    def print_tree(self, node=None, level=0):
        if node == None:
            if level == 0:
                node = self.root
                if node == None:
                    print('Company directory is empty.')
                    return
            else:
                return
                
        print("    " * level + f'- {node.name}')

        self.print_tree(node.left, level + 1)
        self.print_tree(node.right, level + 1)

# CLI functionality
def company_directory():
    tree = TeamTree()

    while True:
        print("\n📋 Team Management Menu")
        print("1. Add Team Lead (root)")
        print("2. Add Employee")
        print("3. Print Team Structure")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            if tree.root:
                print("⚠️ Team lead already exists.")
            else:
                name = input("Enter team lead's name: ")
                tree.root = EmployeeNode(name)
                print(f"✅ {name} added as the team lead.")

        elif choice == "2":
            manager = input("Enter the manager's name: ")
            employee = input("Enter the new employee's name: ")
            side = input("Should this employee be on the LEFT or RIGHT of the manager? ")
            side = side.lower()
            tree.insert(manager, employee, side)

        elif choice == "3":
            print("\n🌳  Current Team Structure:")
            tree.print_tree()

        elif choice == "4":
            print("Good Bye!")
            break
        else:
            print("❌ Invalid option. Try again.")