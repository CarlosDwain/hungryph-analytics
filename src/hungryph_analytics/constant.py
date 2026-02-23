CITIES = {
    "Manila": {"lat": 14.5995, "lon": 120.9842},
    "Quezon City": {"lat": 14.6760, "lon": 121.0437},
    "Makati": {"lat": 14.5547, "lon": 121.0244},
    "Taguig": {"lat": 14.5176, "lon": 121.0509},
    "Pasig": {"lat": 14.5764, "lon": 121.0851},
    "Mandaluyong": {"lat": 14.5794, "lon": 121.0359},
    "Parañaque": {"lat": 14.4793, "lon": 121.0198},
    "Pasay": {"lat": 14.5378, "lon": 120.9918},
    "San Juan": {"lat": 14.6046, "lon": 121.0335},
    "Caloocan": {"lat": 14.6416, "lon": 120.9762}
}

FOOD_TYPES = [
    "Fast Food",          # Jollibee, McDo
    "Milk Tea",           # CoCo, Macao
    "Korean BBQ",         # Samgyupsal
    "Coffee & Bakery",    # Starbucks, Wildflour
    "Filipino Comfort",   # Sisig, Pares, Sinigang
    "Japanese",           # Ramen, Sushi
    "Chinese",            # Dimsum, Binondo-style
    "Healthy & Salads",   # SaladStop
    "Desserts",           # Halo-halo, Cakes
    "Street Food",        # Isaw, Fishballs
    "Chicken Inasal",     # Mang Inasal style
    "Pizza & Pasta"       # Yellow Cab, Shakey's
]

PAYMENT_METHODS = ["GCash", "Maya", "Cash on Delivery", "Credit Card"]

RIDER_TYPES = ["Bicycle", "Motorcycle", "Car"]

# Average speed in km/h considering Manila traffic
# Bicycles can lane-filter in tight streets; Cars get stuck in EDSA.
RIDER_CONFIG = {
    "Bicycle": {"avg_speed": 12, "max_dist_km": 5},
    "Motorcycle": {"avg_speed": 25, "max_dist_km": 15},
    "Car": {"avg_speed": 15, "max_dist_km": 25}
}