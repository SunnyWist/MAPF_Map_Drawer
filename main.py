import numpy as np
import yaml

import matplotlib.pyplot as plt
import matplotlib.patches as patches

from config import *

plt.rcParams["text.usetex"] = True
plt.rc("text.latex", preamble=r"\usepackage{bm}")

# Read the CSV file
data = np.genfromtxt(MAP_FILE_PATH, delimiter=",")

# Read the YAML file
with open(MAP_INFO_FILE_PATH, "r") as f:
    add_info = yaml.safe_load(f)
agents_count = len(add_info["Agents"])
goals_count = len(add_info["Goals"])

# Create a grid of x and y coordinates
x = np.arange(data.shape[1])
y = np.arange(data.shape[0])
X, Y = np.meshgrid(x, y)

fig, ax = plt.subplots(figsize=(6, 6))
plt.pcolormesh(X, Y, data, cmap="Greys", edgecolors="black", linewidth=1)
ax.xaxis.tick_top()
ax.invert_yaxis()
plt.xticks(np.arange(0, data.shape[1], 1), fontsize=24)
plt.yticks(np.arange(0, data.shape[0], 1), fontsize=24)


agent_num = 0
for agent_name, agent_pos in add_info["Agents"].items():
    plt.gca().add_patch(
        patches.Circle(
            (agent_pos[0], agent_pos[1]), 0.45, color=COLORS_CYCLE[agent_num % len(COLORS_CYCLE)], fill=True, zorder=3
        )
    )
    agent_text = r"$\bm{" + agent_name + r"}$"
    plt.text(
        agent_pos[0],
        agent_pos[1],
        agent_text,
        fontsize=INFO_FONT_SIZE,
        math_fontfamily="cm",
        color="white",
        fontweight="bold",
        ha="center",
        va="center",
        zorder=4,
    )
    agent_num += 1

goals_num = 0
for goal_name, goal_pos in add_info["Goals"].items():
    plt.gca().add_patch(
        patches.Rectangle(
            (goal_pos[0] - 0.9 / 2, goal_pos[1] - 0.9 / 2),
            0.9,
            0.9,
            color=COLORS_CYCLE[goals_num % len(COLORS_CYCLE)],
            fill=True,
            zorder=3,
        )
    )
    goal_text = r"$\bm{" + goal_name + r"}$"
    plt.text(
        goal_pos[0],
        goal_pos[1],
        goal_text,
        fontsize=INFO_FONT_SIZE,
        math_fontfamily="cm",
        color="white",
        fontweight="bold",
        ha="center",
        va="center",
        zorder=4,
    )
    goals_num += 1

# Show the plot
plt.show()
