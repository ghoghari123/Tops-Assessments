create schema bank_detail;
-- Create a Bank table, attributes are : branch id, branch name, branch city
create table Bank
(
branch_id int primary key, 
branch_name varchar(25),
branch_city varchar(50)
);
insert into Bank(branch_id,branch_name,branch_city) values 
(101,'YES Bnak','Ahmedabad'),
(102,'BOB Bnak','surat'),
(103,'HDFC Bnak','Mumbai'),
(104,'SBI Bnak','Ahmedabad'),
(105,'Panjab National Bnak','Surat'),
(106,'Reliance Bnak','Vadodara'),
(107,'ICICI Bnak','Karnataka'),
(108,'AXIS Bnak','Delhi'),
(109,'Dena Bnak','Surat'),
(110,'Union Bnak','Banglore');
select * from bank;
-- drop table Bank;
-- delete from Bank;

-- Create a Loan table, attributes are : loan no, branch id, account holder’s id, loan amount and loan type
create table loan
(
loan_no int primary key,
loan_amount double,
loan_type varchar(50),
branch_id int not null,
account_holder_id int,
foreign key loan(branch_id) references Bank(branch_id)
);
insert into Loan(loan_no,loan_amount,loan_type,branch_id,account_holder_id) values 
(1,2000,'Home Loan',101,201),
(2,5000,'Car Loan',102,202),
(3,900,'Home Loan',103,203),
(4,1500,'Personal Loan',104,204),
(5,800,'Car Loan',105,205),
(6,1000,'Home Loan',106,206),
(7,15000,'Personal Loan',107,207),
(8,500,'Car Loan',108,208),
(9,4000,'Personal Loan',109,209),
(10,1000,'Home Loan',110,210);
select * from Loan;
-- delete from Loan;
-- drop table loan;


-- Create a table named as Account holder for the same scenario containing the attributes are account holder’s id, account no, account holder’s name,
-- city,contact, date of account created, account status (active or terminated), account type and balance.
create table Account_holder
(
account_holder_id int primary key,
account_no int,
account_holder_name varchar(50),
city varchar(50),
contact varchar(15),
craeted_date_of_account varchar(11),
account_status varchar(15),
account_type varchar(15),
balance double
); 
insert into Account_holder(account_holder_id, account_no, account_holder_name, city, contact, craeted_date_of_account, account_status, account_type, balance) values 
(201,1101,'Riya Patel','Ahmedabad',7806058403,'20-May-1990','Active','Savings',100000),
(202,1202,'Delasi Italiya','Surat',7801348403,'29-Oct-1999','Terminated','Savings',15000),
(203,1033,'Ashish Rana','Mumbai',9806058403,'4-Nov-2004','Active','Checking',12000),
(204,1044,'Asha Kheni','Rajkot',9067594023,'28-Jan-2020','Terminated','Checking',18000),
(205,1055,'Knishak Sharma','Surat',7054312930,'20-Mar-2000','Active','Savings',10000),
(206,1066,'Yatri Virdiya','Mumbai',8645382022,'27-Apr-2023','Active','Checking',500),
(207,1077,'Nikhil Parmar','Banglore',9834221082,'11-Jun-2010','Terminated','Savings',150000),
(208,1088,'Jigar Vachhani','Panjab',8739201829,'28-Feb-2009','Active','Savings',88000),
(209,1099,'Priya Mehta','Ahmedabad',7634267810,'29-May-1999','Active','Savings',49000),
(210,1180,'Divyesh Vadodara','Ahmedabad',8530291840,'20-Apr-2020','Terminated','Checking',10200);
select * from Account_holder;
-- drop table Account_holder;
-- delete from Account_holder;


-- ● Consider an example where there’s an account holder table where we are doing an intra bank transfer i.e. a person holding account A is trying to transfer $100 to account B.
-- - for this you have to make a transaction in sql which can transfer fund from account A to B
-- - Make sure after the transaction the account information have to be updated for both the credit account and the debited account
delimiter &&
create procedure transaction ( in A varchar(25),in B varchar(25),in transfer_amount double)
begin
	declare available_balance double;
	 if not exists(select 1 from Account_holder where account_holder_id=A) then
 		signal sqlstate '45000' set message_text = 'From Account Doen Not Exits';
	end if;
 	if not exists(select 1 from Account_holder where account_holder_id=B) then
 		signal sqlstate '45000' set message_text = 'To Account Doen Not Exits';
 	end if;
    select balance into available_balance from Account_holder where account_no = A;
    if available_balance < transfer_amount then
		signal sqlstate '45000' set message_text = 'Insufficient Balance';
	end if;
    start transaction;
	update Account_holder set balance = balance - transfer_amount where account_no = A;
	update Account_holder set balance = balance + transfer_amount where account_no = B;
    commit;
end &&
call transaction('1101','1202',100);

-- Also fetch the details of the account holder who are related from the same city
select ah.account_holder_id,ah.account_holder_name,ah.city,b.account_holder_id,b.account_holder_name 
from account_holder ah join Account_holder b on ah.city = b.city
where ah.account_holder_id < b.account_holder_id;

--  Write a query to fetch account number and account holder name, whose accounts were created after 15th of any month
select account_no,account_holder_name from account_holder where craeted_date_of_account > 15;

-- Write a query to display the city name and count the branches in that city. Give the count of branches an alias name of Count_Branch.
select branch_city as City, count(branch_city) as Count_Branch from bank group by branch_city;

-- Write a query to display the account holder’s id, account holder’s name, branch id, and loan amount for people who have taken loans. 
select ah.account_holder_id,ah.account_holder_name,l.branch_id,l.loan_amount from loan l join account_holder ah on l.account_holder_id = ah.account_holder_id;