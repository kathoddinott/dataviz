import matplotlib.pyplot as plt
 
labels = ['CAN', 'USA', 'NOR', 'URS', 'FIN']
sizes = [23.16, 24.19, 16.93, 16.30, 16.08]
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'purple']
patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)
plt.legend(patches, labels, loc="best")
plt.axis('equal')
plt.tight_layout()
plt.show()