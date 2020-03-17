# allure-pytest-example
Creating detailed graphical reports of pytest using allure


Installation and Usage
-

	Create a project in pycharm, install the below mentioned packages
	python3 - 3.6.9
	allure  - 2.6.0 
	pytest - 4.0.2           1     -> pip3 install pytest==4.0.2
	pytest-allure-adaptor-1.7.10   -> pip3 install pytest-allure-adaptor
	attrs-19.1.0                   -> pip3 install attrs==19.1.0

To generate the report : -

* Create Report folder in project folder
* Run below commond in project directory (Note : not in Reports directory)

		pytest --alluredir /home/Username/ProjectName/Reports
		
To see the generated report : -

		cd <Report Directory path> Ex : cd Reports

		allure serve /home/Username/ProjectName/Reports

Report Screens :-

<div float="left">
    
   <img src="https://github.com/VidyaCKabber/allure-pytest-example/blob/master/Images/Overview.png" data-canonical-src="https://gyazo.com/eb5c5741b6a9a16c692170a41a49c858.png" style="margin-left:30px;" height="500" />
   &nbsp;&nbsp;&nbsp;&nbsp;
   <img src="https://github.com/VidyaCKabber/allure-pytest-example/blob/master/Images/Categories.png" data-canonical-src="https://gyazo.com/eb5c5741b6a9a16c692170a41a49c858.png" style="margin-left:30px;" height="500" />
   <img src="https://github.com/VidyaCKabber/allure-pytest-example/blob/master/Images/Categories.png" data-canonical-src="https://gyazo.com/eb5c5741b6a9a16c692170a41a49c858.png" style="margin-left:30px;" height="500" />
   <img src="https://github.com/VidyaCKabber/allure-pytest-example/blob/master/Images/Suits.png" data-canonical-src="https://gyazo.com/eb5c5741b6a9a16c692170a41a49c858.png" style="margin-left:30px;" height="500" />
   <img src="https://github.com/VidyaCKabber/allure-pytest-example/blob/master/Images/Graphs.png" data-canonical-src="https://gyazo.com/eb5c5741b6a9a16c692170a41a49c858.png" style="margin-left:30px;" height="500" />
   <img src="https://github.com/VidyaCKabber/allure-pytest-example/blob/master/Images/Timeline.png" data-canonical-src="https://gyazo.com/eb5c5741b6a9a16c692170a41a49c858.png" style="margin-left:30px;" height="500" />
   <img src="https://github.com/VidyaCKabber/allure-pytest-example/blob/master/Images/Behaviors.png" data-canonical-src="https://gyazo.com/eb5c5741b6a9a16c692170a41a49c858.png" style="margin-left:30px;" height="500" />
   <img src="https://github.com/VidyaCKabber/allure-pytest-example/blob/master/Images/Package.png" data-canonical-src="https://gyazo.com/eb5c5741b6a9a16c692170a41a49c858.png" style="margin-left:30px;" height="500" />
</div>
