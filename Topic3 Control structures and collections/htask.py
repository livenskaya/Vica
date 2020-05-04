#!/usr/bin/env python
# coding: utf-8

# In[1]:


geo_logs = [ 
 {'visit1': ['Москва', 'Россия']},
 {'visit2': ['Дели', 'Индия']},
 {'visit3': ['Владимир', 'Россия']},
 {'visit4': ['Лиссабон', 'Португалия']},
 {'visit5': ['Париж', 'Франция']},
 {'visit6': ['Лиссабон', 'Португалия']},
 {'visit7': ['Тула', 'Россия']},
 {'visit8': ['Тула', 'Россия']},
 {'visit9': ['Курск', 'Россия']},
 {'visit10': ['Архангельск', 'Россия']}
]


# In[7]:


name = []
for visit in geo_logs:
    for country in visit.values():
        if country[1] == 'Россия':
            name.append(visit)
print (name)
    


# In[9]:


ids = {'user1': [213, 213, 213, 15, 213], 
       'user2': [54, 54, 119, 119, 119], 
       'user3': [213, 98, 98, 35]}
print(ids.values())


# In[10]:


ids_set = set()


# In[ ]:




