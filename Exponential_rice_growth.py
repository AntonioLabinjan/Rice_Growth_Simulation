import matplotlib.pyplot as plt

# Initial amount of rice
initial_amount = 1

# Number of squares on a chess field
number_of_squares = 64

# List to store the amount of rice per each square
amount_per_square = []

# Calculate amount of rice on each square
for i in range(number_of_squares):
    amount_per_square.append(initial_amount)
    initial_amount *= 2
    
# Display results
for square, amount in enumerate(amount_per_square, start=1):
    print(f"Square {square}: {amount} grains of rice")
    
# Visualization
plt.plot(range(1, number_of_squares + 1), amount_per_square, marker='o')
plt.xlabel("Square Number")
plt.ylabel("Amount of Rice")
plt.title("Exponential Rice Growth on a Chessboard")
plt.yscale("log") # Logarithmic scale for y-axis
plt.grid(True)
plt.show()