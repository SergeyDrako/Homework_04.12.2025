emails = ["test@gmail.com", "invalid-email", "user@company.ru", "no@domain"]

email_find = list(filter(lambda find: '@' in find and find.endswith(".com") or find.endswith(".ru"), emails))
print(email_find)



