import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from docx import Document
from docx2pdf import convert
from utils.graph_types import bar_chart,grouped_bar_chart
from pathlib import Path

# time_stamp = int(time.time())



DATA_PATH = Path('data')

def create_bar_chart():
    df_fifa21 = pd.read_csv(f'{DATA_PATH}/players_20.csv')
    country = ['United States', 'Canada', 'England', 'Brazil', 'Argentina']
    df_country = df_fifa21[df_fifa21['nationality'].isin(country)]
    new_df = pd.concat(
        [df_country[df_country['nationality'] == 'Argentina'][:20],
         df_country[df_country['nationality'] == 'Brazil'][:20],
         df_country[df_country['nationality'] == 'England'][:20],
         df_country[df_country['nationality'] == 'Canada'][:20],
         df_country[df_country['nationality'] == 'United States'][:20]]
    )
    image_path = bar_chart(title="Chart",xlabel="X label",ylabel="Y Labele",df=new_df,group_by="nationality",xplot="nationality",yplot="overall")
    print(f'Image saved to:{image_path}')

def create_grouped_bar_chart():
    groups = ['Spain Primera Division', 'Italian Serie A', 'German 1. Bundesliga']
    group_by = ['nationality', 'league_name']
    xplot ='nationality'
    yplot='sofifa_id'
    df_fifa21 = pd.read_csv(f'{DATA_PATH}/players_20.csv')
    country = ['United States', 'Canada', 'England', 'Brazil', 'Argentina']
    df_country = df_fifa21[df_fifa21['nationality'].isin(country)]
    df = df_country[df_country['league_name'].isin(groups)]
    image_path = grouped_bar_chart(title="Title",xlabel="X label",ylabel="Y label",df=df,group_by=group_by,xplot=xplot,yplot=yplot,field='league_name')
    print(f'Image saved to:{image_path}')

def init():
   create_bar_chart()
   create_grouped_bar_chart()
   

if __name__ == '__main__':
    init()
