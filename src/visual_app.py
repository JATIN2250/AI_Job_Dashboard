import pandas as pd 
import plotly_express as px 
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st 
from collections import Counter
import ast

# Loading data
@st.cache_data
def load_data():
    df = pd.read_csv("Dataset//AI_job_data.csv")
    return df

df = load_data()

# Side bar fillters

st.sidebar.title('Filters')
year_filter = st.sidebar.multiselect("Select Year(s):",sorted(df['year'].unique()),default=2024)
print("\n")
industry_filter = st.sidebar.multiselect("Select industry:",options=(df['industry'].dropna().unique()),default="Education")

filterd_df = df[(df['year'].isin(year_filter)) & (df['industry'].isin(industry_filter))]


# Visualization

#1 Top 10 High-Paying Job

st.header("💼 Top 10 High-Paying Job Titles")

top_jobs=(
    filterd_df.groupby('job_title')['salary_usd']
    .mean()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig1 = px.bar(top_jobs,x='salary_usd',y='job_title',orientation='h',text='salary_usd',color='job_title')

st.plotly_chart(fig1,use_container_width=True)

st.divider()
# Top 5 hiring countries

st.header("🌍 Top 5 Hiring Company Locations")
if(year_filter and industry_filter):

    location_counts = filterd_df['company_location'].value_counts().head(5).reset_index()

    location_counts.columns = ['company_location','job_postings']

    fig2 = px.pie(location_counts,names='company_location',values='job_postings')

    st.plotly_chart(fig2,use_container_width=True)

    
else:
    fig2 = px.pie(
        names=["No data to display"],
        values=[1],
        
    )
    st.plotly_chart(fig2,use_container_width=True)

st.divider()

# Most Required Skills

st.header("🧠 Most Required Skills")

all_skills = filterd_df['required_skills'].dropna().apply(lambda x : [skill.strip().lower() for skill in x.split(',')] )

skill_list = [skill for sublist in all_skills for skill in sublist]

skill_counts = pd.DataFrame(Counter(skill_list).most_common(15),columns=['Skill','Count'])

fig3 = px.bar(skill_counts,x='Count',y='Skill',color='Skill')

st.plotly_chart(fig3)

st.divider()

# Filtered Job Count

st.header('📊 Filtered Job Count')

if not year_filter:
    st.warning("📌 Please select at least one year.")
else:
    df_year_filter = df[df['year'].isin(year_filter)]

    if industry_filter:
        filtered_df = df_year_filter[df_year_filter['industry'].isin(industry_filter)]
        selected_total = filtered_df.shape[0]
        overall_total = df_year_filter.shape[0]
        remaining_total = overall_total - selected_total
        
        industry_count = (filtered_df['industry']
        .value_counts()
        .reset_index()
        .rename(columns={'industry':'Category','count': 'Job Count'}))
         
        if remaining_total>0:

            industry_count = pd.concat([
            industry_count,
            pd.DataFrame([{
            'Category':'Other Industries',
            'Job Count': remaining_total
            }])
        ], ignore_index=True)
        






    else:
        filtered_df = df_year_filter.copy()

        selected_total = filtered_df.shape[0]
        overall_total = df_year_filter.shape[0]
        remaining_total = overall_total - selected_total

        industry_count = pd.DataFrame({
            'Category': ['All Industries'],
            'Job Count': [selected_total]
        })





    fig4 = px.pie(
        industry_count,
        names='Category',
        values = 'Job Count',
        hole = 0.5

    )
    fig4.update_traces(textinfo='label+percent',marker=dict(colors=["#00cc96","#d3d3d3"]))

    st.plotly_chart(fig4,use_container_width=True)


st.divider()

# Top hiring companies over the years

st.header("📈 Top Hiring Companies Over The Years")
if not year_filter:
    st.warning("📌Please select the filter value.")

else:
    filter_df = df[(df['year'].isin(year_filter)) & (df['industry'].isin(industry_filter))]
    grouped = filter_df.groupby(['year','company_name','industry']).size().reset_index(name='Job_Postings')
    top = grouped.groupby(['year','company_name'])['Job_Postings'].sum().reset_index().sort_values(by='Job_Postings',ascending=False)

    top_n = 10
    top = top.head(top_n)

    final_data = grouped.merge(top[['year','company_name']], on=['year','company_name'])

    fig5 = px.bar(
        final_data,
        x='company_name',
        y='Job_Postings',
         color='industry',
        animation_frame='year',
        color_discrete_sequence=px.colors.qualitative.Set2,
        height=600
    )

    fig5.update_layout(
        yaxis={'categoryorder': 'total ascending'},
        xaxis_title="Job Openings",
        yaxis_title="Company",
        bargap=0.15,
        legend_title="Industry"
    )

    st.plotly_chart(fig5,use_container_width=True)

    
st.divider()

# Experience Level vs Job Type

st.header("👥Experience Level vs Job Type")


filtered_df = df.copy()

if year_filter:
    filtered_df = filtered_df[filtered_df['year'].isin(year_filter)]

if industry_filter:
    filtered_df = filtered_df[filtered_df['industry'].isin(industry_filter)]


if filtered_df.empty:
    st.warning("No data available for the selected filters.")
else:

    grouped = (
        filtered_df
        .groupby(['experience_level', 'employment_type'])
        .size()
        .reset_index(name='Job Count')
    )


    grouped['Experience'] = grouped['experience_level'].map({
        'EN': 'Entry-level',
        'MI': 'Mid-level',
        'SE': 'Senior-level',
        'EX': 'Executive'
    })
    grouped['Employment Type'] = grouped['employment_type'].map({
        'FT': 'Full-time',
        'PT': 'Part-time',
        'CT': 'Contract',
        'FL': 'Freelance'
    })

    
    fig6 = px.bar(
        grouped,
        x='Experience',
        y='Job Count',
        color='Employment Type',
        barmode='group',
        title="🧱 Employment Types by Experience Level",
        text_auto=True,
        color_discrete_sequence=px.colors.qualitative.Set2
    )

    st.plotly_chart(fig6, use_container_width=True)




st.markdown("---")
st.header("📌 Conclusion & Key Insights")

st.markdown("""
🎯 **Key Takeaways from the Dashboard:**

- 💼 **Top Paying Job Titles** help job seekers target high-salary roles.
- 🌍 **Top Hiring Locations** show where demand is geographically concentrated.
- 🧠 **Most Required Skills** provide a guide for upskilling or career pivoting.
- 📈 **Remote Work Trends** highlight the shift toward flexible work models.
- 👥 **Experience vs Employment Types** offer insights into hiring preferences by level.
- 🏢 **Top Hiring Companies Over Time** showcase long-term opportunities and industry leaders.

---

📊 This dashboard empowers users (job seekers, recruiters, analysts) to **explore global tech job trends** interactively across years, industries, and experience levels.

🙏 **Thank you for exploring!**  
If you found this dashboard useful, consider sharing feedback or contributing more ideas.

""")




st.markdown("---")
st.header("💬 Feedback Form")

st.markdown("""
If you have suggestions or feedback about this dashboard, we'd love to hear from you!
""")

with st.form("feedback_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Feedback")

    submitted = st.form_submit_button("Send Feedback")

    if submitted:
        st.success("✅ Thank you for your feedback!")
        # Here’s where you'd POST to FormSubmit from frontend
        # Streamlit doesn’t support client-side form actions directly
        st.markdown("""
        <form action="https://formsubmit.co/jitintulswani1@gmail.com" method="POST" target="_blank">
            <input type="hidden" name="_captcha" value="false">
            <input type="hidden" name="_next" value="https://yourdomain.com/thanks">
            <input type="hidden" name="name" value='{}'>
            <input type="hidden" name="email" value='{}'>
            <input type="hidden" name="message" value='{}'>
            <button type="submit">Submit via Email</button>
        </form>
        """.format(name, email, message), unsafe_allow_html=True)
