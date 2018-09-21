from matplotlib import pyplot as plt


subjects = ["Maths", "Islamiat", "Physics", "Chemistry", "PST"]
marks = [80,75,85,60,70]
# bars are by default width 0.8, so we'll add 0.1 to the left coordinates
# so that each bar is centered
xs = [i + 0.1 for i, _ in enumerate(subjects)]
print(xs)
# plot bars with left x-coordinates [xs], heights [num_oscars]
plt.colors()
plt.bar(xs, marks)
plt.ylabel("Marks")
plt.title("Subjects")
# label x-axis with movie names at bar centers
plt.xticks([i+0.5  for i, _ in enumerate(subjects)], subjects)
plt.show()