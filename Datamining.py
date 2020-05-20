import time
import pandas as pd
import matplotlib.pyplot as plt

import warnings

warnings.filterwarnings("ignore")
start_time = time.time()

folder_path = "/Users/varun/Desktop/program projects/summer 2019/OP_DTL_GNRL_PGYR2018_P06282019.csv"
df = pd.read_csv(folder_path, index_col=0)
states = df["Recipient_State"].value_counts()
drugs1 = df['Name_of_Drug_or_Biological_or_Device_or_Medical_Supply_1'].str.lower().value_counts()
areas1 = df['Product_Category_or_Therapeutic_Area_1'].str.lower().value_counts()
drugs2 = df['Name_of_Drug_or_Biological_or_Device_or_Medical_Supply_2'].str.lower().value_counts()
areas2 = df['Product_Category_or_Therapeutic_Area_2'].str.lower().value_counts()
drugs3 = df['Name_of_Drug_or_Biological_or_Device_or_Medical_Supply_3'].str.lower().value_counts()
areas3 = df['Product_Category_or_Therapeutic_Area_3'].str.lower().value_counts()


def combine():
    #create new csv

    #put area1, area2, area3 in same column
    #put drug1, drug2, drug3 in same column
    #match to correct state
        #all must be in order
    #call counts for drugs and pain in new csv


    pass


def run():
    call = ""
    while call != "end":
        call = input("What would you like to do: ")
        if call == "run":
            state = input("which variable would you like to graph? ")
            if state == "states":
                states.plot('bar')
                print("program running...")
                plt.draw()
                plt.show(block = False)
                print("graphs complete. to view, end program")
            else:
                print("that is not an option")
        else:
            elapsed_time = time.time() - start_time
            m, s = divmod(elapsed_time, 60)
            timer = "%02d:%02d" % (m, s)
            print('Time elapsed:', timer, '\n')
            print("Program ended")
            plt.show()
        pass
    pass

run()
