# Start writing code
(ms_download_facts
.merge(ms_user_dimension,how='left',on
='user_id')
.merge(ms_acc_dimension,how='left',on='acc_id')
.pivot_table(index='date',columns
='paying_customer',values='downloads'
,aggfunc='sum')
.query('no>yes')
.reset_index()
.sort_values('date'))