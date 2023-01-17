import pandas as pd
import streamlit as st
import os
import plotly.express as px
import streamlit_authenticator as stauth
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from datetime import datetime
import sort_dataframeby_monthorweek


def cumetricasu(df):
    new_df = df.groupby(['CU','Months']).sum(['TotalUpgradeNodes', 'ASUNodes']).reset_index()
    mh_list = new_df['Months'].unique().tolist()
    mh_list.sort(key = lambda date: datetime.strptime(date, '%b'))
    MH_selected = st.selectbox(
        'Please select current Month',
        mh_list)
    print(MH_selected)
    data = new_df[new_df["Months"] == MH_selected]

    cm_mask = (new_df.Months).isin([MH_selected]) & (new_df.CU).isin(['CM'])
    cm_data_df= new_df[cm_mask]
    cm_current_mh_asu = cm_data_df['ASUNodes']
    cm_current_mh_total = cm_data_df['TotalUpgradeNodes']
    cm_current_mh_issue = cm_data_df['NonASUNodes']

    cu_mask = (new_df.Months).isin([MH_selected]) & (new_df.CU).isin(['CU'])
    cu_data_df= new_df[cu_mask]
    cu_current_mh_asu = cu_data_df['ASUNodes']
    cu_current_mh_total = cu_data_df['TotalUpgradeNodes']
    cu_current_mh_issue = cu_data_df['NonASUNodes']

    ct_mask = (new_df.Months).isin([MH_selected]) & (new_df.CU).isin(['CT'])
    ct_data_df= new_df[ct_mask]
    ct_current_mh_asu = ct_data_df['ASUNodes']
    ct_current_mh_total = ct_data_df['TotalUpgradeNodes']
    ct_current_mh_issue = ct_data_df['NonASUNodes']

    cht_mask = (new_df.Months).isin([MH_selected]) & (new_df.CU).isin(['CHT'])
    cht_data_df= new_df[cht_mask]
    cht_current_mh_asu = cht_data_df['ASUNodes']
    cht_current_mh_total = cht_data_df['TotalUpgradeNodes']
    cht_current_mh_issue = cht_data_df['NonASUNodes']

    if MH_selected != 'Jan':
        pos = mh_list.index(MH_selected)
        new_pos = pos-1
        last_MH = mh_list[new_pos]

        cm_mask = (new_df.Months).isin([last_MH]) & (new_df.CU).isin(['CM'])
        last_cm_df = new_df[cm_mask]
        cm_last_mh_asu = last_cm_df['ASUNodes']
        cm_last_mh_total = last_cm_df['TotalUpgradeNodes']
        cm_last_mh_issue = last_cm_df['NonASUNodes']

        cu_mask = (new_df.Months).isin([last_MH]) & (new_df.CU).isin(['CU'])
        last_cu_df = new_df[cu_mask]
        cu_last_mh_asu = last_cu_df['ASUNodes']
        cu_last_mh_total = last_cu_df['TotalUpgradeNodes']
        cu_last_mh_issue = last_cu_df['NonASUNodes']

        ct_mask = (new_df.Months).isin([last_MH]) & (new_df.CU).isin(['CT'])
        last_ct_df = new_df[ct_mask]
        ct_last_mh_asu = last_ct_df['ASUNodes']
        ct_last_mh_total = last_ct_df['TotalUpgradeNodes']
        ct_last_mh_issue = last_ct_df['NonASUNodes']


        cht_mask = (new_df.Months).isin([last_MH]) & (new_df.CU).isin(['CHT'])
        last_cht_df = new_df[cht_mask]
        cht_last_mh_asu = last_cht_df['ASUNodes']
        cht_last_mh_total = last_cht_df['TotalUpgradeNodes']
        cht_last_mh_issue = last_cht_df['NonASUNodes']

        if cm_current_mh_total.empty:
            cm_current_mh_total = 0
        if cm_last_mh_total.empty:
            cm_last_mh_total = 0

        if cm_current_mh_asu.empty:
            cm_current_mh_asu = 0
        if cm_last_mh_asu.empty:
            cm_last_mh_asu = 0

        if cm_current_mh_issue.empty:
            cm_current_mh_issue= 0
        if cm_last_mh_issue.empty:
            cm_last_mh_issue= 0

        if cu_current_mh_total.empty:
            cu_current_mh_total = 0
        if cu_last_mh_total.empty:
            cu_last_mh_total = 0

        if cu_current_mh_asu.empty:
            cu_current_mh_asu = 0
        if cu_last_mh_asu.empty:
            cu_last_mh_asu = 0

        if cu_current_mh_issue.empty:
            cu_current_mh_issue= 0
        if cu_last_mh_issue.empty:
            cu_last_mh_issue= 0

        if ct_current_mh_total.empty:
            ct_current_mh_total = 0
        if ct_last_mh_total.empty:
            ct_last_mh_total = 0

        if ct_current_mh_asu.empty:
            ct_current_mh_asu = 0
        if ct_last_mh_asu.empty:
            ct_last_mh_asu = 0

        if ct_current_mh_issue.empty:
            ct_current_mh_issue = 0
        if ct_last_mh_issue.empty:
            ct_last_mh_issue = 0

        if cht_current_mh_total.empty:
            cht_current_mh_total = 0
        if cht_last_mh_total.empty:
            cht_last_mh_total = 0

        if cht_current_mh_asu.empty:
            cht_current_mh_asu = 0
        if cht_last_mh_asu.empty:
            cht_last_mh_asu = 0

        if cht_current_mh_issue.empty:
            cht_current_mh_issue = 0
        if cht_last_mh_issue.empty:
            cht_last_mh_issue = 0

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.subheader('Customer Unit CM')
            st.metric(label="Number Of Total Upgrade Nodes In " + MH_selected, value=int(cm_current_mh_total), delta= int(cm_current_mh_total)-int(cm_last_mh_total))
            st.metric(label="Number Of ASU Nodes In " + MH_selected, value=int(cm_current_mh_asu), delta= int(cm_current_mh_asu)-int(cm_last_mh_asu))
            st.metric(label="Number Of Issues In " + MH_selected, value=int(cm_current_mh_issue), delta= int(cm_current_mh_issue)-int(cm_last_mh_issue))
        with col2:
            st.subheader('Customer Unit CU')
            st.metric(label="Number Of Total Upgrade Nodes In  " + MH_selected, value=int(cu_current_mh_total), delta= int(cu_current_mh_total)-int(cu_last_mh_total))
            st.metric(label="Number Of ASU Nodes In " + MH_selected, value=int(cu_current_mh_asu), delta= int(cu_current_mh_asu)-int(cu_last_mh_asu))
            st.metric(label="Number Of Issues In " + MH_selected, value=int(cu_current_mh_issue), delta= int(cu_current_mh_issue)-int(cu_last_mh_issue))
        with col3:
            st.subheader('Customer Unit CT')
            st.metric(label="Number Of Total Upgrade Nodes In " + MH_selected, value=int(ct_current_mh_total), delta= int(ct_current_mh_total)-int(ct_last_mh_total))
            st.metric(label="Number Of ASU Nodes In " + MH_selected, value=int(ct_current_mh_asu), delta= int(ct_current_mh_asu)-int(ct_last_mh_asu))
            st.metric(label="Number Of Issues In " + MH_selected, value=int(ct_current_mh_issue), delta= int(ct_current_mh_issue)-int(ct_last_mh_issue))
        with col4:
            st.subheader('Customer Unit CHT')
            st.metric(label="Number Of Total Upgrade Nodes In " + MH_selected, value=int(cht_current_mh_total), delta= int(cht_current_mh_total)-int(cht_last_mh_total))
            st.metric(label="Number Of ASU Nodes In " + MH_selected, value=int(cht_current_mh_asu), delta= int(cht_current_mh_asu)-int(cht_last_mh_asu))
            st.metric(label="Number Of Issues In " + MH_selected, value=int(cht_current_mh_issue), delta= int(cht_current_mh_issue)-int(cht_last_mh_issue))
    else:
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.subheader('China Mobile')
            st.metric(label="Number Of Total Upgrade Nodes In " + MH_selected, value=int(cm_current_mh_total), delta="0")
            st.metric(label="Number Of ASU Nodes In " + MH_selected, value=int(cm_current_mh_asu), delta="0")
            st.metric(label="Number Of Issues In " + MH_selected, value=int(cm_current_mh_issue), delta="0")
        with col2:
            st.subheader('China Unicom')
            st.metric(label="Number Of Total Upgrade Nodes In " + MH_selected, value=int(cu_current_mh_total), delta="0")
            st.metric(label="Number Of ASU Nodes In " + MH_selected, value=int(cu_current_mh_asu), delta="0")
            st.metric(label="Number Of Issues In " + MH_selected, value=int(cu_current_mh_issue), delta="0")
        with col3:
            st.subheader('China Telecom')
            if (len(ct_current_mh_total)) == 0:
                ct_current_mh_total = 0
            if (len(ct_current_mh_asu)) == 0:
                ct_current_mh_asu = 0
            if (len(ct_current_mh_issue)) == 0:
                ct_current_mh_issue =0
            st.metric(label="Number Of Total Upgrade Nodes In " + MH_selected, value=int(ct_current_mh_total), delta="0")
            st.metric(label="Number Of ASU Nodes In " + MH_selected, value=int(ct_current_mh_asu), delta="0")
            st.metric(label="Number Of Issues In " + MH_selected, value=int(ct_current_mh_issue), delta="0")
        with col4:
            st.subheader('ChungHwa Telcom')
            st.metric(label="Number Of Total Upgrade Nodes In " + MH_selected, value=int(cht_current_mh_total), delta="0")
            st.metric(label="Number Of ASU Nodes In " + MH_selected, value=int(cht_current_mh_asu), delta="0")
            st.metric(label="Number Of Issues In " + MH_selected, value=int(cht_current_mh_issue), delta="0")
    st.markdown("""---""")





def rangesumasu(df):
    st.subheader(":bar_chart: The Summary Of Total Upgrade/ASU Nodes")
    new_df = df.groupby(['CU','Months']).sum(['TotalUpgradeNodes', 'ASUNodes']).reset_index()
    monthrange = (new_df['Months']).unique().tolist()
    #monthrange.sort(key = lambda date: datetime.strptime(date, '%b'))
    monthrange.sort(key = lambda date: datetime.strptime(date, '%b'))
    print(monthrange)
    start_mon, end_mon = st.select_slider(
        'Select a range of Month ',
        options=monthrange,
        value=('Jan', 'Feb'))
    st.write('You selected month range between', start_mon, 'and', end_mon)

    #start = 'Jan'
    #end = int(end_week.split('W')[1])
    mon_list = []
    if start_mon == end_mon:
        position = monthrange.index(end_mon)
        print(position)
        mon_list.append(monthrange[position])
        print(mon_list)
    else:
        position1 = monthrange.index(start_mon)
        position2 = monthrange.index(end_mon)
        mon_list = monthrange[position1:position2+1]
        print(mon_list)


    mon_list.sort(key = lambda date: datetime.strptime(date, '%b'))

    range_totalup = new_df.query('Months ==' + str(mon_list)).TotalUpgradeNodes.sum()
    range_asu = new_df.query('Months ==' + str(mon_list)).ASUNodes.sum()
    range_rate = range_asu/range_totalup
    range_non_asu = range_totalup - range_asu


    colum1, colum2, colum3, colum4 = st.columns(4)
    with colum1:
        st.caption("Total Upgrade Nodes:")
        st.subheader(f"{range_totalup}")
    with colum2:
        st.caption("Total ASU Nodes:")
        st.subheader(f"{range_asu}")
    with colum3:
        st.caption("ASU Usage Rate:")
        st.subheader('{:.2%}'.format(range_rate))
    with colum4:
        st.caption("Issue counts:")
        st.subheader(f"{range_non_asu}")



    mask = (new_df.Months).isin(mon_list)
    new_df = new_df[mask]

    new_df = sort_dataframeby_monthorweek.Sort_Dataframeby_Month(df=new_df,monthcolumnname='Months')
    print(new_df)
    data_total_upgrade = {
        'Month': new_df['Months'],
        'Count': new_df['TotalUpgradeNodes'],
        'CU': new_df['CU'],
        'Category': 'TotalUpgradeNodes'
    }

    data_asu_upgrade = {
        'Month': new_df['Months'],
        'Count': new_df['ASUNodes'],
        'CU': new_df['CU'],
        'Category': 'ASUNodes'
    }

    Count = len(data_total_upgrade['Count'])
    index_para =[]
    for i in range(Count):
        index_para.append(i)


    df_total_up = pd.DataFrame(data_total_upgrade,index=index_para,columns=['Month','Count','CU','Category'])
    df_asu = pd.DataFrame(data_asu_upgrade,index=index_para,columns=['Month','Count','CU','Category'])
    frames = [df_total_up,df_asu]
    result = pd.concat(frames).reset_index(drop=True)


    data_cm = result[result["CU"] == 'CM']
    data_cu = result[result["CU"] == 'CU']
    data_ct = result[result["CU"] == 'CT']
    data_cht = result[result["CU"] == 'CHT']

    data_cm_tun = data_cm[data_cm["Category"] == "TotalUpgradeNodes"]
    data_cm_tun = data_cm_tun['Count'].sum()

    data_cm_an = data_cm[data_cm["Category"] == "ASUNodes"]
    data_cm_an = data_cm_an['Count'].sum()

    data_cu_tun = data_cu[data_cu["Category"] == "TotalUpgradeNodes"]
    data_cu_tun = data_cu_tun['Count'].sum()

    data_cu_an = data_cu[data_cu["Category"] == "ASUNodes"]
    data_cu_an = data_cu_an['Count'].sum()

    data_ct_tun = data_ct[data_ct["Category"] == "TotalUpgradeNodes"]
    data_ct_tun = data_ct_tun['Count'].sum()

    data_ct_an = data_ct[data_ct["Category"] == "ASUNodes"]
    data_ct_an = data_ct_an['Count'].sum()


    data_cht_tun = data_cht[data_cht["Category"] == "TotalUpgradeNodes"]
    data_cht_tun = data_cht_tun['Count'].sum()

    data_cht_an = data_cht[data_cht["Category"] == "ASUNodes"]
    data_cht_an = data_cht_an['Count'].sum()
    st.markdown("""---""")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.caption("China Mobile Summary:")
        st.subheader(f"Total Nodes: {data_cm_tun}")
        st.subheader(f"ASU Nodes: {data_cm_an}")
        st.subheader("ASU Usage Rate: {:.2%}".format(data_cm_an/data_cm_tun))
    with c2:
        st.caption("China Unicom Summary:")
        st.subheader(f"Total Nodes: {data_cu_tun}")
        st.subheader(f"ASU Nodes: {data_cu_an}")
        st.subheader("ASU Usage Rate: {:.2%}".format(data_cu_an/data_cu_tun))
    with c3:
        st.caption("China Telecom Summary:")
        st.subheader(f"Total Nodes: {data_ct_tun}")
        st.subheader(f"ASU Nodes: {data_ct_an}")
        st.subheader("ASU Usage Rate: {:.2%}".format(data_ct_an/data_ct_tun))
    with c4:
        st.caption("ChungHwa Telecom Summary:")
        st.subheader(f"Total Nodes: {data_cht_tun}")
        st.subheader(f"ASU Nodes: {data_cht_an}")
        st.subheader("ASU Usage Rate: {:.2%}".format(data_cht_an/data_cht_tun))
    st.markdown("""---""")


    groupfig = px.bar(result, x="Category", y="Count", facet_col="Month", color="CU", text="Count")
    groupfig.layout.width = 1200
    groupfig.layout.height = 700

    col1, col2, col3 = st.columns([1,6,1])
    with col1:
        st.write("")
    with col2:
        st.plotly_chart(groupfig)
    with col3:
        st.write("")


    st.markdown("""---""")

    st.subheader('Compare With Last Month')
    cumetricasu(df)

    #st.subheader('Non-ASU Summary')


    reason_df = df.groupby(['City','Months','NonASUReason']).sum(['NonASUNodes']).reset_index()
    mn_list = reason_df['Months'].unique().tolist()
    mn_list.sort(key = lambda date: datetime.strptime(date, '%b'))
    print(mn_list)
    reason_df.index = reason_df['Months']
    reason_df = reason_df.loc[mn_list]


    non_df = (reason_df.query("NonASUNodes != 0")).reset_index(drop=True)

    st.subheader("Non-ASU By City And Type")


    reasonfig = px.scatter(non_df, x="City", y="NonASUNodes", size="NonASUNodes", color="Months",
                            size_max=60, title='Non-ASU By City(From Jan to Now)')
    reasonfig.update_layout()

    fig = px.pie(non_df.query("NonASUNodes != 0"), values='NonASUNodes', names='NonASUReason', title='Non-ASU By Type (From Jan to Now)')
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(reasonfig)
    with col2:
        st.plotly_chart(fig)



def checkbycu(df):
    CU = df['CU'].unique().tolist()
    Site = df['Site'].unique().tolist()

    Month = df['Months'].unique().tolist()
    Month.sort(key = lambda date: datetime.strptime(date, '%b'))

    df['ASUusagerate'] = df['ASUusagerate'].apply(lambda x: format(x, '.2'))
    print(df['ASUusagerate'])
    cu_selection = st.sidebar.multiselect('CU:', CU, default=None)
    site_selection = st.sidebar.multiselect('Site:', Site, default=None)
    MH_selection = st.sidebar.multiselect('Month:', Month, default=None)


    # filter
    mask = (df['CU'].isin(cu_selection)) & (df['Site'].isin(site_selection)) & (df['TotalUpgradeNodes'] != 0) & (df['Months'].isin(MH_selection))
    number_of_result = df[mask].shape[0]
    df = df[mask]

    print(df)

    # chart
    total_upgrade= sum(df['TotalUpgradeNodes'])
    total_asu = sum(df['ASUNodes'])
    total_nonasu = sum(df['NonASUNodes'])
    if total_upgrade != 0:
        total_asu_rate = total_asu/total_upgrade
    else:
        total_asu_rate = 0



    # display the text information
    if cu_selection and site_selection:
        str_cu = ",".join(cu_selection)
        str_site = ",".join(site_selection)
        st.subheader(":bar_chart: The summary of " + str_cu + ' and Site ' + str_site)
    else:
        st.subheader(":bar_chart: The summary of " + ' ' + ' ' +' Site')

    left_column, middle_column, right_column = st.columns(3)
    with left_column:
        st.caption("Total Number Of Upgrade Nodes:")
        st.subheader(f"{total_upgrade:,}")
    with middle_column:
        st.caption("Total Number Of ASU Nodes:")
        st.subheader(f"{total_asu:,}")
    with right_column:
        st.caption("ASU Usage Rate:")
        print(total_asu_rate)
        if total_asu_rate > 0.8:
            icon = ':smile:'
        elif total_asu_rate > 0.6 and total_asu_rate < 0.8:
            icon=':disappointed:'
        else:
            icon=':sob:'
        st.subheader(f"{('{:.2%}'.format(total_asu_rate))}{icon}")

    st.markdown("""---""")


    #df.style.highlight_min(df.color='red', subset='ZTI Rate')
    st.dataframe(df.reset_index(drop=True), width=1500)

    #st.dataframe(df.reset_index(drop=True), width=1500, height=900)
    st.markdown("""---""")


    bar_chart = px.histogram(df, x='City', y=['TotalUpgradeNodes','ASUNodes'],  barmode='group', title='Rollout and ASU Num')
    scatter_chart = px.scatter(df, x='City', y='ASUusagerate', color='ASUusagerate', title='ASU Rate', width=700, height=460)
    scatter_chart.update_layout(yaxis_tickformat=".2%", yaxis_range=[0,1],autotypenumbers='convert types')
    #scatter_chart.update_layout
    #bar_chart.add_trace(line_chart)

    #st.plotly_chart(pie_chart
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(bar_chart)
    with col2:
        st.plotly_chart(scatter_chart)



    st.markdown("""---""")


def rangesumzti(df):
    st.subheader(":bar_chart: The number of Rollout and ZTI nodes ")
    new_df = df.groupby(['CU','Month']).sum(['Rollout', 'ZTI']).reset_index()
    monthrange = (new_df['Month']).unique().tolist()
    new_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    monthrange.sort(key = lambda date: datetime.strptime(date, '%b'))
    print(monthrange)
    start_mon, end_mon = st.select_slider(
        'Select a range of Month ',
        options=monthrange,
        value=('Jan', 'Feb'))
    st.write('You selected month range between', start_mon, 'and', end_mon)

    #start = 'Jan'
    #end = int(end_week.split('W')[1])
    mon_list = []
    if start_mon == end_mon:
        position = monthrange.index(end_mon)
        print(position)
        mon_list.append(monthrange[position])
        print(mon_list)
    else:
        position1 = monthrange.index(start_mon)
        position2 = monthrange.index(end_mon)
        mon_list = monthrange[position1:position2+1]
        print(mon_list)

    #new_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    mon_list.sort(key = lambda date: datetime.strptime(date, '%b'))
    print(mon_list)
    range_rollout = new_df.query('Month ==' + str(mon_list)).Rollout.sum()
    print(range_rollout)
    range_zti = new_df.query('Month ==' + str(mon_list)).ZTI.sum()
    range_rate = range_zti/range_rollout
    range_issue_count = range_rollout - range_zti


    colum1, colum2, colum3, colum4 = st.columns(4)
    with colum1:
        st.caption("Total Rollout Number:")
        st.subheader(f"{range_rollout}")
    with colum2:
        st.caption("Total ZTI Number:")
        st.subheader(f"{range_zti}")
    with colum3:
        st.caption("ZTI Usage Rate:")
        st.subheader('{:.2%}'.format(range_rate))
    with colum4:
        st.caption("Issue counts:")
        st.subheader(f"{range_issue_count}")



    mask = (new_df.Month).isin(mon_list)
    new_df = new_df[mask]

    new_df = sort_dataframeby_monthorweek.Sort_Dataframeby_Month(df=new_df,monthcolumnname='Month')
    print(new_df)
    data_roll_all = {
        'Month': new_df['Month'],
        'Count': new_df['Rollout'],
        'CU': new_df['CU'],
        'Category': 'Rollout'
    }

    data_zti_all = {
        'Month': new_df['Month'],
        'Count': new_df['ZTI'],
        'CU': new_df['CU'],
        'Category': 'ZTI'
    }

    Count = len(data_roll_all['Count'])
    index_para =[]
    for i in range(Count):
        index_para.append(i)


    df_rollout = pd.DataFrame(data_roll_all,index=index_para,columns=['Month','Count','CU','Category'])
    df_zti = pd.DataFrame(data_zti_all,index=index_para,columns=['Month','Count','CU','Category'])
    frames = [df_rollout,df_zti]
    result = pd.concat(frames).reset_index(drop=True)



    data_cm = result[result["CU"] == 'CM']
    data_cu = result[result["CU"] == 'CU']
    data_ct = result[result["CU"] == 'CT']

    data_cm_tun = data_cm[data_cm["Category"] == "Rollout"]
    data_cm_tun = data_cm_tun['Count'].sum()

    data_cm_an = data_cm[data_cm["Category"] == "ZTI"]
    data_cm_an = data_cm_an['Count'].sum()

    data_cu_tun = data_cu[data_cu["Category"] == "Rollout"]
    data_cu_tun = data_cu_tun['Count'].sum()

    data_cu_an = data_cu[data_cu["Category"] == "ZTI"]
    data_cu_an = data_cu_an['Count'].sum()

    data_ct_tun = data_ct[data_ct["Category"] == "Rollout"]
    data_ct_tun = data_ct_tun['Count'].sum()

    data_ct_an = data_ct[data_ct["Category"] == "ZTI"]
    data_ct_an = data_ct_an['Count'].sum()
    st.markdown("""---""")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.caption("China Mobile Summary:")
        st.subheader(f"Total Nodes: {data_cm_tun}")
        st.subheader(f"ZTI Nodes: {data_cm_an}")
        st.subheader("ZTI Usage Rate: {:.2%}".format(data_cm_an/data_cm_tun))
    with c2:
        st.caption("China Unicom Summary:")
        st.subheader(f"Total Nodes: {data_cu_tun}")
        st.subheader(f"ZTI Nodes: {data_cu_an}")
        st.subheader("ZTI Usage Rate: {:.2%}".format(data_cu_an/data_cu_tun))
    with c3:
        st.caption("China Telecom Summary:")
        st.subheader(f"Total Nodes: {data_ct_tun}")
        st.subheader(f"ZTI Nodes: {data_ct_an}")
        st.subheader("ZTI Usage Rate: {:.2%}".format(data_ct_an/data_ct_tun))
    st.markdown("""---""")




    groupfig = px.bar(result, x="Category", y="Count", facet_col="Month", color="CU", text="Count")
    groupfig.layout.width = 1200
    groupfig.layout.height = 700

    col1, col2, col3 = st.columns([1,6,1])
    with col1:
        st.write("")
    with col2:
        st.plotly_chart(groupfig)
    with col3:
        st.write("")


    st.markdown("""---""")

    st.subheader('Compare With Last Month')
    cumetriczti(df)



def cumetriczti(df):


    new_df = df.groupby(['CU','Month']).sum(['Rollout', 'ZTI']).reset_index()
    mh_list = new_df['Month'].unique().tolist()
    mh_list.sort(key = lambda date: datetime.strptime(date, '%b'))
    MH_selected = st.selectbox(
        'Please select current Month',
        mh_list)
    print(MH_selected)
    data = new_df[new_df["Month"] == MH_selected]

    cm_mask = (new_df.Month).isin([MH_selected]) & (new_df.CU).isin(['CM'])
    cm_data_df= new_df[cm_mask]
    cm_current_mh_zti = cm_data_df['ZTI']
    cm_current_mh_Rollout = cm_data_df['Rollout']
    cm_current_mh_issue = cm_data_df['Not Use ZTI Num']

    cu_mask = (new_df.Month).isin([MH_selected]) & (new_df.CU).isin(['CU'])
    cu_data_df= new_df[cu_mask]
    cu_current_mh_zti = cu_data_df['ZTI']
    cu_current_mh_Rollout = cu_data_df['Rollout']
    cu_current_mh_issue = cu_data_df['Not Use ZTI Num']

    ct_mask = (new_df.Month).isin([MH_selected]) & (new_df.CU).isin(['CT'])
    ct_data_df= new_df[ct_mask]
    ct_current_mh_zti = ct_data_df['ZTI']
    ct_current_mh_Rollout = ct_data_df['Rollout']
    ct_current_mh_issue = ct_data_df['Not Use ZTI Num']



    if MH_selected != 'Jan':
        pos = mh_list.index(MH_selected)
        new_pos = pos-1
        last_MH = mh_list[new_pos]

        cm_mask = (new_df.Month).isin([last_MH]) & (new_df.CU).isin(['CM'])
        last_cm_df = new_df[cm_mask]
        cm_last_mh_zti = last_cm_df['ZTI']
        cm_last_mh_Rollout = last_cm_df['Rollout']
        cm_last_mh_issue = last_cm_df['Not Use ZTI Num']

        cu_mask = (new_df.Month).isin([last_MH]) & (new_df.CU).isin(['CU'])
        last_cu_df = new_df[cu_mask]
        cu_last_mh_zti = last_cu_df['ZTI']
        cu_last_mh_Rollout = last_cu_df['Rollout']
        cu_last_mh_issue = last_cu_df['Not Use ZTI Num']

        ct_mask = (new_df.Month).isin([last_MH]) & (new_df.CU).isin(['CT'])
        last_ct_df = new_df[ct_mask]
        ct_last_mh_zti = last_ct_df['ZTI']
        ct_last_mh_Rollout = last_ct_df['Rollout']
        ct_last_mh_issue = last_ct_df['Not Use ZTI Num']


        if cm_current_mh_Rollout.empty:
            cm_current_mh_Rollout =0
        if cm_last_mh_Rollout.empty:
            cm_last_mh_Rollout =0

        if cm_current_mh_zti.empty:
            cm_current_mh_zti = 0
        if cm_last_mh_zti.empty:
            cm_last_mh_zti = 0

        if cm_current_mh_issue.empty:
            cm_current_mh_zti= 0
        if cm_last_mh_issue.empty:
            cm_last_mh_zti= 0

        if cu_current_mh_Rollout.empty:
            cu_current_mh_Rollout =0
        if cu_last_mh_Rollout.empty:
            cu_last_mh_Rollout =0

        if cu_current_mh_zti.empty:
            cu_current_mh_zti = 0
        if cu_last_mh_zti.empty:
            cu_last_mh_zti = 0

        if cu_current_mh_issue.empty:
            cu_current_mh_zti= 0
        if cu_last_mh_issue.empty:
            cu_last_mh_zti= 0


        if ct_current_mh_Rollout.empty:
            ct_current_mh_Rollout =0
        if ct_last_mh_Rollout.empty:
            ct_last_mh_Rollout =0

        if ct_current_mh_zti.empty:
            ct_current_mh_zti = 0
        if ct_last_mh_zti.empty:
            ct_last_mh_zti = 0

        if ct_current_mh_issue.empty:
            ct_current_mh_issue= 0
        if ct_last_mh_issue.empty:
            ct_last_mh_issue= 0




        col1, col2, col3 = st.columns(3)
        with col1:
            st.subheader('Customer Unit China Mobile')
            st.metric(label="Number Of Rollout in " + MH_selected, value=int(cm_current_mh_Rollout), delta= int(cm_current_mh_Rollout)-int(cm_last_mh_Rollout))
            st.metric(label="Number Of ZTI in " + MH_selected, value=int(cm_current_mh_zti), delta= int(cm_current_mh_zti)-int(cm_last_mh_zti))
            st.metric(label="Number Of Issues in " + MH_selected, value=int(cm_current_mh_issue), delta= int(cm_current_mh_issue)-int(cm_last_mh_issue))
        with col2:
            st.subheader('Customer Unit China Unicom')
            st.metric(label="Number Of Rollout in " + MH_selected, value=int(cu_current_mh_Rollout), delta= int(cu_current_mh_Rollout)-int(cu_last_mh_Rollout))
            st.metric(label="Number Of ZTI in " + MH_selected, value=int(cu_current_mh_zti), delta= int(cu_current_mh_zti)-int(cu_last_mh_zti))
            st.metric(label="Number Of Issues in " + MH_selected, value=int(cu_current_mh_issue), delta= int(cu_current_mh_issue)-int(cu_last_mh_issue))
        with col3:
            st.subheader('Customer Unit China Telecom')
            st.metric(label="Number Of Rollout in " + MH_selected, value=int(ct_current_mh_Rollout), delta= int(ct_current_mh_Rollout)-int(ct_last_mh_Rollout))
            st.metric(label="Number Of ZTI in " + MH_selected, value=int(ct_current_mh_zti), delta= int(ct_current_mh_zti)-int(ct_last_mh_zti))
            st.metric(label="Number Of Issues in " + MH_selected, value=int(ct_current_mh_issue), delta= int(ct_current_mh_issue)-int(ct_last_mh_issue))


    else:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.subheader('Customer Unit China Mobile')
            st.metric(label="Number Of Rollout in " + MH_selected, value=int(cm_current_mh_Rollout), delta="0")
            st.metric(label="Number Of ZTI in " + MH_selected, value=int(cm_current_mh_zti), delta="0")
            st.metric(label="Number Of Issues in " + MH_selected, value=int(cm_current_mh_issue), delta="0")
        with col2:
            st.subheader('Customer Unit China Unicom')
            st.metric(label="Number Of Rollout in " + MH_selected, value=int(cu_current_mh_Rollout), delta="0")
            st.metric(label="Number Of ZTI in " + MH_selected, value=int(cu_current_mh_zti), delta="0")
            st.metric(label="Number Of Issues in " + MH_selected, value=int(cu_current_mh_issue), delta="0")
        with col3:
            st.subheader('Customer Unit China Telecom')
            st.metric(label="Number Of Rollout in " + MH_selected, value=int(ct_current_mh_Rollout), delta="0")
            st.metric(label="Number Of ZTI in " + MH_selected, value=int(ct_current_mh_zti), delta="0")
            st.metric(label="Number Of Issues in " + MH_selected, value=int(ct_current_mh_issue), delta="0")


    st.markdown("""---""")

def checkallzti(df):

    print("asdfasdfasdfasdfasdfasdf")
    #option = st.selectbox('Select the month to check',mn_list)

    df_nj = df[(df['Site'] == 'NJ')]
    df_bj = df[(df['Site'] == 'BJ')]
    df_cd = df[(df['Site'] == 'CD')]
    df_gz = df[(df['Site'] == 'GZ')]

    ZTI_Node_nj = sum((df_nj['ZTI']))
    ZTI_Node_bj = sum((df_bj['ZTI']))
    ZTI_Node_cd = sum((df_cd['ZTI']))
    ZTI_Node_gz = sum((df_gz['ZTI']))

    ZTI_Rollout_nj = sum(df_nj['Rollout'])
    ZTI_Rollout_bj = sum(df_bj['Rollout'])
    ZTI_Rollout_cd = sum(df_cd['Rollout'])
    ZTI_Rollout_gz = sum(df_gz['Rollout'])

    ZTI_Rate_nj = round((ZTI_Node_nj/ZTI_Rollout_nj) * 100,2)
    ZTI_Rate_bj = round((ZTI_Node_bj/ZTI_Rollout_bj) * 100,2)
    ZTI_Rate_cd = round((ZTI_Node_cd/ZTI_Rollout_cd) * 100,2)
    ZTI_Rate_gz = round((ZTI_Node_gz/ZTI_Rollout_gz) * 100,2)

    print([ZTI_Rate_nj, ZTI_Rate_bj, ZTI_Rate_cd, ZTI_Rate_gz])
    data_zti_all = {
        'Site': ['NJ', 'BJ', 'CD', 'GZ'],
        'Rate': [ZTI_Rate_nj, ZTI_Rate_bj, ZTI_Rate_cd, ZTI_Rate_gz],
        'Rollout_Nodes': [ZTI_Rollout_nj, ZTI_Rollout_bj, ZTI_Rollout_cd, ZTI_Rollout_gz],
        'ZTI_Nodes': [ZTI_Node_nj, ZTI_Node_bj, ZTI_Node_cd, ZTI_Node_gz]
    }

    data_zti_rate = {
        'Site': ['NJ', 'BJ', 'CD', 'GZ'],
        'Rate': [ZTI_Rate_nj, ZTI_Rate_bj, ZTI_Rate_cd, ZTI_Rate_gz]
    }

    df2 = pd.DataFrame(data_zti_rate,index=[1,2,3,4],columns=['Site','Rate'])
    df3 = pd.DataFrame(data_zti_all)
    subfig = make_subplots(specs=[[{"secondary_y": True}]])

    fig2 = px.scatter(df2,x="Site", y="Rate" ,labels={'Site':'Site Name','Rate':'ZTI Usage'}, color='Site', text='Rate', size='Rate')
    fig2.update_traces(yaxis="y2")
    fig3 = go.Figure(data=[
        go.Bar(x=df3['Site'], y=df3['ZTI_Nodes'], name='Num of ZTI', text=df3['ZTI_Nodes'], hovertext=df3['ZTI_Nodes']),
        go.Bar(x=df3['Site'], y=df3['Rollout_Nodes'], name='Num of rollout', text=df3['Rollout_Nodes'])
    ])
    fig3.update_traces(textfont_size=12, textangle=0, textposition='inside', cliponaxis=False)
    fig3.update_layout(barmode='group', autosize=False, width=600, height=500)

    subfig.add_traces(fig2.data + fig3.data)
    subfig.layout.xaxis.title = "Site Name"
    subfig.layout.yaxis.title = "Total Number Of Rollout and ZTI Nodes"
    subfig.layout.yaxis2.type = "log"
    subfig.layout.yaxis2.title = "ZTI Usage Rate(%)"
    subfig.layout.width = 950
    subfig.layout.height = 600
    #st.plotly_chart(subfig)


    total_Transmission = sum(df['Transmission'])
    total_GNB = sum(df['GNB'])
    total_ENM = sum(df['ENM'])
    total_Others = sum(df['Others'])

    issue_category = {
        'Category': ['Transmission', 'GNB', 'ENM', 'Others'],
        'Qty': [total_Transmission, total_GNB, total_ENM, total_Others]
    }

    df2 = pd.DataFrame(issue_category,index=[1,2,3,4],columns=['Category','Qty'])
    fig = px.pie(df2, values='Qty', names='Category')
    fig.layout.width = 600
    fig.layout.height = 700

    st.subheader(':information_source: Site Information')
    new_df = df.groupby(['CU','Site','Month']).sum(['Rollout', 'ZTI']).reset_index()
    mn_list = new_df['Month'].unique().tolist()
    mn_list.sort(key = lambda date: datetime.strptime(date, '%b'))
    option = st.selectbox(
        'Select the month to check',mn_list)

    print(new_df)
    nj_df = new_df[(new_df.Month == option )&(new_df.Site =='NJ')]
    bj_df = new_df[(new_df['Month']==option )&(new_df['Site'] =='BJ')]
    cd_df = new_df[(new_df['Month']==option )&(new_df['Site'] =='CD')]
    gz_df = new_df[(new_df['Month']==option )&(new_df['Site'] =='GZ')]

    nj_df_rollout = sum(nj_df['Rollout'])
    nj_df_zti = sum(nj_df['ZTI'])
    if nj_df_rollout != 0:
        nj_rate = round((nj_df_zti/nj_df_rollout) * 100,2)
    else:
        nj_rate = 0.00

    bj_df_rollout = sum(bj_df['Rollout'])
    bj_df_zti = sum(bj_df['ZTI'])
    if bj_df_rollout != 0:
        bj_rate = round((bj_df_zti/bj_df_rollout) * 100,2)
    else:
        bj_rate = 0.00

    cd_df_rollout = sum(cd_df['Rollout'])
    cd_df_zti = sum(cd_df['ZTI'])
    if cd_df_rollout != 0:
        cd_rate = round((cd_df_zti/cd_df_rollout) * 100,2)
    else:
        cd_rate = 0.00

    gz_df_rollout = sum(gz_df['Rollout'])
    gz_df_zti = sum(gz_df['ZTI'])
    if gz_df_rollout != 0:
        gz_rate = round((gz_df_zti/gz_df_rollout) * 100,2)
    else:
        gz_rate = 0.00

    colum1, colum2, colum3, colum4 = st.columns(4)

    with colum1:
        st.caption("Site NJ Summary:")
        st.metric("Number Of Rollout",f"{nj_df_rollout}",'')
        st.metric("Number Of ZTI",f"{nj_df_zti}",'')
        st.metric("ZTI Rate" ,f"{nj_rate}"+"%",'')

    with colum2:
        st.caption("Site BJ Summary:")
        st.metric("Number Of Rollout",f"{bj_df_rollout}",'')
        st.metric("Number Of ZTI",f"{bj_df_zti}",'')
        st.metric("ZTI Rate" ,f"{bj_rate}"+"%",'')

    with colum3:
        st.caption("Site CD Summary:")
        st.metric("Number Of Rollout",f"{cd_df_rollout}",'')
        st.metric("Number Of ZTI",f"{cd_df_zti}",'')
        st.metric("ZTI Rate" ,f"{cd_rate}"+"%",'')

    with colum4:
        st.caption("Site GZ Summary:")
        st.metric("Number Of Rollout",f"{gz_df_rollout}",'')
        st.metric("Number Of ZTI",f"{gz_df_zti}",'')
        st.metric("ZTI Rate" ,f"{gz_rate}"+"%",'')



    #with colum3:
    #    st.caption("ZTI Usage Rate:")
    #    st.subheader('{:.2%}'.format(range_rate))
    #with colum4:
    #    st.caption("Issue counts:")
    #    st.subheader(f"{range_issue_count}")


    st.markdown("""---""")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader(':black_medium_square: Site Summary Chart')
        st.caption("The Total Rollout/ZTI/Rate Summary Of 4 Sites ")
        st.caption("From Jan To Now")
        st.plotly_chart(subfig)
    with col2:
        st.write('')
    with col3:
        st.subheader(':black_medium_square: Non-ZTI Category')
        st.caption("The Total Number Of Non-ZTI")
        st.caption("From Jan To Now")
        st.plotly_chart(fig)


def checkbycuzti(df):
    CU = df['CU'].unique().tolist()
    Site = df['Site'].unique().tolist()

    Month = df['Month'].unique().tolist()
    Month.sort(key = lambda date: datetime.strptime(date, '%b'))


    df['ZTI Rate'] = df['ZTI Rate'].apply(lambda x: format(x, '.2%'))
    cu_selection = st.sidebar.multiselect('CU:', CU, default=None)
    site_selection = st.sidebar.multiselect('Site:', Site, default=None)
    MH_selection = st.sidebar.multiselect('Month:', Month, default=None)


    # filter
    mask = (df['CU'].isin(cu_selection)) & (df['Site'].isin(site_selection)) & (df['Rollout'] != 0) & (df['Month'].isin(MH_selection))
    number_of_result = df[mask].shape[0]
    df = df[mask]

    # chart
    total_Transmission = sum(df['Transmission'])
    total_GNB = sum(df['GNB'])
    total_ENM = sum(df['ENM'])
    total_Others = sum(df['Others'])
    total_Rollout = sum(df['Rollout'])
    total_ZTI = sum(df['ZTI'])
    if total_Rollout !=0:
        total_ZTI_rate = total_ZTI/total_Rollout
    else:
        total_ZTI_rate = 0


    issue_category = {
        'Category': ['Transmission', 'GNB', 'ENM', 'Others'],
        'Qty': [total_Transmission, total_GNB, total_ENM, total_Others]
    }

    detail_thnr = sum(df['Transmission-Hardware Not Ready'])
    detail_tdru = sum(df['Transmission- DHCP Realy Unconfigured'])
    detail_tdu = sum(df['Transmission- Data Unconfigured'])
    detail_tzndr = sum(df['Transmission-ZT no Discover received'])
    detail_eis = sum(df['ENM Issue'])
    detail_gti = sum(df['GNB Technical Issue'])
    detail_oth = sum(df['Others'])


    df_pie = pd.DataFrame(issue_category,index=[1,2,3,4],columns=['Category','Qty'])
    fig = px.pie(df_pie, values='Qty', names='Category',title='Issue Category')


    bar_chart = px.histogram(df, x='City', y=['ZTI','Rollout'],  barmode='group', title='Rollout and ZTI Num')
    scatter_chart = px.scatter(df, x='City', y='ZTI Rate', color='ZTI Rate', size_max=60, title='ZTI Rate')
    scatter_chart.update_layout(autotypenumbers='convert types')

    # display the text information
    if cu_selection and site_selection:

        str_cu = ",".join(cu_selection)
        str_site = ",".join(site_selection)
        st.subheader(":bar_chart: The summary of " + str_cu + ' and Site ' + str_site)
    else:
        st.subheader(":bar_chart: The summary of " + ' ' + ' ' +' Site')

    left_column, middle_column, right_column = st.columns(3)
    with left_column:
        st.caption("Total Number Of Rollout:")
        st.subheader(f"{total_Rollout:,}")
    with middle_column:
        st.caption("Total Number Of ZTI:")
        st.subheader(f"{total_ZTI:,}")
    with right_column:
        st.caption("ZTI Usage Rate:")
        print(total_ZTI_rate)
        if total_ZTI_rate > 0.8:
            icon = ':smile:'
        elif total_ZTI_rate > 0.6 and total_ZTI_rate < 0.8:
            icon=':disappointed:'
        else:
            icon=':sob:'
        st.subheader(f"{('{:.2%}'.format(total_ZTI_rate))}{icon}")

    st.markdown("""---""")


    #df.style.highlight_min(df.color='red', subset='ZTI Rate')
    st.dataframe(df.reset_index(drop=True), width=1500, height=900)
    st.markdown("""---""")

    #bar_chart.add_trace(line_chart)

    #st.plotly_chart(pie_chart)
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(bar_chart)
    with col2:
        st.plotly_chart(scatter_chart)

    sortdata(df)

    st.markdown("""---""")
    ####
    detaildata = dict(
        character=["Transmission", "ENM", "GNB", "Others","Transmission-Hardware Not Ready", "Transmission- DHCP Realy Unconfigured", "Transmission- Data Unconfigured", "Transmission-ZT no Discover received", "ENM Issue", "GNB Technical Issue", "others"],
        parent=["","","","","Transmission", "Transmission", "Transmission", "Transmission", "ENM", "GNB", "Others"],
        value=[total_Transmission,total_ENM,total_GNB,total_Others,detail_thnr, detail_tdru, detail_tdu, detail_tzndr, detail_eis, detail_gti, detail_oth])

    figsunburst = px.sunburst(
        detaildata,
        names='character',
        parents='parent',
        values='value',
        title='Detail Issue Data'
    )
    col3, col4 = st.columns(2)
    with col3:
        st.plotly_chart(fig)
    with col4:
        st.plotly_chart(figsunburst)


    issuesort(df)

def issuesort(df):
    cols = ['City','Rollout','ZTI','ZTI Rate','Transmission','ENM','GNB','Others']
    df = df[cols]

    Trasn = px.scatter(df.query("Transmission != 0"), x="Rollout", y="Transmission", size="Transmission", color="City",
                       hover_name="City", log_x=True, size_max=60, title='Transmission issue')
    if len(Trasn['data']) != 0:
        st.plotly_chart(Trasn, use_container_width=True)

    ENM = px.scatter(df.query("ENM != 0"), x="Rollout", y="ENM", size="ENM", color="City",
                     hover_name="City", log_x=True, size_max=60, title='ENM issue')
    if len(ENM['data']) != 0:
        st.plotly_chart(ENM, use_container_width=True)

    GNB = px.scatter(df.query("GNB != 0"), x="Rollout", y="GNB", size="GNB", color="City",
                     hover_name="City", log_x=True, size_max=60, title='GNB issue')
    if len(GNB['data']) != 0:
        st.plotly_chart(GNB, use_container_width=True)

    Others = px.scatter(df.query("Others != 0"), x="Rollout", y="Others", size="Others", color="City",
                        hover_name="City", log_x=True, size_max=60, title='Other issue')
    if len(Others['data']) != 0:
        st.plotly_chart(Others, use_container_width=True)

    st.markdown("""---""")

    issuescatter = px.scatter_matrix(df, dimensions=['Rollout','ZTI','Transmission','ENM','GNB','Others'], color='ZTI Rate')
    issuescatter.update_layout(width=1600,height=800)
    st.plotly_chart(issuescatter)



def sortdata(df):
    cols = ['City','Month','Rollout','ZTI','ZTI Rate']
    df = df[cols]
    mask = df['Rollout'] != 0
    fdf = df[mask]

    df_rollout1 = fdf.sort_values(by=['Rollout'],ascending=False).head(5)
    print(df_rollout1)
    bar_chart1 = px.bar(df_rollout1,  y=['Rollout'], x='City', color='ZTI',template='plotly_white', title='Top 5 Rollout')

    df_rollout2 = fdf.sort_values(by=['Rollout'],ascending=True).head(5)
    print(df_rollout2)
    bar_chart2 = px.bar(df_rollout2,  y=['Rollout'], x='City', color='ZTI',template='plotly_white', title='Last 5 Rollout')

    df_zti1 = fdf.sort_values(by=['ZTI'],ascending=False).head(5)
    bar_chart3 = px.bar(df_zti1, y=['ZTI'], x='City', color='Rollout',template='plotly_white', title='Top 5 ZTI')

    df_zti2 = fdf.sort_values(by=['ZTI'],ascending=True).head(5)
    bar_chart4 = px.bar(df_zti2, y=['ZTI'], x='City',  color='Rollout',template='plotly_white',title='Last 5 ZTI')

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.plotly_chart(bar_chart1, use_container_width=True)
    with col2:
        st.plotly_chart(bar_chart2, use_container_width=True)
    with col3:
        st.plotly_chart(bar_chart3, use_container_width=True)
    with col4:
        st.plotly_chart(bar_chart4, use_container_width=True)

def stchart():
    st.sidebar.header('Data Setting')
    option = st.sidebar.selectbox('Data Category',
                                  ('--','ASU','ZTI'))
    if option == 'ASU':
        uploaded_file = 'ASU.xlsx'
        df = pd.read_excel(uploaded_file, sheet_name='ASU', usecols='A:L')
        data_category = st.sidebar.selectbox("Choose the data category:", ("--","Total Summary","Check Detail Info"))
        if data_category == 'Total Summary':
            st.subheader('Total summary: ')
            rangesumasu(df)
        if data_category == 'Check Detail Info':
            checkbycu(df)
    elif option == 'ZTI':
        uploaded_file = 'ZTI.xlsx'
        df = pd.read_excel(uploaded_file, sheet_name='ZT Collection Info')
        data_category = st.sidebar.selectbox("Choose the data category:", ("--","Total Summary","CU and Site Summary","Check Detail Info"))

        if data_category == 'Total Summary':
            rangesumzti(df)

        if data_category == 'CU and Site Summary':
            #col1, col2, col3 = st.columns(3)
            #with col1:
            checkallzti(df)
            #with col2:
            #    st.write('')
            #with col3:
            # noztiPie(df)
        if data_category == 'Check Detail Info':
            checkbycuzti(df)


# Only select the sheet, we can see the data
if __name__ == '__main__':
    st.set_page_config(page_title='The summary of ENO program in MLC&TW Beta',layout="wide")
    st.header('2022 Data Summary of ENO MLC&TW Beta ')

    names = ['admin']
    usernames = ['admin']
    password = ['Ericss0n@123']
    hashed_passwords = stauth.Hasher(password).generate()

    authenticator = stauth.Authenticate(names,usernames,hashed_passwords,'some_cookie_name','some_signature_key',cookie_expiry_days=30)
    name, authentication_status, username = authenticator.login('Login', 'sidebar')

    if st.session_state['authentication_status']:
        st.sidebar.write('Welcome *%s*' % (st.session_state['name']))
        authenticator.logout('Logout', 'sidebar')
        stchart()
    elif st.session_state['authentication_status'] == False:
        st.sidebar.error('Username/password is incorrect')
    elif st.session_state['authentication_status'] == None:
        st.sidebar.warning('Please enter your username and password')