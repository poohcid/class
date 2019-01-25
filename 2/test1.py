"""BusStop I"""
import csv
import matplotlib.pyplot as plt
def main():
    """BusStop I"""
    with open(r'Exchange1997-2016.csv') as csvfile:
        reader = csv.reader(csvfile)
        for i in reader:
            print(i)

main()
