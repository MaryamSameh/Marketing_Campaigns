import pandas as pd 
import plotly.express as px 
import streamlit as st 
import plotly.graph_objects as go

# Read dataframe 
df = pd.read_csv('Cleaned-Marketing.csv')

# Streamlit app title
st.header('Marketing Campaigns Dashboard')

# Create tabs
data, customers_demographics,Income,Amount_spending,Sales_channels = st.tabs(['Data', 'Customers Demographics','Income$',
                                                                              "Products'Spending","Sales Channels"])
viridis_colors = px.colors.sequential.Viridis

with data:
    st.header('Raw Data')
    st.write(df)  # Display raw data in a simple table

with customers_demographics:
    st.header('Customers Demographics')
    
    
    # Customer Age Distribution
    st.subheader('Customer Age Distribution')
    age_counts = df['age'].value_counts().sort_index()
    fig_age = px.bar(x=age_counts.index, y=age_counts.values,
                     labels={'x': 'age', 'y': 'Number of Customers'},
                     title='Customer Count by Age',text_auto=True,color_continuous_scale=viridis_colors,color=age_counts.index)
    fig_age.update_layout(title_font_size=20,xaxis_title_font_size=16,yaxis_title_font_size=16,font=dict(size=20))
    st.plotly_chart(fig_age)
    
    # Marital Status
    st.subheader('Marital Status')
    marital_counts = df['marital_status'].value_counts().sort_values(ascending=False)
    fig_marital = px.pie(values=marital_counts.values, names=marital_counts.index,
                         title='Marital Status Distribution',color_discrete_sequence=viridis_colors,color=marital_counts.values)
    st.plotly_chart(fig_marital)

    #Marital_status  bar
    marital_counts = df['marital_status'].value_counts()
    st.subheader('Marital Status Distribution (Bar)')
    df_counts = pd.DataFrame({'marital_status': marital_counts.index, 'count': marital_counts.values})
    fig_marital_bar = px.bar(df_counts, x='marital_status', y='count',title='Marital Status Distribution',
                            color='count',color_continuous_scale=viridis_colors,text_auto=True,
                                         labels={'marital_status': 'Marital Status', 'count': 'Count'})

                                         
    fig_marital_bar.update_layout(title_font_size=20,xaxis_title_font_size=16,yaxis_title_font_size=16,
        font=dict(size=12))
    st.plotly_chart(fig_marital_bar)

    
    # Education Level
    st.subheader('Education Level')
    education_counts = df['education'].value_counts()
    df_education_counts = pd.DataFrame({'education': education_counts.index, 'count': education_counts.values})
    fig_education = px.bar(df_education_counts,x='education', y='count',color = 'count',
                           labels={'x': 'Education Level', 'count': 'Number of Customers'},
                           title='Customer Count by Education Level', text_auto=True,color_continuous_scale=viridis_colors)
    
    fig_education.update_layout(title_font_size=20,xaxis_title_font_size=16,yaxis_title_font_size=16,font=dict(size=12))
    st.plotly_chart(fig_education)

    
    # Country Distribution
    st.subheader('Customers Countries')
    country_counts = df['country'].value_counts()
    df_country_counts = pd.DataFrame({'country': country_counts.index, 'count': country_counts.values})
    fig_country = px.bar(df_country_counts,x='country', y='count',color='count',
                         labels={'x': 'Country', 'y': 'Number of Customers'},
                         title='Customer Count by Country', text_auto=True,color_continuous_scale=viridis_colors)
    st.plotly_chart(fig_country)
    
with Income:
    
    st.header('Income Analysis')
    
    # Group by age and calculate average income
    st.subheader('Average Income by Ages_Group')
    age_bins = [0, 20, 30, 40, 50, 60, 70,80,90,100]
    age_labels = ['0-20', '20-30', '30-40', '40-50', '50-60', '60-70','70-80','80-90','90-100']
    df['age_group'] = pd.cut(df['age'], bins=age_bins, labels=age_labels, right=False)
    grouped_age = df.groupby('age_group')['income$'].mean().reset_index()
    grouped_age_sorted = grouped_age.sort_values(by='income$', ascending=False)
    fig_age_income = px.bar(grouped_age_sorted, x='age_group', y='income$',
                            labels={'age_group': 'Age_Group', 'income$': 'Average Income$'},
                            title='Average Income by Age_Group',
                            color='income$',text_auto=True,
                            color_continuous_scale=viridis_colors)
    fig_age_income.update_layout(title_font_size=20,xaxis_title_font_size=16,yaxis_title_font_size=16,font=dict(size=20))
    st.plotly_chart(fig_age_income)
    
    # Group by marital status and calculate average income
    st.subheader('Average Income by Marital Status')
    grouped_marital = df.groupby('marital_status')['income$'].mean().reset_index()
    grouped_marital_sorted = grouped_marital.sort_values(by='income$', ascending=False)
    fig_marital_income = px.bar(grouped_marital_sorted, x='marital_status', y='income$',
                                labels={'marital_status': 'Marital Status', 'income$': 'Average Income$'},
                                title='Average Income by Marital Status',
                                color='income$',
                                color_continuous_scale=viridis_colors,text_auto=True)
    fig_marital_income.update_layout(title_font_size=20,xaxis_title_font_size=16,yaxis_title_font_size=16,font=dict(size=20))
    st.plotly_chart(fig_marital_income)
    
    # Group by education and calculate average income
    st.subheader('Average Income by Education Level')
    grouped_education = df.groupby('education')['income$'].mean().reset_index()
    grouped_education_sorted = grouped_education.sort_values(by='income$', ascending=False)
    fig_education_income = px.bar(grouped_education_sorted, x='education', y='income$',
                                  labels={'education': 'Education Level', 'income$': 'Average Income'},
                                  title='Average Income by Education Level',
                                  color='income$',
                                  color_continuous_scale=viridis_colors,text_auto=True)
    fig_education_income.update_layout(title_font_size=20,xaxis_title_font_size=16,yaxis_title_font_size=16,font=dict(size=20))
    st.plotly_chart(fig_education_income)
    
    # Group by kidhome and calculate average income
    st.subheader('Average Income by kidHome Children')
    grouped_kidhome = df.groupby('kidhome')['income$'].mean().reset_index().astype(str)
    fig_kidhome_income = px.bar(grouped_kidhome, x='kidhome', y='income$',
                                labels={'kidhome': 'Number of Children at Home', 'income$': 'Average Income'},
                                title='Average Income by Number of Children at Home',
                                color='kidhome',
                                color_continuous_scale=viridis_colors,text_auto=True)
    fig_kidhome_income.update_layout(title_font_size=20,xaxis_title_font_size=16,yaxis_title_font_size=16,font=dict(size=20))
    st.plotly_chart(fig_kidhome_income)
    
    # Group by teenhome and calculate average income
    st.subheader('Average Income by teenHome Children')
    grouped_teenhome = df.groupby('teenhome')['income$'].mean().reset_index().astype(str)
    grouped_teenhome_sorted = grouped_teenhome.sort_values(by='income$', ascending=False)
    fig_teenhome_income = px.bar(grouped_teenhome_sorted, x='teenhome', y='income$',
                                 labels={'teenhome': 'Number of Teenagers at Home', 'income$': 'Average Income'},
                                 title='Average Income by Number of Teenagers at Home',
                                 color='teenhome',
                                 color_continuous_scale=viridis_colors,text_auto=True)
    fig_teenhome_income.update_layout(title_font_size=20,xaxis_title_font_size=16,yaxis_title_font_size=16,font=dict(size=20))
    st.plotly_chart(fig_teenhome_income)  

    # Group by country and calculate average income
    st.subheader('Average Income by Country')
    grouped_country = df.groupby('country')['income$'].mean().reset_index()
    grouped_country_sorted = grouped_country.sort_values(by='income$', ascending=False)
    fig_country_income = px.bar(grouped_country_sorted, x='country', y='income$',
                                  labels={'country': 'Countries', 'income$': 'Average Income'},
                                  title='Average Income by Countries',
                                  color='income$',color_continuous_scale=viridis_colors,text_auto=True)
    fig_education_income.update_layout(title_font_size=20,xaxis_title_font_size=16,yaxis_title_font_size=16,font=dict(size=20))
    st.plotly_chart(fig_country_income)

#Total amount spending for each Product
with Amount_spending:
    st.header('Amount Spending Analysis')

    # Define product categories
    product_columns = {
        'Wines': 'mntwines',
        'Fruits': 'mntfruits',
        'Meat Products': 'mntmeatproducts',
        'Fish Products': 'mntfishproducts',
        'Sweet Products': 'mntsweetproducts',
        'Gold Products': 'mntgoldprods'
    }

    # Radio button for selecting products
    st.subheader('Select Products')
    selected_product = st.radio('Show Amount Spent on', list(product_columns.keys()))

    # Plot selected product in one visualization
    if selected_product:
        product_column = product_columns[selected_product]
        total_spent_df = df[[product_column]].sum().reset_index()
        total_spent_df.columns = ['Product', 'Total Amount Spent']
        fig_product = px.bar(total_spent_df, x='Product', y='Total Amount Spent',
                             labels={'Product': 'Product', 'Total Amount Spent': 'Total Amount Spent'},
                             title=f'Total Amount Spent on {selected_product}', text_auto=True,
                             color='Total Amount Spent', color_continuous_scale=viridis_colors)
        fig_product.update_layout(title_font_size=20, xaxis_title_font_size=25, yaxis_title_font_size=16, font=dict(size=20))
        st.plotly_chart(fig_product)

    # Amount spent by marital status
    st.subheader('Amount Spent by Marital Status')
    marital_status_data = df.groupby('marital_status')[product_column].sum().reset_index()
    marital_status_data_sorted = marital_status_data.sort_values(by=product_column, ascending=False)
    fig_marital_status = px.bar(marital_status_data_sorted, x='marital_status', y=product_column,
                                labels={'marital_status': 'Marital Status', product_column: 'Amount Spent'},
                                title=f'Amount Spent on {selected_product} by Marital Status', text_auto=True,
                                color=product_column, color_continuous_scale=viridis_colors)
    st.plotly_chart(fig_marital_status)

    # Amount spent by education
    st.subheader('Amount Spent by Education Level')
    education_data = df.groupby('education')[product_column].sum().reset_index()
    education_data_sorted = education_data.sort_values(by=product_column, ascending=False)
    fig_education = px.bar(education_data_sorted, x='education', y=product_column,
                           labels={'education': 'Education Level', product_column: 'Total Amount Spent'},
                           title=f'Total Amount Spent on {selected_product} by Education Level', text_auto=True,
                           color=product_column, color_continuous_scale=viridis_colors)
    fig_education.update_layout(title_font_size=20, xaxis_title_font_size=25, yaxis_title_font_size=16, font=dict(size=20))
    st.plotly_chart(fig_education)

    
    # Amount spent by age group
    st.subheader('Amount Spent by Age Group')
    age_bins = [0, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    age_labels = ['0-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80-90', '90-100']
    df['age_group'] = pd.cut(df['age'], bins=age_bins, labels=age_labels, right=False)
    age_group_data = df.groupby('age_group')[product_column].sum().reset_index()
    age_group_data_sorted = age_group_data.sort_values(by='age_group', ascending=False)
    fig = px.bar(age_group_data_sorted, x='age_group',y=product_column, color=product_column, color_continuous_scale=viridis_colors)
    fig.update_layout(title_font_size=20, xaxis_title_font_size=25, yaxis_title_font_size=16, font=dict(size=20))
    st.plotly_chart(fig)

with Sales_channels:
    
    st.sidebar.header('Sales Channel Selection')
    selected_channel = st.sidebar.radio('Select Sales Channel', ['Store Purchases', 'Web Purchases', 'Catalog Purchases', 'Deals Purchases'])

# Define sales channels mapping
    sales_channels = {
        
       'Store Purchases': 'numstorepurchases',
       'Web Purchases': 'numwebpurchases',
       'Catalog Purchases': 'numcatalogpurchases',
       'Deals Purchases': 'numdealspurchases'
}

    sales_channel = sales_channels[selected_channel]

# Header for sales channels analysis
    st.header('Sales Channels Analysis')

# Count of selected sales channel by marital status
    st.subheader(f'Count of {selected_channel} by Marital Status')
    marital_status_data = df.groupby('marital_status')[sales_channel].sum().reset_index()
    marital_status_data_sorted = marital_status_data.sort_values(by=sales_channel, ascending=False)
    fig_marital_status = px.bar(marital_status_data_sorted, x='marital_status', y=sales_channel,
                            labels={'marital_status': 'Marital Status', sales_channel: 'Count'}, text_auto=True,
                            title=f'Count of {selected_channel} by Marital Status', color=sales_channel, color_continuous_scale='viridis')
    st.plotly_chart(fig_marital_status)

# Count of selected sales channel by education level 
    st.subheader(f'Count of {selected_channel} by Education Level')
    education_data = df.groupby('education')[sales_channel].sum().reset_index()
    education_data_sorted = education_data.sort_values(by=sales_channel, ascending=False)
    fig_education = px.bar(education_data_sorted, x='education', y=sales_channel,
                       labels={'education': 'Education Level', sales_channel: 'Count'}, text_auto=True,
                       title=f'Count of {selected_channel} by Education Level', color=sales_channel, color_continuous_scale='viridis')
    st.plotly_chart(fig_education)

# Count of selected sales channel by age group
    st.subheader(f'Count of {selected_channel} by Age Group')
    age_group_data = df.groupby('age_group')[sales_channel].sum().reset_index()
    age_group_data_sorted = age_group_data.sort_values(by='age_group', ascending=False)
    fig_age_group = px.bar(age_group_data_sorted, x='age_group', y=sales_channel,
                       labels={'age_group': 'Age Group', sales_channel: 'Count'}, text_auto=True,
                       title=f'Count of {selected_channel} by Age Group', color=sales_channel, color_continuous_scale='viridis')
    st.plotly_chart(fig_age_group)

# Count of selected sales channel by kidhome
    st.subheader(f'Count of {selected_channel} by Number of Children at Home (Kidhome)')
    kidhome_data = df.groupby('kidhome')[sales_channel].sum().reset_index()
    kidhome_data_sorted = kidhome_data.sort_values(by='kidhome', ascending=False)
    fig_kidhome = px.bar(kidhome_data_sorted, x='kidhome', y=sales_channel,
                     labels={'kidhome': 'Number of Children at Home', sales_channel: 'Count'}, text_auto=True,
                     title=f'Count of {selected_channel} by Number of Children at Home (Kidhome)',
                     color='kidhome', color_continuous_scale='viridis')
    st.plotly_chart(fig_kidhome)

# Count of selected sales channel by teenhome
    st.subheader(f'Count of {selected_channel} by Number of Teenagers at Home (Teenhome)')
    teenhome_data = df.groupby('teenhome')[sales_channel].sum().reset_index()
    teenhome_data_sorted = teenhome_data.sort_values(by='teenhome', ascending=False)
    fig_teenhome = px.bar(teenhome_data_sorted, x='teenhome', y=sales_channel,
                      labels={'teenhome': 'Number of Teenagers at Home', sales_channel: 'Count'}, text_auto=True,
                      title=f'Count of {selected_channel} by Number of Teenagers at Home (Teenhome)',
                      color='teenhome', color_continuous_scale='viridis')
    st.plotly_chart(fig_teenhome)
    
    
