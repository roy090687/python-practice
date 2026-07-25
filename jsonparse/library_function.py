library_data = {
    "library_name": "City Central Library",
    "location": "Downtown",
    "books": [
        {
            "title": "The Silent Patient",
            "author": {"name": "Alex Michaelides", "nationality": "Cypriot"},
            "year": 2019,
            "genres": ["Thriller", "Mystery"],
            "borrowers": [
                {"name": "John", "age": 25, "membership": "Gold"},
                {"name": "Priya", "age": 34, "membership": "Silver"}
            ]
        },
        {
            "title": "Educated",
            "author": {"name": "Tara Westover", "nationality": "American"},
            "year": 2018,
            "genres": ["Memoir", "Biography"],
            "borrowers": []
        },
        {
            "title": "Atomic Habits",
            "author": {"name": "James Clear", "nationality": "American"},
            "year": 2018,
            "genres": ["Self-help", "Productivity"],
            "borrowers": [
                {"name": "Sara", "age": 27, "membership": "Platinum"}
            ]
        },
        {
            "title": "Sapiens",
            "author": {"name": "Yuval Noah Harari", "nationality": "Israeli"},
            "year": 2011,
            "genres": ["History", "Anthropology", "Thriller"],
            "borrowers": [
                {"name": "Amit", "age": 41, "membership": "Gold"},
                {"name": "Leo", "age": 19, "membership": "Silver"}
            ]
        }
    ]
}

def get_first_two_elements(data):
    print("Library Name:", data["library_name"])
    print("Library Location:", data["location"])

def get_book_titles_publish_after_year(data, year):
    result = []
    for book in data["books"]:
        if book["year"] > year:
            result.append(book["title"])
    return result

def get_borrowers_gold_membership(data, membership):
    result = []
    for book in data["books"]:
        for borrower in book.get("borrowers", []):
            if borrower["membership"] == membership:
                result.append(borrower["name"])
    return result

def get_genres_group_by_title(data):
    genre_map = {}
    for book in data["books"]:
        for genre in book.get("genres", []):
            if genre not in genre_map:
                genre_map[genre] = []
            # Add book-titles to the genre list
            genre_map[genre].append(book.get("title"))
    return genre_map

# Find the book that has the highest number of borrowers.
def get_highest_number_of_borrowers(data):
    result = []
    max_count = 0

    for book in data["books"]:
        borrower_count = len(book.get("borrowers"))
        if borrower_count > max_count:
            max_count = borrower_count
            title = book["title"]
            borrower_names = []
            for b in book["borrowers"]:
                borrower_names.append(b.get("name"))
            # reset result with this book
            result = [(title, borrower_count, borrower_names)]
        elif borrower_count == max_count and borrower_count > 0:
            max_count = borrower_count
            title = book["title"]
            borrower_names = []
            for b in book["borrowers"]:
                borrower_names.append(b["name"])
            result.append((title, borrower_count, borrower_names))
    return result

# Group authors by nationality and list their books.
def group_authors_by_nationality(data):
    nationality_map = {}
    for book in data["books"]:
        nationality = book["author"]["nationality"]
        title = book["title"]
        if nationality not in nationality_map:
            nationality_map[nationality] = []
        nationality_map[nationality].append(title)
    return nationality_map


# Calculate the average age of all borrowers across the library
def calculate_avg_age_borrowers(data):
    ages = []
    for book in data["books"]:
        for borrower in book.get("borrowers", []):
            ages.append(borrower["age"])
    return sum(ages)/len(ages)


def print_results():
    get_first_two_elements(library_data)
    book_titles = get_book_titles_publish_after_year(library_data, 2011)
    borrowers_names = get_borrowers_gold_membership(library_data, "Gold")
    genre_groups = get_genres_group_by_title(library_data)
    highest = get_highest_number_of_borrowers(library_data)
    group_nationality = group_authors_by_nationality(library_data)
    avg_age = calculate_avg_age_borrowers(library_data)

    print("Book titles published after a given year 2011:", book_titles)
    print("Borrowers who have a 'Gold' membership:", borrowers_names)
    print("Books grouped by genres:")
    for genre, titles in genre_groups.items():
        print(f"{genre}: {', '.join(titles)}")

    print("Book(s) with the highest number of borrowers:")
    for item in highest:
        title = item[0]
        count = item[1]
        borrowers = item[2]
        print(f"{title}: {count} borrowers ({', '.join(borrowers)})")

    print("Group authors by nationality and list their books:-")
    for nationality, title in group_nationality.items():
        print(f"{nationality}: {', '.join(title)}")

    print("Average age is:", avg_age)

# -------------------------------
# Call the main function
# -------------------------------
print_results()
