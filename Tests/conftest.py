import os
import sys

myPath = os.path.dirname(os.path.abspath(__file__))
print(myPath)
sys.path.insert(0, myPath + '/../')
from selenium import webdriver
from PageObjects.homePage import HomePage
import pytest
from selenium.webdriver.chrome.options import Options
import platform 
platform = platform.system()


@pytest.fixture()
def driver():
    if platform == 'Windows':
        driver_path = os.path.join(myPath, "../TestResources/drivers/chromedriver")
        driver = webdriver.Chrome(driver_path)    
    elif platform == 'Linux':     
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        driver_path = myPath.replace("/Tests","/TestResources/drivers_linux/chromedriver")
        driver = webdriver.Chrome(driver_path,chrome_options=chrome_options)        
    return driver

@pytest.fixture()
def home_page(driver):
    home_page = HomePage(driver)
    return home_page

@pytest.fixture()
def screenshot_path():
    if platform =="Windows":
        screeenshot_folder_path = os.path.join(myPath, "../TestResources/failed_tests_screens/")
    if platform =="Linux":
        screeenshot_folder_path =myPath.replace("/Tests", "/TestResources/failed_tests_screens/")
    return screeenshot_folder_path

@pytest.fixture(scope="session", autouse=True)
def my_own_session_run_at_beginning(request):
    print('\nIn my_own_session_run_at_beginning()')

    def my_own_session_run_at_end():
        print('In my_own_session_run_at_end()')
        # Generate HTML file report




        #READ CONTACTS
        contacts = []
        contacts_path = os.path.join(myPath, "../TestResources/contacts.txt")
        read = open(contacts_path, "r")
        contents = read.readlines()
        for line in contents:
            line = line.replace('\n', '')
            contacts.append(line)

        #GET PASSWORD FILE PATH
        if platform == "Windows":
            password_file = os.path.join(myPath, "../TestResources/password.txt")
        if platform == "Linux":
            password_file = myPath.replace("/Tests", "/TestResources/password.txt")

        print("report path")
        #print(testReport_path)
        # read stored password
        with open(password_file, 'rb') as f:
            password = f.read()

        # encrypt password
        key = Fernet.generate_key()
        fernet = Fernet(key)
        encrypted_password = fernet.encrypt(password)

        # decrypt password
        fernet_decrypt = Fernet(key)
        decrypted_password = fernet_decrypt.decrypt(encrypted_password)

        PASSWORD = decrypted_password.decode()
        MY_ADDRESS = "samanthachapa31990@gmail.com"
        print("Email Address" + MY_ADDRESS)
        #print("Password" + PASSWORD)

        if platform == "Windows":
            reports_file_path = os.path.join(myPath, "../reports/report.html")
        if platform == "Linux":
            reports_file_path = myPath.replace("/Tests", "/reports/report.html")
        try:
            s = smtplib.SMTP(host='smtp.gmail.com', port=587)
            s.ehlo()
            s.starttls()
            s.login(MY_ADDRESS, PASSWORD)
            print(s.noop())
            for email in contacts:
                msg = MIMEMultipart()  # create a message

                # add in the actual person name to the message template
                message = "Hello, test email"

                # setup the parameters of the message
                msg['From'] = MY_ADDRESS
                msg['To'] = email
                msg['Subject'] = "This is TEST"

                # add in the message body
                msg.attach(MIMEText(message))

                # add attachments
                filename = "report.html"
                attachment = open(reports_file_path, "rb")

                part = MIMEBase('application', 'octet-stream')
                part.set_payload((attachment).read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

                msg.attach(part)

                # send the message via the server set up earlier.
                s.send_message(msg)
                del msg
            s.quit()
        except:
            print("Exception occurred")


    request.addfinalizer(my_own_session_run_at_end)



