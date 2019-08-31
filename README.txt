Steps for installation of the Product:


Note:		Read and follow each and every steps Carefully.....

Devices Required:

	3-Windows PC( Windows version should be 8,10 if windows 7 u should be updated upto service pack 1 )

	2-Web Camera ( It should meet some minimum quality expectation )


Working :

	1.Recognize_In program will run on first Pc.

	2.Recognize_Out program will run on second pc.

	3.Admin program will run on admin pc.

	3.All Program is Connected to a Online Mysql DB.

	4.Entry will be put by both program if any faces are found for each one minute.

	5.The In Attendance is put in "inat" Table of the DB.
	
	6.The Out Attendance is put in "outat" Table of the DB.

	7.You will be given a Admin program with two options:
	
			1.show by date(U have to give date as input of format (yyyy-mm-dd) )

				it will show the attendence entry on the given date.

			2.show by date and id (if u want to see any particular student came on a particular day)

				it will show the attendence entry on the given date and given id.

	
	Note:  Both programs need to be trained with datasets before running.


Configuring the In-Attendance Pc:

	Note: You need a stable Internet Connection .
	
	1.make sure python is installed on the entire machine.( while installing python 3.0+ ,the checkbox found below " Add PATH to python  " should be checked )
	else uninstall and reinstall the python by ticking the checkbox "Add PATH to python".
	
	2.Once python is installed :
		goto "Start -> cmd "
		
		type  "pip install opencv-contrib-python" press Enter the opencv package willbe installed on your machine.
		(wait for sometime it will take some time)		

		then type "pip install pillow" press Enter and wait for sometime.

		then type "pip install pymysql" press Enter and wait for sometime.

		Once the packages are installed our program is ready to run on our machine.

	3.Create a folder "Face Recognition".(wherever u want for ease u can put it in desktop)
		
		create three folders inside "Face Recognition"

			1."Cascades" (Captial C for starting letter).

			2."dataset"     (All small Letters).

			3."trainer"       (All small letters).


	4.Goto the gihub links:(the links can be easily copied by double clicking)

			1.  https://github.com/PRETHIV/Face_with_Online_DB/blob/master/datacollector.py

			Copy the entire code and paste it in a notepad and save it as "datacollector.py" inside "Face Recognition"
			(make sure u copy the code alone )

			2.  https://github.com/PRETHIV/Face_with_Online_DB/blob/master/trainer_python.py

			Copy the entire code and paste it in a notepad and save it as "trainer.py" inside "Face Recognition"
			(make sure u copy the code alone)	

			3. https://github.com/PRETHIV/Face_with_Online_DB/blob/master/recognize.py

			Copy the entire code and paste it in a notepad and save it as  "recognizein.py" inside "Face Recognition"
			(make sure u copy the code alone)

	5.The haarcascade_frontalface_default.xml can't be copied directly from the git because it is 30000+ lines of code.
		
		so you can find the xml file inside folder of cv2->data->haarcascade_frontalface_default.xml

		to find the path of cv2 goto start->cmd

		type "python" and press Enter

		type the following code 
			
		" import cv2
		  print(cv2.__file__) " and press Enter

		it will show you the entire path of pyd file don't go to the entire path go until "cv2"

		goto "data" and copy the "haarcascade_frontalface_default.xml" and paste it inside "Face Recognition" folder and inside "Cascades" folder as well.

		
	6.Once done collect Faces by runnning the "datacollector.py" .

	Note: Before running the program make sure the camera is working properly to verify that goto the following link

	
		link	:    https://webcamtests.com/

		Click Testmycam button  
  
		To run datacollector.py file goto "start -> cmd -> "

		Navigate to that folder "Face Recognition"  (To navigate type "cd (foldername) and press enter")

		once "Face Recognition " folder is navigated by cmd
		
		type "python datacollector.py" and press Enter

		it will start running and ask for a id to that face give a id in the format (yydepcoderollno)

		eg: my roll no is 310816205074 u have to give it as 16205074 more than 8 digits will not work

		Note:	(no popup will come just look into the camera after entering ur name)

		and enter name of the face

		and register ur face by looking into the camera .

		Note:	1.The lighting should be good.

			2.When registering your face no other faces should be visible within the camera. 

		Collect as many faces you want 

	7.Once done train the dataset by running "trainer.py".

		to run "trainer.py" goto "start->cmd"

		navigate to the "Face Recognition" folder

		type "python trainer.py"

		wait for sometime it will take some time depends on number of faces.


	8.Once done run "recognizein.py".

		to run "recognizein.py" goto "start->cmd"

		navigate to the "Face Recognition" folder

		type "python recognizein.py"

		it will take some time to start after initializing all the basic things

		once started,test by looking into the camera.

		Note : Entry will be put after every one minute.


Configuring the Out-Attendance Pc:

	Note:Stable internet connection is required.

	Step 1, 2, 3, 4.1, 4.2 are same 

	step 4.3:

		goto https://github.com/PRETHIV/Face_with_Online_DB/blob/master/recognizeout.py

		Copy the entire code and paste it in a notepad and save it as  "recognizeout.py" inside "Face Recognition"
		(make sure u copy the code alone)

	stet 5,6 and 7 are same:

	step 8:

		Once done run "recognizeout.py".

		to run "recognizeout.py" goto "start->cmd"

		navigate to the "Face Recognition" folder

		type "python recognizeout.py"

		it will take some time to start after initializing all the basic things

		once started test by looking into the camera.

		Note : Entry will be put after every one minute.



Configuring admin Pc:(Pc should be windows 7(service pack 1 or above) , 8, 10)

	Note: Stable internet connection is required.

	1.step 1 is as same as before .

	2.goto "start-> cmd"

		type "pip install pymysql" and press Enter.

	3.goto the link https://github.com/PRETHIV/Face_with_Online_DB/blob/master/Admin.py

		Copy the entire code and paste it in a notepad and save it as "admin.py" wherever u want.

	4.To run admin.py

		goto "start->cmd"

		navigate to the folder where u have the admin.py

		type "python admin.py" and press Enter 

	


	---------------X--------------------X-----------------------------X----------------------------



		ENJOY OUR PRODUCT......!




		

		

		

			
