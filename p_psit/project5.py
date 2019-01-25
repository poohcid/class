"""

"""
import csv
import matplotlib.pyplot as plt
import numpy as np

def plot_region_rank():
    """กราฟเส้นของแต่ละภาค"""
    region = ["northern", "northeastern", "central", "western", "southwestern", "southeastern"]
    dct_average, dct_color = {}, {}
    color = ['c', 'green', 'magenta', 'coral', 'royalblue', 'lightskyblue']
    for i in range(1, 7):
        result = np.average(location(i))
        dct_average[region[i-1]] = result
        dct_color[color[i-1]] = result
    region.sort(key=lambda x: dct_average[x])
    color.sort(key=lambda x: dct_color[x])
    rain = [dct_average[i] for i in region]
    plt.bar(region, rain, color=color, width=0.5)
    plt.title(u'กราฟเรียงลำดับภูมิภาคจากระดับน้ำฝนเฉลี่ยทั้งหมดจากน้อยไปมาก', fontname='JasmineUPC', fontsize='20')
    plt.xlabel(u'ภูมิภาค', fontname='JasmineUPC', fontsize='20')
    plt.ylabel(u'ปริมาณน้ำฝน(มม.)', fontname='JasmineUPC', fontsize='20')
    add_text(region, rain, 40, 40)
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

plot_region_rank()
