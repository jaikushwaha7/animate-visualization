import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

file_path = 'populations.csv'
df = pd.read_csv(file_path)
df['Age Group'] = df['Age Group'].fillna(method='ffill')

df['Males'] = df['Males'].str.replace(',','').astype('int')
df['Females'] = df['Females'].str.replace(',','').astype('int')
df['Females']= df['Females']*-1

fig, ax =plt.subplots(figsize=(15,8))

def animate(year):
    ax.clear()
    filtered = df[df['Year']==year]
    males = plt.barh(y=filtered['Age Group'], width= filtered['Males'], color= '#00ADB5')
    females= plt.barh(y=filtered['Age Group'], width= filtered['Females'],color='#00A8D3')

    ax.set_xlim(-2_000_000, 2_000_000)
    ax.bar_label(males, padding=3, labels=[f'{round(value,-3):,}' for value in filtered['Males']])
    ax.bar_label(females, padding=3, labels=[f'{-1*round(value,-3):,}' for value in filtered['Females']])

    for edge in ['top', 'right', 'bottom', 'left']:
        ax.spines[edge].set_visible(False)
    
    ax.tick_params(left=False)
    ax.get_xaxis().set_visible(False)

    ax.legend([males, females], ["Males" , "Females"])

    ax.set_title(f'Population of Canada in {year}', size = 18, weight='bold')

animation = FuncAnimation(fig, animate, frames= range(df['Year'].min(), df['Year'].max()+1))
#animation.save('Population pyramid.gif', dpi=300, writer=PillowWriter(fps= 5))
plt.show()



