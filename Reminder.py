import time
from plyer import notification
 if __name__ == '__main__':
 	while True:
 		notification.notify(
 			title = "**Please Use Hand Sanitizer timely!!",
 			message ="This will keep us protected from corona virus.",
 			app_icon = "path to your .ico file",
 			timeout= 20
 			)
 		#	time.sleep(12)
 			time.sleep(60*60)