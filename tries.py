class Contacts(object):
    __slots__ = ['partial_string_counter', 'sub_contacts']
    def __init__(self, sub_contacts= {}, partial_string_counter=0):
        self.partial_string_counter = partial_string_counter
        self.sub_contacts = {}

def do_add(node, contact):
    # takes node and the string to be added (contact)
    # checks if any of the 'node.sub_contacts' have the first char of the string
    currNode = node
    for char in list(contact):

        if (char not in currNode.sub_contacts.keys()):
            currNode.sub_contacts[char] = Contacts()

        currNode = currNode.sub_contacts[char]
        currNode.partial_string_counter += 1

def do_find(node, contact):
    # Looks through find_partial to see if the string matches
    # if string matches: sends the last node to find_count
    # if string doesn't match: returns 0
    lastNode = find_partial(node, contact)
    count = 0
    if (lastNode):
        count = lastNode.partial_string_counter
    return count

def find_partial(node, partial_string):
    # finds partial string by traversing the tree
    # returns the node at which the string becomes 0 
    # OR returns '0' if string is not matched

    currNode = node
    for char in list(partial_string):

        if (char in currNode.sub_contacts.keys()):
            currNode = currNode.sub_contacts[char]
        else:
            currNode = 0
            break        

    return currNode

# global contact list
contact_list_root = Contacts()
n = int(input().strip())
for a0 in range(n):
    op, contact = input().strip().split(' ')
    if (op == 'add'):
        do_add(contact_list_root, contact)
    if (op == 'find'):
        count = do_find(contact_list_root, contact)
        print (count)