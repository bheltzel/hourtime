#from Tkinter import *mk

# import the Tkinter GUI interface
import Tkinter
import pymongo
from pymongo import MongoClient

# create a class while inheriting the base Tkinter GUI
class time_entry(Tkinter.Tk):
    # create a hierarchy of elements
    def __init__(self, parent):
        Tkinter.Tk.__init__(self, parent)
        # identify the parent and set as variable
        self.parent = parent
        # reference the initialize method for when
        #    the GUI starts up
        self.initialize()

    # method for starting the GUI
    def initialize(self):
        #create layout
        self.grid()

        # entry is a method for text box
        self.entry = Tkinter.Entry(self)
        # put the textbox in the grid layout
        # EW makes it stick to the edges L & R
        self.entry.grid(column=0, row=0, sticky='EW')

        def button_cb():
            # init mongodb conn
            client = MongoClient()
            # assign db primer to var db
            db = client.test
            # access collection of data set, set to var
            clctn = db.dataset

            # insert
            result = db.restaurants.insert_one(
                {
                    "address": {
                        "street": "945 amsterdam"
                    }
                }
            )

            cursor = db.restaurants.find()
            for document in cursor:
                # put text into the entry / text box
                self.entry.insert(0, document)
                print(document)

            # delete all documents / records
            # result = db.restaurants.delete_many({"address.street": "945 amsterdam"})

        # create a button
        button = Tkinter.Button(self, text=u"POV6", command=button_cb)
        button.grid(column=0, row=1, sticky='EW')

        button_2 = Tkinter.Button(self, text=u"3M")
        button_2.grid(column=1, row=1, sticky='EW')

# references the main element of the class
if __name__ == "__main__":
    # set the window name
    app = time_entry(None)
    # title the window
    app.title('Time Entry')
    # make the window always active until closed
    app.mainloop()

