from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import Select

# Initialize the WebDriver
driver = webdriver.Chrome()


# Open the website
driver.get("https://practice-react.sdetunicorns.com/")
driver.maximize_window()
print(driver.title)
try:

    # 1. Wait for the User Profile button to appear and be clickable
    user_profile_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='root']/header/div[2]/div[1]/div/div[3]/div/div[2]/button/i"))
    )

    # adding additional time 
    driver.implicitly_wait(10)
    user_profile_button.click()
    

    print("User Profile button found and clicked!")

    # 2. Click on 'Register'
    register_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='root']/header/div[2]/div[1]/div/div[3]/div/div[2]/div/ul/li[2]/a"))   
    )

    driver.implicitly_wait(10)

    register_button.click()

    
    print("Register button clicked!")
   

   # 3. Fill all mandatory field

    username_field = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.ID, "username"))
    )
    username_field.send_keys("Asmaa_Hamisa_4")
    print("Username filled!")

    
    email_field = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.ID, "email"))
    )
    email_field.send_keys("asmaahamisa64@gmail.com")
    print("Email filled!")

    password_field = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "password"))
    )
    password_field.send_keys("Password123454")
    print("Password filled!")

    # Wait for the dropdown to be present
    gender_dropdown = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.ID, "gender"))
    )
  # Create a Select object
    select = Select(gender_dropdown)

  # Select an option by visible text
    select.select_by_visible_text("Female")

    print("gender selected!")
       
    # Submit the registration form


    submit_button = driver.find_element(By.XPATH, "//*[@id='root']/div/div/form/button")
    driver.implicitly_wait(10)
    submit_button.click()

    print("Registration form submitted!")




    # 4. Validate that user profile contains button logout

    user_profile_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='root']/header/div[2]/div[1]/div/div[3]/div/div[2]/button/i"))
    )   

    driver.implicitly_wait(10)
    user_profile_button.click()

    print("User Profile button found and clicked!")

    logout_button = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@id='root']/header/div[2]/div[1]/div/div[3]/div/div[2]/div/ul/li[2]"))
    )

    if logout_button:
        print("Logout button is present. Validation successful!")
    else:
        print("Logout button not found. Validation failed.")
    

  
except TimeoutException:
    print("Error: Element took too long to load.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
   


finally:

 driver.implicitly_wait(200)
  #  print(" Regester button founded !")
 driver.quit()