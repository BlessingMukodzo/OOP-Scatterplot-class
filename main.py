import matplotlib.pyplot as plt

#creating the class

class Point2D:
    def __init__(self, my_file):
        self.my_file = open(my_file,'r')
        self.x_coords = []
        self.y_coords = []
        self.translated_x = []
        self.translated_y = []
        self.my_file.readline()
        for line in self.my_file.readlines():
            self.x_coords.append(float(line.split(',')[0]))
            self.y_coords.append(float(line.split(',')[1]))

    def plot(self):
        plt.scatter(self.x_coords, self.y_coords, color='blue', label='Original Points')
        plt.scatter(self.translated_x, self.translated_y, color='red', label='Translated Points')
        plt.xlabel('X Coordinates')
        plt.ylabel('Y Coordinates')
        plt.title('Scatterplot of X and Y Coordinates')
        plt.grid()
        plt.legend()
        plt.show()

    def translate_points(self, dx, dy):
        self.translated_x = [x_coords + dx for x_coords in self.x_coords]
        self.translated_y = [y_coords + dy for y_coords in self.y_coords]

scatter_plotter = Point2D('C:/Users/User/Downloads/x_y_coordinates.txt')
scatter_plotter.translate_points(1, 1) # Example translation
scatter_plotter.plot()
