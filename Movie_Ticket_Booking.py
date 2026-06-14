class MovieTicketBooking:

    def __init__(self):
        self.movies = []
        self.shows = {}
        self.bookings = []

    # ================= ADMIN SECTION =================

    def add_movie(self):
        movie = input("Enter Movie Name: ")
        self.movies.append(movie)
        print("Movie Added Successfully")

    def view_movies(self):
        if not self.movies:
            print("No Movies Available")
        else:
            print("\nAvailable Movies")
            for i, movie in enumerate(self.movies, start=1):
                print(i, movie)

    def add_show(self):
        movie = input("Enter Movie Name: ")

        if movie not in self.movies:
            print("Movie Not Found")
            return

        show_time = input("Enter Show Time: ")

        if movie not in self.shows:
            self.shows[movie] = []

        self.shows[movie].append(show_time)

        print("Show Added Successfully")

    def delete_movie(self):
        movie = input("Enter Movie Name To Delete: ")

        if movie in self.movies:
            self.movies.remove(movie)

            if movie in self.shows:
                del self.shows[movie]

            print("Movie Deleted Successfully")

        else:
            print("Movie Not Found")

    def view_bookings(self):
        if not self.bookings:
            print("No Bookings Available")
        else:
            print("\nBooking Details")
            for booking in self.bookings:
                print(booking)

    # ================= USER SECTION =================

    def view_shows(self):

        movie = input("Enter Movie Name: ")

        if movie in self.shows:

            print("Available Shows")
            for show in self.shows[movie]:
                print(show)

        else:
            print("No Shows Available")

    def book_ticket(self):

        movie = input("Enter Movie Name: ")

        if movie not in self.movies:
            print("Movie Not Available")
            return

        if movie not in self.shows:
            print("No Shows Available")
            return

        print("\nAvailable Shows")
        for show in self.shows[movie]:
            print(show)

        show_time = input("Select Show Time: ")

        seats = int(input("Number Of Seats: "))

        customer = input("Customer Name: ")

        booking = {
            "Customer": customer,
            "Movie": movie,
            "Show": show_time,
            "Seats": seats
        }

        self.bookings.append(booking)

        print("Ticket Booked Successfully")

    def user_booking_details(self):

        name = input("Enter Customer Name: ")

        found = False

        for booking in self.bookings:

            if booking["Customer"] == name:
                print(booking)
                found = True

        if not found:
            print("No Booking Found")


# ================= MAIN PROGRAM =================

system = MovieTicketBooking()

while True:

    print("\n===== MOVIE TICKET BOOKING SYSTEM =====")
    print("1. Admin")
    print("2. User")
    print("3. Exit")

    role = input("Enter Choice: ")

    if role == "1":

        while True:

            print("\n===== ADMIN MENU =====")
            print("1. Add Movie")
            print("2. Add Show")
            print("3. Delete Movie")
            print("4. View Bookings")
            print("5. Back")

            choice = input("Enter Choice: ")

            if choice == "1":
                system.add_movie()

            elif choice == "2":
                system.add_show()

            elif choice == "3":
                system.delete_movie()

            elif choice == "4":
                system.view_bookings()

            elif choice == "5":
                break

            else:
                print("Invalid Choice")

    elif role == "2":

        while True:

            print("\n===== USER MENU =====")
            print("1. View Movies")
            print("2. View Shows")
            print("3. Book Ticket")
            print("4. View Booking")
            print("5. Back")

            choice = input("Enter Choice: ")

            if choice == "1":
                system.view_movies()

            elif choice == "2":
                system.view_shows()

            elif choice == "3":
                system.book_ticket()

            elif choice == "4":
                system.user_booking_details()

            elif choice == "5":
                break

            else:
                print("Invalid Choice")

    elif role == "3":
        print("Thank You")
        break

    else:
        print("Invalid Choice")
