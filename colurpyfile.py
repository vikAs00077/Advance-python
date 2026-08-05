import matplotlib.pyplot as plt

# Five shades of teal blue
colors = [
    "#004D61",
    "#006D77",
    "#008080",
    "#1FA2A5",
    "#5BC0BE",
    "#ffffff"
]

fig, ax = plt.subplots(figsize=(10, 2))

for i, color in enumerate(colors):
    ax.barh(0, 1, left=i, color=color)
    ax.text(
        i + 0.5,
        -0.25,
        color,
        ha="center",
        va="top",
        fontsize=10,
        fontweight="bold"
    )

ax.set_xlim(0, len(colors))
ax.set_ylim(-0.5, 0.5)
ax.axis("off")

plt.title("5 Shades of Teal Blue", fontsize=14, fontweight="bold")
plt.show()