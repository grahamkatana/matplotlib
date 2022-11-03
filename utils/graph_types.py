import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time
from pathlib import Path

IMAGE_PATH = Path('images')
DATA_PATH = Path('data')
time_stamp = int(time.time())

# document = Document()
# paragraph = document.add_paragraph("Printing images to a file")

# set global graph styles
# sns.set_style('darkgrid')
# plt.rc('axes', titlesize=18)
# plt.rc('axes', labelsize=14)
# plt.rc('ytick', labelsize=13)
# plt.rc('xtick', labelsize=13)
# plt.rc('legend', fontsize=13)
# plt.rc('font', size=13)

# # figure sizes
# plt.figure(figsize=(8, 4), tight_layout=True)

df_fifa21 = pd.read_csv(f'{DATA_PATH}/players_20.csv')
country = ['United States', 'Canada', 'England', 'Brazil', 'Argentina']
df_country = df_fifa21[df_fifa21['nationality'].isin(country)]

# barplot = df_country.groupby(['nationality'], as_index=False).mean()[
#     ['nationality', 'overall']]


# use matplotlib to plot
# plt.figure(figsize=(8,4), tight_layout=True)
# colors = sns.color_palette('pastel')
# plt.bar(barplot['nationality'], barplot['overall'], color=colors[:5])
# plt.xlabel('Nationality')
# plt.ylabel('Average Rating')
# plt.title('Barplot')
# plt.show()

# use seaborn
def bar_chart(title,xlabel,ylabel,df,group_by,xplot,yplot):
    barplot = df.groupby([group_by], as_index=False).mean()[
        [xplot, yplot]]
    plt.figure(figsize=(8, 4), tight_layout=True)
    ax = sns.barplot(x=barplot[xplot],
                     y=barplot[yplot], palette='pastel', ci=None)
    ax.set(title=title, xlabel=xlabel, ylabel=ylabel)
    graph_image_location = plt.savefig(f'{IMAGE_PATH}/{time_stamp}_bar.png', bbox_inches='tight')
    return graph_image_location


def grouped_bar_chart(title,xlabel,ylabel,df,group_by,xplot,yplot,field):
    # group by n variables
    barplot = df.groupby(group_by, as_index=False).count()
    plt.figure(figsize=(12, 6), tight_layout=True)
    ax = sns.barplot(x=barplot[xplot], y=barplot[yplot],
                     hue=barplot[field], palette='pastel')
    ax.set(title=title,
           xlabel=xlabel, ylabel=ylabel)
    ax.legend(title=title, title_fontsize='13', loc='upper right')
    graph_image_location = plt.savefig(f'{IMAGE_PATH}/{time_stamp}_bar_plot.png', bbox_inches='tight')
    return graph_image_location


# def pie_chart():
#     # pie chart
#     piechart = df_fifa21[df_fifa21['club_name'] == 'Chelsea']
#     piechart = piechart.sort_values('value_eur', ascending=False)[
#         ['short_name', 'value_eur']]
#     piechart = piechart[:11]
#     colors = sns.color_palette('pastel')
#     plt.figure(figsize=(7, 6), tight_layout=True)
#     explode_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.2]
#     plt.pie(piechart['value_eur'], labels=piechart['short_name'], autopct='%.0f %%', explode=explode_list, pctdistance=.7,
#             colors=colors, shadow=True)
#     plt.title('Chelsea', weight='bold')
#     # plt.show()
#     plt.savefig(f'images/{time_stamp}_pie.png', bbox_inches='tight')
#     # document.add_picture(f'images/{time_stamp}_pie.png')
#     # document.save(f'docs/{time_stamp}.docx')
#     # convert("test.docx")
   



