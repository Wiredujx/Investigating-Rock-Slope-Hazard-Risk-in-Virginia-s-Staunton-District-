import pandas as pd


def importData():
    rock_slopes = pd.read_csv('Rock_Slopes_Table-Rock_Slope_Data.csv', encoding='cp1252')
    #print(rock_slopes.to_string())
    #print(rock_slopes.head(5).to_string())
    return rock_slopes

def main():
    importData()

if __name__ == "__main__":
    main()