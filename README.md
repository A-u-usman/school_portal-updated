# School_portal
This project  is a simple portal web application for school. 
The portal  allows students to enter their personal and academic details.
Each student’s details can also be managed in the application. 

To run this application on your local machine, use the follwoing steps
1-- Activate the virtual enviroment "venv" using the command "venv\Scripts\activate"
2-- Install all the required packages in the requirements.txt file using the command "pip install -r requirements.txt"
3-- Create a MySQL database named "Students"
4-- Creat a table in the Sudent database called "informations"
5-- create the following columns in the informations table :
                                                            id          integer   Primary key
                                                            firstname   varchar(255)
                                                            middlename  varchar(255)
                                                            lastname    varchar(255)
                                                            email       varchar(255)
                                                            dob         date
                                                            gender      varchar(255)
                                                            phonenumber varchar(255)
                                                            address     varchar(255)
                                                            soo         varchar(255)
                                                            lga         varchar(255)
                                                            nok         varchar(255) 
                                                            jambscore    integer
                                                            admissionstatus   varchar(255)
                                                            filename          text
6-- start MySQL sever
7-- start the student portal application using the command "Python app.py"

create table  informations(
	id int NOT NULL auto_increment ,
    driverId varchar(15) NOT NULL UNIQUE,
    passport text,
    firtname varchar(30),
    lastname varchar(30),
    middlename varchar (30),
    dob DATE, 
    gender varchar(20), 
    marriageStatus varchar(20), 
    phoneNumber varchar(22), 
    address text, 
    highestQualification text,
    driverLicenseNo text,
    licenseExpiry DATE, 
    nameOfOwner varchar(50), 
    vehicleRegNo varchar(50), 
    regNoExpiry DATE, 
    vehicleType varchar(50), 
    vehicelCapacity text, 
    vehicleModel varchar(50),  
    vehicleColor varchar(50), 
    chasisNo text, 
    vehicleMake varchar(50), 
    purpose varchar(50), 
    lastService date,
    nextOfKinName text ,
    nextOfKinRel varchar(50),
    nextOfKinPhoneNo varchar(50),
    nextOfKinAddress text,
    primary key(id)
    
);


  lastname varchar(30),
            middlename varchar (30),
            dob DATE, 
            gender varchar(20), 
            marriageStatus varchar(20), 
            phoneNumber varchar(22), 
            address text, 
            highestQualification text,
            driverLicenseNo text,
            licenseExpiry DATE, 
            nameOfOwner varchar(50), 
            vehicleRegNo varchar(50), 
            regNoExpiry DATE, 
            vehicleType varchar(50), 
            vehicelCapacity text, 
            vehicleModel varchar(50),  
            vehicleColor varchar(50), 
            chasisNo text, 
            vehicleMake varchar(50), 
            purpose varchar(50), 
            lastService date,
            nextOfKinName text ,
            nextOfKinRel varchar(50),
            nextOfKinPhoneNo varchar(50),
            nextOfKinAddress text,
            '''