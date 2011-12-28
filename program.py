#!/usr/bin/python
#
# program.py
#
# 2011 - Prit Ranjan - emailprit@gmail.com
#
# Usage:
#       ./program.py data_csv_file[Req] item1[Req] item2[Opt] ... (if program.py is executable)
#    OR python program.py data_csv_file[Req] items1[Req] item2[Opt]
#

import sys
import traceback

def Print(obj):
    '''
    A method to see a big dictionary in a better format.
    '''
    import pprint
    pp=pprint.PrettyPrinter(indent=4)
    pp.pprint(obj)

class solution(object):
    
    def __init__(self):
        self.Map={} # Dictionary format - item1: (restaurantID, price, [item1, item2, item3, ... ])
    
    def createMap(self, filename):
        '''
        Reads the csv file and create a dictionary.
        '''
        try:
            file=open(filename, 'r')
        except:
            raise Exception("File %s doesn't exists. Please check." %(filename,))

        for line in file:
            try:
                line=line.strip()
                lst=line.split(',')
                restaurantID=lst[0].strip()
                price=float(lst[1].strip())
                items=[i.strip() for i in lst[2:]]
            except:
                raise Exception("Error while reading file %s" %(filename,))

            # Key as item and values as restaurantID, price and all items which will be purchased along with item
            for item in items:
                if self.Map.has_key(item):
                    self.Map[item].append((restaurantID, price, items))
                else:
                    self.Map[item]=[]
                    self.Map[item].append((restaurantID, price, items))

        #Print(self.Map)

    def search(self, searchItems):
        '''
        A search method which searches the best deal in self.Map
        '''
        purchaseOptions={} # restaurantID: [price, [item1, item2, ...]]
        
        for searchItem in searchItems:
            if self.Map.has_key(searchItem): # if item not available then raise
                deals=self.Map[searchItem] # [(restaurantID, price, [item1, item2, ...]), ... ]
            else:
                raise Exception("Failed to find any matching restaurant for you. Giving up :(")

            if purchaseOptions: # If initial dictionary is not empty
                for deal in deals:
                    dealFound=0
                    if purchaseOptions.has_key(deal[0]): # If restaurantID is already present then purchase
                        dealFound=1
                        price, items = purchaseOptions[deal[0]]
                        if searchItem not in items:
                            purchaseOptions[deal[0]] = (price+deal[1], items+deal[2])
                if not dealFound:
                    raise Exception("Failed to find any matching restaurant for you. Giving up :(")
            else: # If empty then add all options
                for deal in deals:
                    purchaseOptions[deal[0]] = (deal[1], deal[2])

        #Print(deals)
        bestDeal=min(purchaseOptions.iteritems(), key=lambda x: x[1])
        #Print(bestDeal)
        return bestDeal

if __name__=="__main__":
    if len(sys.argv) < 3:
        print 'Insufficient arguments. Usage: %s DataFileCSV[Req] Item1[Req] Item2[Opt] Item3[Opt] ...' %(sys.argv[0],)
        sys.exit()
    try:
        filename=sys.argv[1]
        items=sys.argv[2:]

        obj=solution()
        obj.createMap(filename) # Creating Map
        bestDeal=obj.search(items) # Searching items in Map
        
        # Now it's time to publish results :)
        print '\n------------------------------------------------------------------'
        print "Here is the best deal for you.\n\nRestaurantID: %s\nPrice: %s\nMenu: %s"\
            %(bestDeal[0], bestDeal[1][0], ', '.join([ i.title() for i in bestDeal[1][1] ]))
        print '------------------------------------------------------------------\n'

    except Exception, e:
        print e
        #print traceback.format_exc() # for debugging
        
