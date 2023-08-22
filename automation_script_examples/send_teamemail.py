import os
from re import M
import win32com.client as win32
import time

# Setup Outlook Instance
olApp = win32.Dispatch("Outlook.Application")
olNS = olApp.GetNameSpace("MAPI")


mailitem = olApp.CreateItem(0)


#Abigail Email Object
mailitem.Subject = "Dashboards will arrive on Wednesday"
mailitem.BodyFormat = 1
mailitem.HTMLbody = (r"""Hello Everyone!<br><br>
     We are waiting on the window completion data to load into the dashboards. We should receive it tomorrow. I'll send out the dashboards as soon as we get it!<br><br>
     If you have any questions, please feel free to reach out!<br><br>
     Thanks,<br></br>
     """)
mailitem.To = "##########################"
# mailitem.Attachments.Add(os.path.join(os.getcwd(), "C:\\Users\\###\\Desktop\\FC\\KPI Trackers\\df\\dashboards\########.xlsx"))


mailitem.Display()
mailitem.Send()
# mailitem.Save()
time.sleep(3)