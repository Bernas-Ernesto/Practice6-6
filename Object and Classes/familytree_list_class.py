class FamilyTree:
    def __init__(self, name = "", relation = ""):
        self.name = name 
        self.relation = relation 

class Member:
    def __init__(self):
        self.family = []
    
    def add_family_member(self):
        name = input("Name: ")
        relation = input("Relation: ")
        add_family = FamilyTree(name = name, relation = relation)
        self.family.append(add_family)
    
    def show_family_tree(self):
        if self.family:
            print("\nFamily Members:")
            for member in self.family:
                print(f"{member.name} - {member.relation}")
        else:
            print("No family members found.")
    
family_tree = Member()

for i in range(3):
    family_tree.add_family_member()
    
family_tree.show_family_tree()