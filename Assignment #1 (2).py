#!/usr/bin/env python
# coding: utf-8

# In[5]:


# List of order ID’s which are processed 
processed_orders = [1152, 1154, 1155, 1156, 1157, 1160, 1161, 1162, 1166, 1169, 1170, 1172, 1176, 1050, 1178, 1051, 1052, 1054, 1058, 1060, 1061, 1062, 1065, 1066, 1067, 1068, 1069, 1076, 1077, 1080, 1081, 1083, 1091, 1085, 1088, 1089, 1131, 1092, 1094, 1095, 1099, 1102, 1103, 1104, 1106, 1107, 1108, 1109, 1111, 1117, 1119, 1121, 1150, 1128, 1129, 1136, 1137, 1139, 1140, 1141, 1144, 1148, 1124]

# List of order ID’s which are returned
returned_orders = [1153, 1158, 1159, 1163, 1164, 1165, 1167, 1168, 1171, 1173, 1174, 1175, 1177, 1053, 1055, 1056, 1057, 1059, 1063, 1064, 1070, 1071, 1072, 1073, 1074, 1075, 1078, 1079, 1082, 1084, 1086, 1087, 1090, 1093, 1096, 1097, 1098, 1100, 1101, 1105, 1110, 1112, 1113, 1114, 1115, 1116, 1118, 1120, 1122, 1123, 1125, 1126, 1127, 1130, 1132, 1133, 1134, 1135, 1138, 1142, 1143, 1145, 1146, 1147, 1149, 1151]

# Consider the information available in the above two lists and answer the question given below


# #### Count the total number of orders [ Orders include both processed and returned orders]
# 
# - 63
# - 66
# - 126
# - 129

# In[6]:


List3= ( processed_orders + returned_orders)
len(List3)


# #### In the total orders, identify the 50th order [ Note: Assume the order ID’s are being generated in a consecutive manner]
# 
# - 1152
# - 1099
# - 1154
# - 1100
# 

# In[11]:


List3= ( processed_orders + returned_orders)
A= sorted(List3)
print(A[49])


# In[ ]:





# In[ ]:





# In[ ]:





# #### Is 50th order a returned order or processed order?
# 
# - Returned Order
# - Processed Order
# 

# #### What is the last processed order ID ? [ Note: Assume the order ID’s are being generated in a consecutive manner]
# 
# - 1050
# - 1178
# - 1124
# - 1177
# 
# 

# In[18]:


A=1099
if A in processed_orders:
    print("Processed Order")
else:
    print("Returned Order")


# In[30]:


Z= sorted(processed_orders)
len(processed_orders)
print(Z[62])


# #### Identify the first 4 orders which are processed?
# 
# - 1152, 1154, 1155, 1156
# - 1051, 1152, 1153, 1154
# - 1050, 1051, 1052, 1054
# - 1050, 1051, 1052, 1053

# In[33]:


Z[0:4]


# In[ ]:




