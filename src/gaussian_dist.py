import math
import matplotlib.pyplot as plt

class Gaussian_dist():
    """
    This is a Gaussian distribution class for calculating and visualizing 
    a gaussian ditribution class

    Attributes:
    - mean (float) representing the mean value of the distribution
    - stdev (float) representing the standard deviation of the distribution
    - data (list of floats) a list of floats extracted from a data file
 
    """

    def __init__(self, mu = 0, sigma = 1):
        """
        This is how we intend to create a gaussian distribution object at the beginning,
        by creating the simplest special case when the mean mu=0 and the standard deviation
        sigma=1
        """
        self.mean = mu
        self.stdev=sigma
        self.data = []

    def calculate_mean(self):
        """ Method to calculate the mean of the dataset
        Args: None

        Returns:
         float: mean of the data set.
        """
        print("len(self.data):",len(self.data))
        the_mean= 1.0 * sum(self.data)/len(self.data)
        self.mean=the_mean
        print("self.mean=",self.mean)
        return self.mean

    def calculate_stdev(self,sample = True):
        """Method to calculate the standard deviation of the dataset
        Args: 
            sample (boolean): whether the data represents a sample or population
        Returns:
            float: The standard deviation of the dataset
        """
        if sample:
            n = len(self.data) -1
        else:
            n = len(self.data)
        
        mean=self.mean

        sigma_pow2 = 0

        for line in self.data:
            sigma_pow2 += (line - mean) ** 2
        
        sigma = math.sqrt(sigma_pow2 / n)
        self.stdev = sigma
        print("self.stdev1=",self.stdev)
        return self.stdev

    def read_data_file(self, file_name, sample = True):
        """ Method to read in data from a txt file:
        The txt file must have only 1 number (float) per line.
        The numbers are stored in the data attribute.
        After reading in the file, the mean and the standard deviation are calculated.

        Args:
            file_name (string):name of a txt file to read data from.
        Returns: 
            None 
        """
        with open (file_name) as file:
            data_list = []

            line = file.readline()
            while line:
                data_list.append(float(line))
                line = file.readline()
        file.close()
        print("data_list:",data_list)
        self.data = data_list
        self.mean = self.calculate_mean()
        print("mean_data_list=",self.mean)
        self.stdev = self.calculate_stdev(sample)
        print("stdev_data_list=",self.stdev)
    
    
    def plot_histogram(self):
        """Function to output a histogram of the instance variable data using 
        matplotlib pyplot library.
        
        Args:
            None
            
        Returns:
            None
        """
        plt.hist(self.data)
        plt.title('Histogram of Data')
        plt.xlabel('data')
        plt.ylabel('count')
    
    def pdf(self, x):
        """Probability density function calculator for the gaussian distribution.
        
        Args:
            x (float): point for calculating the probability density function
            
        
        Returns:
            float: probability density function output
        """
        
        return (1.0 / (self.stdev * math.sqrt(2*math.pi))) * \
            math.exp(-0.5*((x - self.mean) / self.stdev) ** 2)
            