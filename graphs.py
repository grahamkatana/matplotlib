import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from docx import Document
from docx2pdf import convert
import time

time_stamp = int(time.time())

document = Document()
paragraph = document.add_paragraph("Printing images to a file")

# set global graph styles
sns.set_style('darkgrid')
plt.rc('axes', titlesize=18)
plt.rc('axes', labelsize=14)
plt.rc('ytick', labelsize=13)
plt.rc('xtick', labelsize=13)
plt.rc('legend', fontsize=13)
plt.rc('font', size=13)

# figure sizes
plt.figure(figsize=(8, 4), tight_layout=True)

df_fifa21 = pd.read_csv('data/players_20.csv')
country = ['United States', 'Canada', 'England', 'Brazil', 'Argentina']
df_country = df_fifa21[df_fifa21['nationality'].isin(country)]

barplot = df_country.groupby(['nationality'], as_index=False).mean()[
    ['nationality', 'overall']]


# use matplotlib to plot
# plt.figure(figsize=(8,4), tight_layout=True)
# colors = sns.color_palette('pastel')
# plt.bar(barplot['nationality'], barplot['overall'], color=colors[:5])
# plt.xlabel('Nationality')
# plt.ylabel('Average Rating')
# plt.title('Barplot')
# plt.show()


# use seaborn
def bar_chart():
    new_df = pd.concat(
        [df_country[df_country['nationality'] == 'Argentina'][:20],
         df_country[df_country['nationality'] == 'Brazil'][:20],
         df_country[df_country['nationality'] == 'England'][:20],
         df_country[df_country['nationality'] == 'Canada'][:20],
         df_country[df_country['nationality'] == 'United States'][:20]]
    )
    barplot = new_df.groupby(['nationality'], as_index=False).mean()[
        ['nationality', 'overall']]

    plt.figure(figsize=(8, 4), tight_layout=True)
    ax = sns.barplot(x=barplot['nationality'],
                     y=barplot['overall'], palette='pastel', ci=None)
    ax.set(title='Barplot', xlabel='Nationality', ylabel='Average Rating')
    # plt.show()
    plt.savefig(f'images/{time_stamp}_bar.png', bbox_inches='tight')
    document.add_picture(f'images/{time_stamp}_bar.png')


def grouped_bar_chart():
    # group by n variables
    barplot = df_country[df_country['league_name'].isin(
        ['Spain Primera Division', 'Italian Serie A', 'German 1. Bundesliga'])]
    barplot = barplot.groupby(
        ['nationality', 'league_name'], as_index=False).count()
    plt.figure(figsize=(12, 6), tight_layout=True)
    ax = sns.barplot(x=barplot['nationality'], y=barplot['sofifa_id'],
                     hue=barplot['league_name'], palette='pastel')
    ax.set(title='Nº of Players outside of domestic league',
           xlabel='Country', ylabel='Count')
    ax.legend(title='League', title_fontsize='13', loc='upper right')
    # plt.show()
    plt.savefig(f'images/{time_stamp}_bar_plot.png', bbox_inches='tight')
    document.add_picture(f'images/{time_stamp}_bar_plot.png')


def pie_chart():
    # pie chart
    piechart = df_fifa21[df_fifa21['club_name'] == 'Chelsea']
    piechart = piechart.sort_values('value_eur', ascending=False)[
        ['short_name', 'value_eur']]
    piechart = piechart[:11]
    colors = sns.color_palette('pastel')
    plt.figure(figsize=(7, 6), tight_layout=True)
    explode_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.2]
    plt.pie(piechart['value_eur'], labels=piechart['short_name'], autopct='%.0f %%', explode=explode_list, pctdistance=.7,
            colors=colors, shadow=True)
    plt.title('Chelsea', weight='bold')
    # plt.show()
    plt.savefig(f'images/{time_stamp}_pie.png', bbox_inches='tight')
    document.add_picture(f'images/{time_stamp}_pie.png')
    document.save(f'docs/{time_stamp}.docx')
    # convert("test.docx")
   


def init():
    bar_chart()
    grouped_bar_chart()
    pie_chart()
    convert(f"docs/{time_stamp}.docx", f"pdfs/{time_stamp}.pdf")


if __name__ == '__main__':
    init()
