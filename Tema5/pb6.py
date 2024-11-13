class LibraryItem:
    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id
        self.checked_out = False

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            print(f"{self.title} has been checked out.")
        else:
            print(f"{self.title} is already checked out.")

    def return_item(self):
        if self.checked_out:
            self.checked_out = False
            print(f"{self.title} has been returned.")
        else:
            print(f"{self.title} was not checked out.")

    def display_info(self):
        status = "Checked Out" if self.checked_out else "Available"
        return f"ID: {self.item_id}, Title: {self.title}, Status: {status}"

class Book(LibraryItem):
    def __init__(self, title, item_id, author, pages):
        super().__init__(title, item_id)
        self.author = author
        self.pages = pages

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Author: {self.author}, Pages: {self.pages}"

class DVD(LibraryItem):
    def __init__(self, title, item_id, director, duration):
        super().__init__(title, item_id)
        self.director = director
        self.duration = duration

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Director: {self.director}, Duration: {self.duration} mins"

class Magazine(LibraryItem):
    def __init__(self, title, item_id, issue, publisher):
        super().__init__(title, item_id)
        self.issue = issue
        self.publisher = publisher

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Issue: {self.issue}, Publisher: {self.publisher}"

book = Book("The Great Gatsby", "B001", "F. Scott Fitzgerald", 218)
print(book.display_info())
book.check_out()
print(book.display_info())
book.return_item()

dvd = DVD("Inception", "D001", "Christopher Nolan", 148)
print(dvd.display_info())
dvd.check_out()
print(dvd.display_info())
dvd.return_item()

magazine = Magazine("National Geographic", "M001", "March 2023", "National Geographic Society")
print(magazine.display_info())
magazine.check_out()
print(magazine.display_info())
magazine.return_item()