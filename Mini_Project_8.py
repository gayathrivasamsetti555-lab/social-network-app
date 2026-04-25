from collections import deque

class SocialNetwork:
    def __init__(self):
        self.users = set()
        self.graph = {}  # user -> set of follows

    def add_user(self, user):
        self.users.add(user)
        self.graph[user] = set()

    def follow(self, u, v):
        if u in self.users and v in self.users:
            self.graph[u].add(v)

    def mutual_friends(self, u, v):
        return self.graph[u] & self.graph[v]

    def recommend(self, user):
        visited = set([user])
        queue = deque([user])
        rec = set()

        while queue:
            curr = queue.popleft()
            for nei in self.graph[curr]:
                if nei not in visited:
                    visited.add(nei)
                    queue.append(nei)
                    rec.add(nei)

        rec.discard(user)
        return rec


sn = SocialNetwork()

sn.add_user("Rahul")
sn.add_user("Priya")
sn.add_user("Amit")
sn.add_user("Sneha")
sn.add_user("Kiran")

sn.follow("Rahul", "Priya")
sn.follow("Rahul", "Amit")
sn.follow("Priya", "Sneha")
sn.follow("Amit", "Kiran")

print("Mutual Friends (Rahul & Priya):", sn.mutual_friends("Rahul", "Priya"))
print("Recommendations for Rahul:", sn.recommend("Rahul"))