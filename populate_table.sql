use payrolldb;
insert into m_state values('TN','Tamil Nadu');
insert into m_state values('WB','West Bengal');
insert into m_state values('MP','Madhya Pradesh');
insert into m_state values('UP','Uttar Pradesh');
insert into m_state values('RA','Rajasthan');

insert into m_address (address_id,building_details,road,landmark,city,state_id,country) values(101, 'Buil-A', '5th Road', 'Near City Mall', 'Kolkata', 'WB', 'India');
insert into m_address (address_id,building_details,road,landmark,city,state_id,country) values(102, 'Sun Buil', 'Beena  Road', 'Near MeenaBazaar','Bareily', 'UP', 'India');
insert into m_address (address_id,building_details,road,landmark,city,state_id,country) values(103, 'Coach Buil', 'Nani Road', 'Near Cine Hall', 'Jaipur','RA' , 'India');
insert into m_address (address_id,building_details,road,landmark,city,state_id,country) values(104, 'Farmer Buil', 'Rajesh Road', 'Near Vellore Fort', 'Vellore', 'TN', 'India');
insert into m_address (address_id,building_details,road,landmark,city,state_id,country) values(105, 'Buil-X', 'Nano Road', 'Near MaxStore', 'Bhopal', 'MP', 'India');
insert into m_address (address_id,building_details,road,landmark,city,state_id,country) values(106, 'Office Buil','Nicco Park','Near SaltLake','Kolkata','WB','India');

insert into m_company (company_id,company_name,address_id) values(01, 'InfoBliss Capital',101);
insert into m_company (company_id,company_name,address_id) values(02, 'InfoBliss Cloud Solutions',103);
insert into m_company (company_id,company_name,address_id) values(03, 'InfoBliss Aegis',104);

insert into m_department (company_id, department_id,department_name) values(01,11,'Human Resources');
insert into m_department (company_id, department_id,department_name)  values(02,12,'Human Resources');
insert into m_department (company_id, department_id,department_name)  values(01,13,'Marketing');
insert into m_department (company_id, department_id,department_name)  values(02,14,'Technical');
insert into m_department (company_id, department_id,department_name)  values(03,15,'Accounts & Finance');
insert into m_department (company_id, department_id,department_name)  values(03,16,'Production');
insert into m_department (company_id, department_id,department_name)  values(02,17,'Research & Development');
insert into m_department (company_id, department_id,department_name)  values(01,18,'Accounts & Finance');

insert into m_grade values(1,'Head of Department');
insert into m_grade values(2,'Senior Officer');
insert into m_grade values(3,'Junior Staff');
insert into m_grade values(4,'Janitor');

insert into m_employee (employee_id,employee_name,department_id,company_id, address_id,employee_doj, grade_id) values(001,'Rajesh Raushan',11,01,102,'2015-02-01',1);
insert into m_employee (employee_id,employee_name,department_id,company_id, address_id,employee_doj, grade_id) values(002,'Vinay Verma',12,02,104,'2014-09-12',1);
insert into m_employee (employee_id,employee_name,department_id,company_id, address_id,employee_doj, grade_id) values(003,'Divya Doijod',13,01,106,'2019-12-01',2);
insert into m_employee (employee_id,employee_name,department_id,company_id, address_id,employee_doj, grade_id) values(004,'Manisha Mangal',14,02,105,'2018-08-30',2);
insert into m_employee (employee_id,employee_name,department_id,company_id, address_id,employee_doj, grade_id) values(005,'Payal Pandey',15,03,101,'2018-05-23',1);
insert into m_employee (employee_id,employee_name,department_id,company_id, address_id,employee_doj, grade_id) values(006,'Nandana Nair',16,03,104,'2017-09-15',2);
insert into m_employee (employee_id,employee_name,department_id,company_id, address_id,employee_doj, grade_id) values(007,'Anant Agarwal',17,02,105,'2020-04-11',3);
insert into m_employee (employee_id,employee_name,department_id,company_id, address_id,employee_doj, grade_id) values(008,'Kanan Kapoor',18,01,102,'2019-07-10',3);
insert into m_employee (employee_id,employee_name,department_id,company_id, address_id,employee_doj, grade_id) values(009,'Tanmay Tandon',15,03,102,'2017-05-28',3);
insert into m_employee (employee_id,employee_name,department_id,company_id, address_id,employee_doj, grade_id) values(010,'Farah fisher',11,01,103,'2018-11-19',3);
insert into m_employee (employee_id,employee_name,department_id,company_id, address_id,employee_doj, grade_id) values(011,'Howard Herman',15,03,106,'1995-08-25',4);

insert into m_paygrade (employee_id,grade_id,basic_amt,da_amt,pf_amt,medical_amt) values(001,1,400000,30000,3000,2500);
insert into m_paygrade (employee_id,grade_id,basic_amt,da_amt,pf_amt,medical_amt) values(003,2,300000,20000,2400,2500);
insert into m_paygrade (employee_id,grade_id,basic_amt,da_amt,pf_amt,medical_amt) values(007,3,230000,17000,2200,2500);
insert into m_paygrade (employee_id,grade_id,basic_amt,da_amt,pf_amt,medical_amt) values(011,4,16000,10000,1000,2500);

insert into m_pay (employee_id,fin_year,gross_salary,gross_dedn,net_salary) values(001,2020,458000,2000,456000);
insert into m_pay (employee_id,fin_year,gross_salary,gross_dedn,net_salary) values(002,2020,458000,3000,455000);
insert into m_pay (employee_id,fin_year,gross_salary,gross_dedn,net_salary) values(003,2020,324900,1555,323345);
insert into m_pay (employee_id,fin_year,gross_salary,gross_dedn,net_salary) values(004,2020,324900,2000,322900);
insert into m_pay (employee_id,fin_year,gross_salary,gross_dedn,net_salary) values(005,2020,458000,1700,456300);
insert into m_pay (employee_id,fin_year,gross_salary,gross_dedn,net_salary) values(006,2020,324900,1700,323200);
insert into m_pay (employee_id,fin_year,gross_salary,gross_dedn,net_salary) values(007,2020,404700,2300,402400);
insert into m_pay (employee_id,fin_year,gross_salary,gross_dedn,net_salary) values(008,2020,404700,2300,402400);
insert into m_pay (employee_id,fin_year,gross_salary,gross_dedn,net_salary) values(009,2020,404700,2300,402400);
insert into m_pay (employee_id,fin_year,gross_salary,gross_dedn,net_salary) values(010,2020,404700,2300,402400);
insert into m_pay (employee_id,fin_year,gross_salary,gross_dedn,net_salary) values(011,2020,29500,100,29400);

insert into t_leave ( employee_id,fin_year,leave_date, leave_type, is_approved) values(001,2020,'2020-09-11','LWP',1);
insert into t_leave ( employee_id,fin_year,leave_date, leave_type, is_approved) values(004,2020,'2020-10-23','PL',0);
insert into t_leave ( employee_id,fin_year,leave_date, leave_type, is_approved) values(009,2020,'2020-03-01','CL', 1);
insert into t_leave ( employee_id,fin_year,leave_date, leave_type, is_approved) values(011,2020,'2020-07-10','SL',-1);

insert into t_achievement (employee_id,achievement_date, achievement_type) values(011,'2020-06-25','25 Years Of Service');
insert into t_achievement (employee_id,achievement_date, achievement_type) values(003,'2020-11-12','Good Customer Service');
insert into t_achievement (employee_id,achievement_date, achievement_type) values(006,'2020-02-29','Employee of The Year');
insert into t_achievement (employee_id,achievement_date, achievement_type) values(010,'2020-03-03','Special Projects');
