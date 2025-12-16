class PermissionMixin:
    def has_permission(self, user_role):
        if user_role == 'admin':
            return True
        return False

class SecureAction(PermissionMixin):
    def execute(self, role):
        if self.has_permission(role):
            print("Админ. Метод запущен")
        else:
            print('Нет прав.')


action = SecureAction()
action.execute('admin')
action.execute('user')


