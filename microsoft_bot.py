from banner_modules import *
class pozitive:
    @classmethod
    def success(cls):
        cls.driver.close()
        return colored.green("[+]Account Has Been Generated Successfully")
class negative:
    @classmethod
    def fail(cls):
        
        cls.driver.close()
        return colored.red("[!]Some captcha issue has occured. Please run the script again...")  
class MicrosoftCaptchaBypass:
    @classmethod
    def classmethod_init(cls):
        try:
            if str(os.name=="nt"):
                with OpenKey(HKEY_CURRENT_USER, 'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders') as key:
                    cls.Downloads = QueryValueEx(key, '{374DE290-123F-4565-9164-39C4925E467B}')[0]
            elif str(os.name=="posix"):
                try:
                    cls.Downloads=str(os.path.expanduser("~")+"/Downloads")
                except:
                    print(colored.red("[!]Make sure your system is based on English Language!!!!"))
                    print(colored.yellow("-------------------------------------------------------"))
                    print(colored.red("[!]Sisteminizin Ingilizce tabanlı olduğuna emin olun."))
       
            microsoft_bot.DelPreviousCaptcha()
        except:
            pass
    @classmethod
    def DelPreviousCaptcha(cls):
        command1="del "+str(cls.Downloads)+'\*.wav'
        os.system(command1)
        microsoft_bot.fight_with_directory_errors(cls.Downloads)
    @classmethod
    def fight_with_directory_errors(cls):
        microsoft_bot.time_holder(3)
        command="rename "+str(cls.Downloads)+'\*.wav'+" captcha.wav"
        os.system(command)
        cls.file_path=cls.Downloads+"/captcha.wav"
        microsoft_bot.CaptchaBypass(cls.file_path)
    @classmethod
    def CaptchaBypass(cls,file_path):
        r=sr.Recognizer()
        try:
            with sr.AudioFile(file_path) as source:
                
                audio=r.listen(source)
                cls.text=r.recognize_google(audio)
                        
        except:
            print(colored.red("[-]Could not understand the captcha. Trying to  solve it again.."))
            microsoft_bot.IfNotCorrect()
                
        print(colored.green("Captcha Bypassed:")+colored.blue(cls.text))
        microsoft_bot.input_the_bypassed_captcha(cls.text)
    @classmethod
    def input_the_bypassed_captcha(cls,text):
     
        for j in range(0,len(text)):
            
            WebDriverWait(cls.driver, 10).until(EC.element_to_be_clickable((By.ID, "audio_response_field"))).send_keys(text[j])
            microsoft_bot.time_holder(0.3)
        microsoft_bot.time_holder(1)
        WebDriverWait(cls.driver, 10).until(EC.element_to_be_clickable((By.ID, "audio_submit"))).click()
        

        microsoft_bot.ItIsCorrect()
    @classmethod
    def ItIsCorrect(cls):
        try:
            WebDriverWait(cls.driver, 10).until(EC.element_to_be_clickable((By.ID, "idBtn_Back"))).click()
            print(microsoft_bot.success())
        except:
            microsoft_bot.IfNotCorrect()
    @classmethod
    def IfNotCorrect(cls):
        print(colored.red("[!]Error Occured. Trying To Solve The Captcha Again.."))
        error=WebDriverWait(cls.driver, 10).until(EC.element_to_be_clickable((By.ID, "audio_error"))).text
        if error=="Incorrect, try again":
            microsoft_bot.DelPreviousCaptcha()
            microsoft_bot.AboErrorLa()
            microsoft_bot.fight_with_directory_errors()
            
            
            
      

class proxy_and_vpnservices:
    @classmethod
    def chromedriveroptionfunction(cls):
        options = ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('disable-infobars')
        options.add_argument("--lang=en-GB")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument("window-size=1280,800")
        options.add_argument('--log-level=3')
        options.add_argument("--enable-logging")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.0383 Safari/537.36")
        cls.driver=uc.Chrome(options=options)
        

class generate_microsoft_mail:
    @classmethod
    def get_microsoft(cls,variable01,variable03,variable02,variable04):
        microsoft_bot.time_holder(0.07)
        cls.driver.get("https://signup.live.com/signup")
        microsoft_bot.time_holder(0.07)
        WebDriverWait(cls.driver, 10).until(EC.element_to_be_clickable((By.ID, "liveSwitch"))).click()
        try:
            microsoft_bot.time_holder(0.07)
            while(variable01<=len(cls.generated_mail)):
                WebDriverWait(cls.driver, 10).until(EC.element_to_be_clickable((By.NAME, "MemberName"))).send_keys(cls.generated_mail[variable01])
                microsoft_bot.time_holder(0.03)
                variable01+=1   
        except IndexError:
            pass
        WebDriverWait(cls.driver, 10).until(EC.element_to_be_clickable((By.ID, "iSignupAction"))).click()
        try:
            microsoft_bot.time_holder(0.07)
            while(variable03<=len(cls.generated_password_x)):
                WebDriverWait(cls.driver, 10).until(EC.element_to_be_clickable((By.ID, "PasswordInput"))).send_keys(cls.generated_password_x[variable03])
                microsoft_bot.time_holder(0.03)
                variable03+=1
           
        except IndexError:
            pass
        WebDriverWait(cls.driver, 10).until(EC.element_to_be_clickable((By.ID, "iSignupAction"))).click()
        try:
            microsoft_bot.time_holder(0.07)
            while(variable02<=len(cls.name)):
                WebDriverWait(cls.driver, 10).until(EC.element_to_be_clickable((By.ID, "FirstName"))).send_keys(cls.name[variable02])
                microsoft_bot.time_holder(0.03)
                variable02+=1
           
        except IndexError:
            pass
        WebDriverWait(cls.driver, 10).until(EC.element_to_be_clickable((By.ID, "iSignupAction"))).click()
        try:
            microsoft_bot.time_holder(0.07)
            for i in len(cls.name):
                WebDriverWait(cls.driver, 10).until(EC.element_to_be_clickable((By.ID, "FirstName"))).send_keys(cls.name[str(i)])
                microsoft_bot.time_holder(0.03)
        except TypeError:
            pass
        try:
            microsoft_bot.time_holder(0.07)
            while(variable04<=len(cls.surname)):
                WebDriverWait(cls.driver, 10).until(EC.element_to_be_clickable((By.ID, "LastName"))).send_keys(cls.surname[variable04])
                microsoft_bot.time_holder(0.03)
                variable04+=1
            WebDriverWait(cls.driver, 10).until(EC.element_to_be_clickable((By.ID, "iSignupAction"))).click()
        except IndexError:
             WebDriverWait(cls.driver, 10).until(EC.element_to_be_clickable((By.ID, "iSignupAction"))).click()
        
        for i in range(0,3):
            
            WebDriverWait(cls.driver, 10).until(EC.element_to_be_clickable((By.ID, "BirthDay"))).click()
            WebDriverWait(cls.driver, 10).until(EC.element_to_be_clickable((By.ID, "BirthDay"))).send_keys(cls.day)
            microsoft_bot.time_holder(0.07)
            WebDriverWait(cls.driver, 10).until(EC.element_to_be_clickable((By.ID, "BirthMonth"))).click()
            WebDriverWait(cls.driver, 10).until(EC.element_to_be_clickable((By.ID, "BirthMonth"))).send_keys(cls.month)
            microsoft_bot.time_holder(0.07)
            WebDriverWait(cls.driver, 10).until(EC.element_to_be_clickable((By.ID, "BirthYear"))).click()
            WebDriverWait(cls.driver, 10).until(EC.element_to_be_clickable((By.ID, "BirthYear"))).send_keys(cls.year)

        WebDriverWait(cls.driver, 10).until(EC.element_to_be_clickable((By.ID, "iSignupAction"))).click()
        microsoft_bot.time_holder(5)

class audio_download:
    @classmethod
    def listen_the_voice(cls):
        r=sr.Recognizer()
        while True:
            with sr.Microphone() as source:
                audio=r.listen(source)
                captcha=""
                try:
                    cls.text=r.recognize_google(audio)
                    print(colored.green("Bypassed Captcha:")+colored.blue(cls.text))
                    break
                except Exception as e:
                    print(colored.red("[!]Couldn't hear! If this error goes to infinity loop, press ctrl+c and run the script again."))
                    continue
        microsoft_bot.input_the_bypassed_captcha(cls.text)
    @classmethod
    def download_the_voice(cls):
        microsoft_bot.classmethod_init()
        microsoft_bot.time_holder(4)
        try:
            cls.driver.switch_to.frame(cls.driver.find_element_by_css_selector("#enforcementFrame"))
            cls.driver.switch_to.frame(cls.driver.find_element_by_css_selector("#fc-iframe-wrap"))
            WebDriverWait(cls.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/span/a[2]"))).click()
        except:
            WebDriverWait(cls.driver, 10).until(EC.element_to_be_clickable((By.ID, "idBtn_Back"))).click()
            print(microsoft_bot.success())
          
                #WebDriverWait(cls.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div[5]/div[2]/a[2]"))).click()
                #WebDriverWait(cls.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div[1]/div[3]/div/div[1]/div[5]/div/div/form/div[5]/div[1]/a"))).click()
                #microsoft_bot.listen_the_voice()
                #microsoft_bot.time_holder(1000)
                #print(microsoft_bot.fail())
                
                
         
        WebDriverWait(cls.driver, 10).until(EC.element_to_be_clickable((By.ID, "audio_download"))).click()

        microsoft_bot.fight_with_directory_errors()
        
        
    @classmethod
    def AboErrorLa(cls):
        WebDriverWait(cls.driver, 10).until(EC.element_to_be_clickable((By.ID, "audio_download"))).click()
   
        
            
class microsoft_bot(proxy_and_vpnservices,generate_microsoft_mail,audio_download,MicrosoftCaptchaBypass,pozitive,negative):
    def __init__(self):
        self.months=["January","March","April","June","July","August","September","October","November","December"]

        self.random_exts=["astar"]
        self.random_choice=random.choice(self.random_exts)
        

    
    @classmethod
    def disable_logs(cls):
        logging.getLogger("undetected_chromedriver").setLevel(logging.CRITICAL)
        logging.getLogger("selenium").setLevel(logging.CRITICAL)
   
 
        
    @classmethod
    def random_mailname_generator(cls):
     
        cls.generated_password=""
        
        mail_name=cls.name+cls.surname
        mail_length=random.randint(4,5)
        for i in range(0,mail_length):
            mail_name+=random.choice(string.digits)
            
        pw_l=random.randint(4,5)
        for j in range(0,pw_l):
            cls.generated_password+=str(random.choice(string.ascii_lowercase))
            cls.generated_password+=str(random.choice(string.digits))
        cls.generated_password_x=cls.generated_password
        cls.generated_mail=mail_name
        microsoft_bot.random_user_generator_info(cls.name,cls.surname,cls.day,cls.month,cls.year,cls.gender,cls.generated_mail,cls.generated_password_x)        
    @classmethod
    def random_user_generator_info(cls,name,surname,day,month,year,gender,generated_mail,generated_password_x):
        print(colored.green(f"Name:{name}\nSurname:{surname}\nBirthDay:{day}\nBirthMonth:{month}\nBirthYear:{year}\nGender:{gender}\nMail Address:{generated_mail}\nPassword:{generated_password_x}"))


    @classmethod
    def random_user_generator(cls,months):

        user_information=requests.get("https://randomuser.me/api/?nat=us")
        user_information=user_information.json()
        user_information=user_information["results"][0]
        cls.name=user_information["name"]["first"]
        cls.surname=user_information["name"]["last"]
        cls.date=user_information["dob"]["date"].split("T")[0]
        cls.year=cls.date.split("-")[0]
        cls.day=cls.date.split("-")[2]
        cls.month=random.choice(months)
        cls.gender=user_information["gender"]
        
        for i in range(1,10):
            if cls.day=="0"+str(i):
                cls.day=str(i)
       
    @staticmethod
    def time_holder(x):
        time.sleep(x)
    
  
    def run(self):
        microsoft_bot.disable_logs()
        microsoft_bot.random_user_generator(self.months)
        microsoft_bot.random_mailname_generator()
        
        microsoft_bot.chromedriveroptionfunction()
      
        
        microsoft_bot.get_microsoft(0,0,0,0)
        microsoft_bot.download_the_voice()
while True:
    try:
        micbot=microsoft_bot()
        micbot.run()
    except:
        continue

