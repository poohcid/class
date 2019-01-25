"""กราฟข้อมูลน้ำฝน 2524 - 2558"""
import csv
import matplotlib.pyplot as plt
import numpy as np

def main():
    """ดึงข้อมูลน้ำฝนและแสดงผลเป็นกราฟ"""
    url = open(r'2524-2558.csv')
    reader = csv.reader(url)
    x = np.arange(2524, 2559)
    y = [int(i[1]) for i in reader]
    result = np.average(y)
    color = list(map(lambda x: '#1f77b4' if x >= result else 'r', y))
    plt.bar(x, y, color=color)
    plt.plot(x, [result]*len(x), 'r')
    plt.xticks(x, rotation=45)
    plt.text(2557, result+4, u'ค่าเฉลี่ยทั้งหมด 1458 มม.', fontname='JasmineUPC', fontsize='20')
    plt.show()

main()
