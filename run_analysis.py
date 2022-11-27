from iris_analysis.io.save import save
from iris_analysis.io.load import *
from iris_analysis.calculate import stats

header = ['name', 'mean', 'median', 'std']
data = [
    ["sepal.length", stats()[0], stats()[4], stats()[8]],
    ["sepal.width", stats()[1], stats()[5], stats()[9]],
    ["petal.length", stats()[2], stats()[6], stats()[10]],
    ["petal.width", stats()[3], stats()[7], stats()[11]]
]
print(save(header, data))


print(load2('results.csv'))
