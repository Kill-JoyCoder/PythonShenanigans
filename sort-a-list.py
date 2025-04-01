import pandas
import numpy as np
def sort_values():
    d=pandas.read_excel(data='List of Hackathon Names.xlsx')
    d.sort_values(by=['Name'], ascending=[True])
    d.sort_values(by=['First Date'], ascending=[True])
    d.sort_values(by=['Last Date'], ascending=[True])
    

sort_values()

