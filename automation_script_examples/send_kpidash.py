import os
from re import M
import win32com.client as win32
import time

# Setup Outlook Instance
olApp = win32.Dispatch("Outlook.Application")
olNS = olApp.GetNameSpace("MAPI")


### = olApp.CreateItem(0)
### = olApp.CreateItem(0)
### = olApp.CreateItem(0)
### = olApp.CreateItem(0)
### = olApp.CreateItem(0)


# ### Email Object
###.Subject = "UPDATED: KPI Dashboard"
###.BodyFormat = 1
###.HTMLbody = (r"""Hello Abigail!<br><br>
#      Your KPI Dashboard has been updated for the current week!<br><br>
#      Be sure to click Save As to download the file: abigail_dashboard.xlsx.<br> 
#      Also, make sure to enable content once you open the file.<br><br>
#      If you have any questions, please feel free to reach out!<br><br>
#      Thanks,<br></br>
#      """)
# ###.To = "##########"
# ###.Attachments.Add(os.path.join(os.getcwd(), "C:\\Users\\###\\Desktop\\FC\\KPI Trackers\\df\\dashboards\\#######.xlsx"))


# ###.Display()
# ###.Send()
# # ####.Save()
# time.sleep(3)



