from datetime import datetime


class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        # no of books issued for enhancing feature and limit user from issuing more books
        #self.books_issued
        # update the fine amount associated with every user
        #self.fine_amount

    # Method to Add new user to library
    def add(self, library):
        # Check if given user id already exists in the library
        search_result = User.search(library.users, user_id=self.user_id)
        if len(search_result) != 0:
            # Cannot have 2 users with same User ID, failed to add user
            print(f"FAILED to add user, User ID: {self.user_id} already exists in library")
        else:
            # User ID does not exist, can add it to library
            library.users.append(self.__dict__)
            timestamp = datetime.now()
            # update log event
            library.log.append(f"{timestamp}:: ADDED new USER by the name :: {self.name} with user id :: {self.user_id} to the library")
            print("New User added to the library")

    # Method to update user details in library, only name can be updated
    def update(self, library):
        matching_user = User.search(library.users, None, self.user_id)
        user_record_index = matching_user[0]['index']
        library.users[user_record_index]['name'] = self.name
        timestamp = datetime.now()
        library.log.append(
            f"{timestamp}:: UPDATED User named {library.users[user_record_index]['name']} with user id :: {self.user_id}")

    # Method to delete an existing user from library
    def delete(self, library):
        # check if User ID is present in the system
        search_result = User.search(library.users, user_name=self.name, user_id=self.user_id)
        if len(search_result) != 0:
            # Removing the user
            library.users.remove(self)
            timestamp = datetime.now()
            library.log.append(f"{timestamp}:: DELETED user by the name :: {self.name} with user id {self.user_id} from the library")
        else:
            print(f"FAILED to delete user, User ID: {self.user_id} does not exists in library")

    # Search method for user based on name or user id or both. Also storing record index
    @staticmethod
    def search(user_list, user_name=None, user_id=0):
        matching_users = []
        for count, user in enumerate(user_list):
            if (user_name is None or user_name.lower() in user['name'].lower()) and (user_id == 0 or user_id == user['user_id']):
                matching_users.append({"index": count, "users": user})
        return matching_users



