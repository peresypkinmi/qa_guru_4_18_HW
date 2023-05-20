from voluptuous import Schema


class UserModels:
    user_model = Schema({"id": int,
                         "email": str,
                         "first_name": str,
                         "last_name": str,
                         "avatar": str})

    list_users_model = {"page": int,
                        "per_page": int,
                        "total": int,
                        "total_pages": int,
                        "data": [user_model],
                        "support": {"url": str,
                                    "text": str}}
