import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Plotting class
# Plot pie chart for creation source
# labels = 'Organization Invite', 'Guest Invite', 'Asana Signup', 'Google Auth',   'Personal Project'
# sizes = [34.7, 22.3, 18.2, 14.4, 10.4]

# fig1, ax1 = plt.subplots()
# ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
#         shadow=True, startangle=90)
# ax1.axis('equal')
# plt.show()



# Plot side by side bar chart for email domain
# labels = ['Gmail', 'Yahoo', 'Jourrapide', 'Gustr', 'Cuvox', 'Hotmail']
# signin = [33.2, 19.6, 10, 9.5, 9.3, 9.1]
# adopt = [33.6, 16.1, 10.3, 9.1, 8.7, 12.4]

# x = np.arange(len(labels))  # the label locations
# width = 0.35  # the width of the bars

# fig, ax = plt.subplots()
# rects1 = ax.bar(x - width/2, signin, width, label='Sign In')
# rects2 = ax.bar(x + width/2, adopt, width, label='Adopted')

# # Add some text for labels, title and custom x-axis tick labels, etc.
# ax.set_ylabel('Percent')
# ax.set_title('Percent of emails by Sign In & Adopted')
# ax.set_xticks(x)
# ax.set_xticklabels(labels)
# ax.legend()


# def autolabel(rects):
#     """Attach a text label above each bar in *rects*, displaying its height."""
#     for rect in rects:
#         height = rect.get_height()
#         ax.annotate('{}'.format(height),
#                     xy=(rect.get_x() + rect.get_width() / 2, height),
#                     xytext=(0, 3),  # 3 points vertical offset
#                     textcoords="offset points",
#                     ha='center', va='bottom')


# autolabel(rects1)
# autolabel(rects2)

# fig.tight_layout()

# plt.show()


#Plot bar graph for creation source adoption rate
x = np.arange(5)
money = [8.1, 17.1, 13.5, 14.5, 17.3]

fig, ax = plt.subplots()
plt.bar(x, money)
plt.xticks(x, ('Personal Proj', 'Guest', 'Org', 'Asana', 'Google'))
plt.show()
