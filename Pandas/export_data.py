
#%%
import pandas as pd



ipl = pd.read_csv('dataset/deliveries.csv')
ipl

temp_df = ipl.pivot_table(index='batsman',columns='bowling_team',values='batsman_runs',aggfunc='sum')

# excel writer for multiple files export 

with pd.ExcelWriter('temp_ipl.xlsx') as writer:
     ipl.to_excel(writer,sheet_name='sheet_1')
     temp_df.to_excel(writer,sheet_name='sheet_2')

# Exporting to the excel 

# ipl.to_excel('batsman.xlsx')



# To HTML 
# %%
#  exporting to HTML 

ipl.query('batsman_runs == 6').pivot_table(index='over',columns='ball',values='batsman_runs',aggfunc='count').to_html('batsman.html')



# TO JSOIN
#%%

ipl_json = ipl.groupby(['batting_team','batsman'])['batsman_runs'].sum().unstack().to_json('batsman.json')

# To SQL 
# %%


from sqlalchemy import create_engine

my_df = ipl.query('batsman_runs == 6').pivot_table(index='over',columns='ball',values='batsman_runs',aggfunc='count')

engine = create_engine("mysql+pymysql://root:sqlroot@localhost/session_37")

my_df.to_sql("batsman", con=engine,if_exists='append')

# %%


