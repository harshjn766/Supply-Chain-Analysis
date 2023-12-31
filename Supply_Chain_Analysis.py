#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import plotly.io as pio
pio.templates.default='plotly_white'


# In[3]:


data = pd.read_csv('supply_chain_data.csv')


# In[13]:


data.head()


# In[14]:


data.describe()


# ## To find the relationship between the price of products and revenue generated by them

# In[23]:


fig=px.scatter(data,x='Price',y='Revenue generated',color='Product type',hover_data=['Number of products sold'],trendline='ols')


# In[24]:


fig.show()


# ### Thus, the company derives more revenue from skincare products, and higher the price of skincare, the more revenue they generate.

# ## Sales by Product Type

# In[37]:


sales_data=data.groupby('Product type')['Number of products sold'].sum().reset_index()


# In[38]:


pie_chart=px.pie(sales_data, values='Number of products sold', names='Product type',title='Sales by Product Type',hover_data=['Number of products sold'],hole=0.5,color_discrete_sequence=px.colors.qualitative.Pastel)
pie_chart.update_traces(textposition='inside',textinfo='percent+label')
pie_chart.show()


# ### So 45% of the business comes from skincare products, 29.5% from haircare, and 25.5% from cosmetics

# ## Total revenue generated by shipping carriers:

# In[50]:


total_revenue= data.groupby('Shipping carriers')['Revenue generated'].sum().reset_index()

fig=go.Figure()

fig.add_trace(go.Bar(x=total_revenue['Shipping carriers'],
                      y=total_revenue['Revenue generated']))

fig.update_layout(title='Total revenue by shipping carrier',
                  xaxis_title='Shipping carriers',
                  yaxis_title='Revenue Genrated')
fig.show()


# ### So the company is using three carriers for transportation, and Carrier B helps the company in generating more revenue.

# ## Average Lead time and Average Manufacturing costs for all products of the company

# In[52]:


avg_lead_time=data.groupby('Product type')['Lead time'].mean().reset_index()
avg_manufacturing_cost=data.groupby('Product type')['Manufacturing costs'].mean().reset_index()
result=pd.merge(avg_lead_time,avg_manufacturing_cost,on='Product type')
result.rename(columns={'Lead time': 'Average Lead time','Manufacturing costs':'Average Manufacturing costs'},inplace='True')
print(result)


# ## Analysig SKU's

# ### There's a column in the dataset as SKUs. So SKU stand for Stock Keeping Units.They’re like special codes that help companies keep track of all the different things they have for sale 

# In[54]:


revenue_chart=px.line(data,x='SKU',y='Revenue generated',title='Revenue Generated by SKU')
revenue_chart.show()


# ## Analysing Stock Levels

# ### There's another column in the dataset as Stock Levels.Stock levels refer to the number of products a store or business has in its inventory.

# In[57]:


stock_chart=px.line(data,x='SKU',y='Stock levels',title='Stock level of each SKU')
stock_chart.show()


# ### Order Quantity of each SKU

# In[59]:


order_quantity_chart=px.bar(data,x='SKU',y='Order quantities',title='Order Quantities by eack SKU')
order_quantity_chart.show()


# ### Shipping Costs

# In[61]:


shipping_costs_chart=px.bar(data,x='Shipping carriers',y='Shipping costs',title='Shipping cost by Carrier')
shipping_costs_chart.show()


# ### In one of the above visualizations, we discovered that Carrier B helps the company in more revenue. It is also the most costly Carrier among the three. 

# ## Cost Distribution by Transportation Mode

# In[66]:


transportation_chart=px.pie(data,values='Costs',names='Transportation modes',title='Cost Distribution by Transportation Mode',hole=0.5,color_discrete_sequence=px.colors.qualitative.Pastel)
transportation_chart.show()


# ### So the company spends more on Road and Rail modes of transportation for the transportation of Goods.

# ## Analysing Defect Rate

# ### The Defect Rate in the supply chain refers to the percentage of products that have something wrong or are found broken after shipping.Let's have a look at the average defect rate of all products types:

# In[71]:


defect_rates_by_products=data.groupby('Product type')['Defect rates'].mean().reset_index()
fig = px.bar(data,x='Product type',y='Defect rates',title='Average Defect rates by product types')
fig.show()


# ### So the defect rate of skincare products is higher.

# ## Defect Rates by mode of Transportation

# In[4]:


pivot_table = pd.pivot_table(data, values='Defect rates', 
                             index=['Transportation modes'], 
                             aggfunc='mean')

transportation_chart = px.pie(values=pivot_table["Defect rates"], 
                              names=pivot_table.index, 
                              title='Defect Rates by Transportation Mode',
                              hole=0.5,
                              color_discrete_sequence=px.colors.qualitative.Pastel)
transportation_chart.show()


# In[ ]:




