import datetime
class Consultation:
    
    def __init__(self , cid=0 , pid=0 , remarks="" , medicines="" , next_followup=""):
        self.pid=pid
        self.cid=cid
        self.remarks=remarks
        self.medicines=medicines
        self.next_followup=next_followup
        self.created_on = datetime.datetime.now()
    
    def add_consultation_details(self):
        self.pid = input("Please enter patient id: ")
        self.remarks = input("Please enter your remarks: ")
        self.medicines = input("Please enter prescibed medicines: ")
        self.next_followup = input("Please enter next followup date (yyyy-mm-dd hh:mm:ss): ")
    
    def show(self):
        print("===========Consultation===========")

        consultation="""
        {cid} | {pid} 
        {remarks} {medicines}
        {next_followup} | {created_on}
        """.format_map(vars(self))

        print(consultation)

        print("===========Consultation===========")


"""
CREATE TABLE Consultation (
    cid INT PRIMARY KEY auto_increment,
    pid INT ,
    remarks VARCHAR(255),
    medicines VARCHAR(20),
    next_followup datetime,
    created_on datetime,
    FOREIGN KEY (pid) REFERENCES patient(pid)
);

"""