"""

"""
import csv
import matplotlib.pyplot as plt
import numpy as np

def plot_location_2558():
    """กราฟเส้นของแต่ละภาค"""
    url = open(r'2548-2558.csv')
    reader = list(csv.reader(url))
    data_year = [float(i) for i in reader[-1][1:]]
    color = ['c', 'green', 'magenta', 'coral', 'royalblue', 'lightskyblue']
    region = ["northern", "northeastern", "central", "western", "southwestern", "southeastern"]
    plt.bar(region, data_year[:-1], color=color, width=0.5)
    plt.plot(region, [data_year[-1]]*6, 'r--')
    plt.title(u'กราฟข้อมูลปริมาณน้ำฝนในปี พ.ศ. 2558', fontname='JasmineUPC', fontsize='20')
    plt.xlabel(u'ภูมิภาค', fontname='JasmineUPC', fontsize='20')
    plt.ylabel(u'ปริมาณน้ำฝน(มม.)', fontname='JasmineUPC', fontsize='20')
    plt.text(region[0], data_year[-1]+15, u'average is = %.2f mm' %data_year[-1])
    add_text(region, data_year[:-1], 40, 160)
    plt.grid(axis='y', alpha=0.75)
    plt.show()

def location(count):
    """อ่านข้อมูลแล้วส่งข้อมูลเป็น list ของแต่ละภาค"""
    url = open(r'2548-2558.csv')
    reader = csv.reader(url)
    return [float(i[count]) for i in reader]

def add_text(var_x, var_y, count1, count2):
    for i in range(len(var_x)):
        rain = '%.2f' %var_y[i]
        rain = rain.rstrip("0")
        if i != 1:
            plt.text(var_x[i], var_y[i]+count1, u'%s' %rain, fontsize=24, style='oblique', ha='center', fontname='EucrosiaUPC')
        else:
            plt.text(var_x[i], var_y[i]+count2, u'%s' %rain, fontsize=24, style='oblique', ha='center', fontname='EucrosiaUPC')

plot_location_2558()
