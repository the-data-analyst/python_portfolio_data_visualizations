import matplotlib.pyplot as plt
#samsung smartwatch 1st qtr sales over time
#read data from file
#cleanse data
#visualize data using bar chart

def samsungSales ():

    infile = open('sales.txt','r')

    aline = infile.readline()

    saleslist = []

    while aline != '':
        saleslist.append (int(aline))

        aline = infile.readline().rstrip('\n')

    infile.close()

    x = [0,10,20,30,40]

    plt.xticks([0, 10, 20, 30, 40], ['2016', '2017', '2018', '2019', '2020'])   

    plt.yticks([0, 100, 200, 300, 400, 500], ['$0m', '$1m', '$2m', '$3m', '$4m','$5m'])
    plt.title('SAMSUNG SMARTWATCH 1ST QTR SALES')
    
    plt.xlabel ('YEAR')
    plt.ylabel ('REVENUE')
    width = 5

    plt.bar (x,saleslist,width, color = ('r','g','b','k'))

    plt.show()

samsungSales ()

    
