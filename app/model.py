import math
import random

class Model():

    def predict(self, sales, category):
        ran_num = random.uniform(-1,1)
        log  = math.log(sales)
        return log * ran_num + category