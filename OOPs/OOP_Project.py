 # Using NLP Cloud api for NLP related model 
import nlpcloud

class NLPApp:
      
      def __init__(self):
           self.__database = {}
           self.__first_menu()
      
      
      def __first_menu(self):
          first_input = input("""
                 Hi! Welcome to NLP App. How would you you wanted to proceed
                 1. Not a Member ? Register
                 2. Already a user ? Login
                 3. Don't Interested ? Exit 
                 """)
          if first_input == '1':
               print("Registering")
               self.__register()
                
          elif first_input == '2':
               self.__login()
          else:
               print("Wrong Choice")
               exit()
               
      def __second_menu(self):
          second_input = input("""
                 Hi! Welcome to NLP App. How would you you wanted to proceed
                 1. NER
                 2. Language Detection
                 3. Sentiment Analysis
                 """)
          if second_input == '1':
               self.__NER()
                
          elif second_input == 2:
               self.__Language_Detection()
          
          elif second_input == '3':
               self.__Sentiment_Analysis()
          else:
               exit()
           
      def __register(self):
           username = input("Enter your username: ")
           email = input("Enter your email adrress: ")
           password = input("Enter your password: ")
          
           
           if email in self.__database:
                print("User already exists")
           else:
                self.__database[email] = [username,password]
                print("Registered Successfully")
                print(self.__database)
                self.__first_menu()
     
     
      def __login(self):
          login_email = input("Enetr your email: ")  
          login_pass = input("Enetr your email: ")  
          
          if login_email in self.__database:
               if self.__database[login_email][1] == login_pass:
                    print("Login Successful")
                    self.__second_menu()
               else:
                    print("Wrong Password")
                    self.__login()
               
          else:
             print("Invalid Password")
             self.__first_menu()
      def __NER(self):
           user_para = input("Enetr the Paragraph: ")
           user_search = input("Enter what you wanted to search: ")
           

           client = nlpcloud.Client("finetuned-llama-3-70b", "b8f2fcb50ee56d2193b0b7eea01c6600b62244a4", gpu=True)
           response = client.entities(user_para,
           searched_entity=user_search
           )
           print("The searched entity is: ", response)
      
      def __Language_Detection(self):
           user_para = input("Enter the para: ")
           user_search = input("Enter the language you wanted to search: ")
           client = nlpcloud.Client("finetuned-llama-3-70b", "b8f2fcb50ee56d2193b0b7eea01c6600b62244a4", gpu=True)
           client.entities(user_para,
           searched_entity=user_search )
      def __Sentiment_Analysis(self):
           user_para = input("Enter the para: ")
           client = nlpcloud.Client("finetuned-llama-3-70b", "b8f2fcb50ee56d2193b0b7eea01c6600b62244a4", gpu=True)
           response = client.sentiment(user_para)
           print("The Sentiment is: ", response['scored_labels'])
           
           self.__second_menu()

Obj = NLPApp()





 
  
               
           
           