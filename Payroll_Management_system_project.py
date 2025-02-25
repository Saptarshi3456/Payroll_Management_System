import mysql.connector

import datetime

from tabulate import tabulate



while True:

    db = input("\nEnter name of your database: ")

    if db != '':

        break

    else:

        print('\n\t\tPlease Input A Database Name!')

mydb = mysql.connector.connect(host='localhost', user='root', passwd='84206')

mycursor = mydb.cursor()

if db != '':

    try:

        sql = 'CREATE DATABASE %s' % (db)

        mycursor.execute(sql)

        print("\n\t\tDatabase Created Successfully!")



    except:

        print("\n\t\tDatabase Already Created!")



mycursor = mydb.cursor()

mycursor.execute("Use "+db)



while True:

    TableName = input("\nName of Table to be created: ")

    if TableName != '':

        break

    else:

        print('\n\t\tPlease Input A Table Name!')



if TableName != '':

    try:

        query = "Create table "+TableName+" \

            (EmpNo int primary key,\

                Name varchar(15) not null,\

                    Job varchar(15),\

                        BasicSalary int,\

                            DA float,\

                                HRA float,\

                                    GrossSalary float,\

                                        Tax float,\

                                            NetSalary float)"

        mycursor.execute(query)

        print("\n\t\tTable "+TableName+" Created Successfully!")

    except:

        print("\n\t\tTable "+TableName+" Already Created!")





while True:

    print()

    print("*"*112)

    print('MAIN MENU'.center(112))

    print("*"*112)

    print()

    print('\t\t1.  For adding employee records.')

    print('\t\t2.  For displaying record of all the employees.')

    print('\t\t3.  For displaying record of a particular employee.')

    print('\t\t4.  For deleting record of all the employees.')

    print('\t\t5.  For deleting a record of a particular employee.')

    print('\t\t6.  For modification in the record.')

    print('\t\t7.  For displaying payroll.')

    print('\t\t8.  For displaying salary slip for all the employees.')

    print('\t\t9.  For displaying salary slip of a particular employee.')

    print('\t\t10. For exit.')

    print()

    print('Enter Choice : ', end='')

    choice = int(input())

    if choice == 1:

        try:

            print("\n\t\t: Now Input Employee's Information : ")

            mempno = int(input('\nEnter employee no.: '))

            mname = input('Enter employee name: ')

            mjob = input('Enter employee job: ')

            mbasic = float(input('Enter baisc salary: '))

            if mjob.upper() == 'OFFICER':

                mda = mbasic*0.5

                mhra = mbasic*0.35

                mtax = mbasic*0.2

            elif mjob.upper() == 'MANAGER':

                mda = mbasic*0.45

                mhra = mbasic*0.3

                mtax = mbasic*0.15

            else:

                mda = mbasic*0.4

                mhra = mbasic*0.25

                mtax = mbasic*0.1

            mgross = mbasic+mda+mhra

            mnet = mgross-mtax

            rec = (mempno, mname, mjob, mbasic, mda, mhra, mgross, mtax, mnet)

            query = "insert into "+TableName + \

                " values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"

            mycursor.execute(query, rec)



            mydb.commit()

            print("Record added successfully!")

        except Exception as e:

            print('\nSomething went wrong! ', e)



    elif choice == 2:

        try:

            query = 'select * from '+TableName

            mycursor.execute(query)

            print(tabulate(mycursor, headers=['Emp No.', 'Name', 'Job', 'Basic Salary',

                  'DA', 'HRA', 'Gross Salary', 'Tax', 'Net Salary'], tablefmt='fancy_grid'))

            '''myrecords=mycursor.fetchcall()

            for rec in myrecords:

                print(rec)'''

        except Exception as e:

            print('\nSomething went wrong! ', e)



    elif choice == 3:

        try:

            en = input('Enter employee no. of the record to be displayed: ')

            query = 'select * from '+TableName+' where EmpNo='+en

            mycursor.execute(query)

            print('\n\nRecord of Employee No.: '+en)

            print(tabulate(mycursor, headers=['Emp No.', 'Name', 'Job', 'Basic Salary',

                  'DA', 'HRA', 'Gross Salary', 'Tax', 'Net Salary'], tablefmt='fancy_grid'))

            c = mycursor.rowcount

            if c == -1:

                print('Nothing to display!')

        except Exception as e:

            print('\nSomething went wrong! ', e)



    elif choice == 4:

        try:

            ch = input('Do you want to delete all the records (Y/N)')

            if ch.upper() == 'Y':

                mycursor.execute('delete from '+TableName)

                mydb.commit()

                print('All the records have been deleted!')

        except Exception as e:

            print('\nSomething went wrong! ', e)



    elif choice == 5:

        try:

            en = input('Enter employee no. of the record to be deleted: ')

            query = 'delete from '+TableName+' where EmpNo='+en

            mycursor.execute(query)

            mydb.commit()

            c = mycursor.rowcount

            if c > 0:

                print('Deletion done!')

            else:

                print('Employee No. ', en, ' not found')

        except Exception as e:

            print('\nSomething went wrong! ', e)



    elif choice == 6:

        try:

            en = input('Enter employee no. of the record to be modified: ')

            query = 'select * from '+TableName+' where EmpNo='+en

            mycursor.execute(query)

            myrecord = mycursor.fetchone()

            c = mycursor.rowcount

            if c == -1:

                print('Employee No. '+en+' does not exist')

            else:

                mname = myrecord[1]

                mjob = myrecord[2]

                mbasic = myrecord[3]

                print('Emp No.      :', myrecord[0])

                print('Name         :', myrecord[1])

                print('Job          :', myrecord[2])

                print('Basic Salary :', myrecord[3])

                print('DA           :', myrecord[4])

                print('HRA          :', myrecord[5])

                print('Gross        :', myrecord[6])

                print('Tax          :', myrecord[7])

                print('Net          :', myrecord[8])

                print('---------------------------')

                print('Type value to modify below or just press Enter ↩ for no change')

                x = input('Enter name: ')

                if len(x) > 0:

                    mname = x

                x = input('Enter job: ')

                if len(x) > 0:

                    mjob = x

                    if mjob.upper() == 'OFFICER':

                        mda = mbasic*0.5

                        mhra = mbasic*0.35

                        mtax = mbasic*0.2

                    elif mjob.upper() == 'MANAGER':

                        mda = mbasic*0.45

                        mhra = mbasic*0.3

                        mtax = mbasic*0.15

                    else:

                        mda = mbasic*0.4

                        mhra = mbasic*0.25

                        mtax = mbasic*0.1

                x = input('Enter basic salary: ')

                if len(x) > 0:

                    mbasic = float(x)

                query = 'update '+TableName+' set Name='+"'"+mname+"'"+','+' Job=' + \

                    "'"+mjob+"'"+','+' BasicSalary=' + \

                        str(mbasic)+' where EmpNo='+en

                print(query)

                mycursor.execute(query)

                mydb.commit()

                print('Your record has been modified successfully!')

        except Exception as e:

            print('\nSomething went wrong! ', e)

    elif choice == 7:

        try:

            query = 'select * from '+TableName

            mycursor.execute(query)

            print("\n\n\n")

            print(112*'*')

            print('Employee Payroll'.center(112))

            print(112*'*')

            now = datetime.datetime.now()

            print("Current Date & Time: ", end=' ')

            print(now.strftime("%d-%m-%Y" + ' & ' + "%H:%M:%S"))

            print()

            print(tabulate(mycursor, headers=['Emp No.', 'Name', 'Job', 'Basic Salary',

                  'DA', 'HRA', 'Gross Salary', 'Tax', 'Net Salary'], tablefmt='psql'))



        except Exception as e:

            print('\nSomething went wrong! ', e)

    elif choice == 8:

        try:

            query = 'select * from '+TableName

            mycursor.execute(query)

            now = datetime.datetime.now()

            print()

            print('-'*112)

            print('SALARY SLIP'.center(112))

            print('-'*112)

            print('Current Date & Time:', end=' ')

            print(now.strftime("%d-%m-%Y"+' & '+"%H:%M:%S"))

            print()

            print(tabulate(mycursor, headers=['Emp No.', 'Name', 'Job', 'Basic Salary',

                  'DA', 'HRA', 'Gross Salary', 'Tax', 'Net Salary'], tablefmt='psql'))

        except Exception as e:

            print('\nSomething went wrong! ', e)

    elif choice == 9:

        try:

            en = input(

                "Enter employee no. whose pay slip you want to retrieve: ")

            query = 'select * from '+TableName+' where EmpNo='+en

            mycursor.execute(query)

            now = datetime.datetime.now()

            print()

            print("*"*112)

            print('SALARY SLIP OF A PARTICULAR EMPLOYEE'.center(112))

            print("*"*112)

            print('Current Date & Time:', end=' ')

            print(now.strftime("%d-%m-%Y"+' & '+"%H:%M:%S"))

            print(tabulate(mycursor, headers=[

                  'Emp No.', 'Name', 'Job', 'Basic Salary', 'DA', 'HRA', 'Gross Salary', 'Tax', 'Net Salary'], tablefmt='fancy_grid'))

        except Exception as e:

            print('\nSomething went wrong! ', e)

    elif choice == 10:

        break

    else:

        print('\nPlease choose the correct option number!')
