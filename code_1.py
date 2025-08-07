import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

start = time.time()
# Create a random DataFrame
np.random.seed(0)  # For reproducibility
data = {
    'A': np.random.rand(10),
    'B': np.random.rand(10),
    'C': np.random.rand(10)
}
df = pd.DataFrame(data)

# Plot the DataFrame
plt.figure(figsize=(10, 6))
for column in df.columns:
    plt.plot(df.index, df[column], label=column)

plt.title('Random Data Frame Plot')
plt.xlabel('Index')
plt.ylabel('Values')
plt.legend()
plt.grid(True)
print('ok')
# Save the plot as a PNG file
plt.savefig('random_dataframe_plot.png')
# Show the plot (optional)
# plt.show()
end = time.time()
print(f"Execution time: {end - start} seconds")