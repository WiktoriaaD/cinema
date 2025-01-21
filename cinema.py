

class Movie:
    def __init__(self, title, duration, showtimes):
        self.title = title
        self.duration = duration
        self.showtimes = showtimes

    def add_showtime(self, time):
        self.showtimes.append(time)
    
    def remove_showtime(self, time):
        if time in self.showtimes:
            self.showtimes.remove(time)
        else:
            print(f"Showtime {time} not found.")
    
    def display_details(self):
        print(f"{self.title} ({self.duration} min) - Showtimes: {', '.join(self.showtimes)}")

class Customer:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.reservations = []
    
    def add_reservation(self, movie, time):
        if time in movie.showtimes:
            self.reservations.append((movie.title, time))
            print(f"{self.first_name} reserved {movie.title} at {time}")
        else:
            print("Show not available.")
    
    def display_reservations(self):
        print(f"Reservations for: {self.first_name} {self.last_name}: {self.reservations}")

class VIPCustomer(Customer):
    def get_discounted_price(self, price):
        return price * 0.8
    
    def book_private_show(self, movie, time):
        print(f"VIP Private showtime reserved for {movie.title} at {time}")
        self.reservations.append((movie.title, time, "Private show."))

class Cinema:
    def __init__(self):
        self.movies = []
        self.customers = []
    
    def add_movie(self, movie):
        self.movies.append(movie)
    
    def add_customer(self, customer):
        self.customers.append(customer)
    
    def display_movies(self):
        for movie in self.movies:
            movie.display_details()

def main():
    cinema = Cinema()
    movie1 = Movie("Incepcja", 148, ["14:00", "18:00"])
    movie2 = Movie("Shrek", 90, ["15:00", "19:00"])
    cinema.add_movie(movie1)
    cinema.add_movie(movie2)
    
    customer = Customer("Jan", "Kowalski")
    vip = VIPCustomer("Alicja", "Smith")
    cinema.add_customer(customer)
    cinema.add_customer(vip)
    
    customer.add_reservation(movie1, "14:00")
    vip.book_private_show(movie2, "19:00")
    
    cinema.display_movies()
    customer.display_reservations()
    vip.display_reservations()

main()
