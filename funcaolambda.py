users = [
    {
        "id": 1,
        "name": "Allan",
        "age": 25,
        "profile _ picture": "http://...",
        "city": "São Paulo"
    },
    {
        "id": 2,
        "name": "Julie",
        "age": 29,
        "profile _ picture": "http://...",
        "city": "Curitiba"
    },
    {
        "id": 3,
        "name": "Pedro",
        "age": 31,
        "profile _ picture": "http://...",
        "city": "Rio de Janeiro"
    }
]

def users_over_25(user):
    return user["age"] > 25


filtered_users = filter(users_over_25, users)
list(filtered_users)

filtered_users = filter(lambda user: user["age"] > 25, users)
list(filtered_users)

