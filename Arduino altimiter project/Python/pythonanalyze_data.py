import pandas as pd
import matplotlib.pyplot as plt

# Load logged data
df = pd.read_csv("data.csv")

# Compute velocity and acceleration
df["velocity"] = df["altitude"].diff() / df["time"].diff()
df["acceleration"] = df["velocity"].diff() / df["time"].diff()

df = df.dropna().reset_index(drop=True)

# Save enhanced dataset
df.to_csv("data_with_vel_acc.csv", index=False)

# Plot: Altitude vs Time
plt.figure(figsize=(6, 4))
plt.plot(df["time"], df["altitude"])
plt.title("Altitude vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Altitude (m)")
plt.grid(True)
plt.savefig("altitude_vs_time.png")

# Plot: Velocity vs Time
plt.figure(figsize=(6, 4))
plt.plot(df["time"], df["velocity"])
plt.title("Velocity vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.grid(True)
plt.savefig("velocity_vs_time.png")

# Plot: Acceleration vs Time
plt.figure(figsize=(6, 4))
plt.plot(df["time"], df["acceleration"])
plt.title("Acceleration vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Acceleration (m/s²)")
plt.grid(True)
plt.savefig("acceleration_vs_time.png")