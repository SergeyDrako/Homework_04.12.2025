class Admin:
    def create_user(self, username):
        self.username = username

class Support:
    def create_ticket(self, name):
        self.name = name

class SuperUser(Admin, Support):
    pass

su = SuperUser()
su.create_user("Ivan")
su.create_ticket("Падает сервис")
# print(su.name)
# print(su.username)