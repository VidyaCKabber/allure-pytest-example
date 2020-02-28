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

* Create Report folder under project tree
* Run below commond in project directory (Note : not in Reports directory)

		pytest --alluredir /home/Username/ProjectName/Reports
		
To see the generated report : -

		cd <Report Directory path> Ex : cd Reports

		allure serve /home/Username/ProjectName/Reports

