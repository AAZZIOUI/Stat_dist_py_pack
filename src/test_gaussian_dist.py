from gaussian_dist import Gaussian_dist

#Gaussian_dist().read_data_file("data_file.txt",sample=True)
def test_Gaussian_dist_mean():
    assert(Gaussian_dist(20,2).mean==20)

def test_Gaussian_dist_stdev():
    assert(Gaussian_dist(100,5).stdev==5)

def test_Gaussian_dist_read_file_mean():
    file_name='my_file.txt'
    gauss = Gaussian_dist()
    gauss.read_data_file(file_name,sample=True)
    file_mean = gauss.calculate_mean()
    assert(file_mean==3.0)
def test_Gaussian_dist_read_file_stdev():
    file_name='my_file.txt'
    gauss = Gaussian_dist()
    gauss.read_data_file(file_name,sample=True)
    file_stdev = round(gauss.calculate_stdev(sample=True),5)
    assert(file_stdev==0.89443)





