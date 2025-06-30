# Question 2: Graph

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def addVertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def addEdge(self, from_vertex, to_vertex):
        if from_vertex in self.adjacency_list and to_vertex in self.adjacency_list:
            if to_vertex not in self.adjacency_list[from_vertex]:
                self.adjacency_list[from_vertex].append(to_vertex)

    def listOutgoingAdjacentVertex(self, vertex):
        return self.adjacency_list.get(vertex, [])

    def listIncomingAdjacentVertex(self, vertex):
        followers = []
        for user, following in self.adjacency_list.items():
            if vertex in following:
                followers.append(user)
        return followers

class Person:
    def __init__(self, username, name, gender, bio, is_private=False):
        self.username = username
        self.name = name
        self.gender = gender
        self.bio = bio
        self.is_private = is_private

    def getProfile(self):
        if self.is_private:
            return f"Name: {self.name}\n(Private Profile)"
        else:
            return f"Name: {self.name}\nGender: {self.gender}\nBio: {self.bio}"

people = {
    "Vigneesh": Person("Vigneesh", "Vigneesh Gopal", "Male", " Loves Advance Algo Subject", False),
    "Niyas": Person("Niyas", "Muhammad Niyas", "Male", "Loves Homework", True),
    "Joel": Person("Joel", "Joel Teh", "Male", "Loves Badminton", False),
    "Sharvin": Person("Sharvin", "Sharvin Chow", "Male", "Loves Gaming", False),
    "Sandra": Person("Sandra", "Sandra Roleda", "Female", "Loves Drawing", True),
}

social_graph = Graph()
for username in people:
    social_graph.addVertex(username)

# Sample Follow Relationships
social_graph.addEdge("Vigneesh", "Niyas")
social_graph.addEdge("Vigneesh", "Joel")
social_graph.addEdge("Niyas", "Joel")
social_graph.addEdge("Joel", "Sharvin")
social_graph.addEdge("Sharvin", "Vigneesh")
social_graph.addEdge("Sandra", "Niyas")

# Main
def menu():
    while True:
        print("\nSocial Media Graph Menu")
        print("1. LIST ALL USERS")
        print("2. VIEW A USER'S PROFILE")
        print("3. VIEW WHO A USER FOLLOWS")
        print("4. VIEW A USER'S FOLLOWERS")
        print("5. FOLLOW A USER")
        print("6. UNFOLLOW A USER")
        print("0. EXIT")
        choice = input("Enter a Number From List: ")

        if choice == "1":
            for personName in people:
                print(f"- {personName}")
        elif choice == "2":
            personName = input("Enter username: ")
            if personName in people:
                print(people[personName].getProfile())
            else:
                print("User not found.")
        elif choice == "3":
            personName = input("Enter username: ")
            follows = social_graph.listOutgoingAdjacentVertex(personName)
            print(f"{personName} follows: {', '.join(follows) if follows else 'No one'}")
        elif choice == "4":
            personName = input("Enter username: ")
            followers = social_graph.listIncomingAdjacentVertex(personName)
            print(f"{personName}'s followers: {', '.join(followers) if followers else 'No one'}")
        elif choice == "5":
            from_user = input("Who wants to follow? ")
            to_user = input("Who to follow? ")
            social_graph.addEdge(from_user, to_user)
            print(f"{from_user} now follows {to_user}.")
        elif choice == "6":
            from_user = input("Who wants to unfollow? ")
            to_user = input("Who to unfollow? ")
            if to_user in social_graph.adjacency_list.get(from_user, []):
                social_graph.adjacency_list[from_user].remove(to_user)
                print(f"{from_user} has unfollowed {to_user}.")
            else:
                print(f"{from_user} does not follow {to_user}.")
        elif choice == "0":
            print("Ended program")
            break
        else:
            print("Choice does not exist")

if __name__ == "__main__":
    menu()
