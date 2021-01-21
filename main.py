import time
from selenium import webdriver
from proprofs import *
from mail import *
import os

op = webdriver.ChromeOptions()
op.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
op.add_argument("--headless")
op.add_argument("--disable-dev-sh-usage")
op.add_argument("--no-sandbox")

driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=op)

# Start the chrome driver and pass url of homerun login page
driver.get("https://app.homerun.co/login?redirect=")

# Maximize the browser window
driver.maximize_window()

# Find the email input field
email = driver.find_element_by_xpath('//*[@id="email"]')

# Find the password input field
password = driver.find_element_by_xpath('//*[@id="password"]')

# Send credentials to respective field
email.send_keys(user_email)
password.send_keys(user_pass)

# Wait for 2 seconds
time.sleep(2)

# Find "Login with email" button and then click on it
driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div/form/button').click()

# Wait for 10 seconds to load webpage properly
time.sleep(10)

# Homerun dashboard url
main_url = driver.current_url

# Initialize blank list which will used to store xpath of engineering jobs
engineering = []

# xpath of Senior react develop job
senior_react = '/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/div/div[2]/div[1]/div[1]/span[2]/a'

# Append the xpath to list
engineering.append(senior_react)


# Add comment function
def add_comment(marks, content, cd_mail):
    # Add result in comments
    comment = driver.find_element_by_css_selector('#portal-mount > div > div > div.PageModal__wrapper__184dL > div > '
                                                  'div > div > div.CandidateModal__candidate-profile-wrapper__kT10d > '
                                                  'div > div.CandidateProfile__widgets__3PMIn > div > div > div > '
                                                  'div.CandidateWidgets__wrapper__3_j4m > span > '
                                                  'div.CandidateWidgets__notes__sLByP > div > div > div > div > div > '
                                                  'div > div.TextEditor__editor__2HMtf.general__reset__1da_S > div')

    # Send comment content
    comment.send_keys(f'Marks - {marks}\n{content}\n{cd_mail}')

    # Wait for 2 seconds
    time.sleep(2)

    # Click on "Add" button to add comment
    driver.find_element_by_xpath('//*[@id="portal-mount"]/div/div/div[3]/div/div/div/div['
                                 '2]/div/div[2]/div/div/div/div[2]/span/div[2]/div/div/div['
                                 '1]/div/div[2]/div[2]/button').click()


# Compose mail function
def compose_mail(template):
    # Wait for 2 seconds
    time.sleep(2)

    # Click on "Compose email" button
    driver.find_element_by_xpath('//*[@id="portal-mount"]/div/div/div[3]/div/div/div/div[2]/div/div[1]/div/div['
                                 '2]/div[1]/div/div/div/div[2]/div[1]/div').click()

    # Wait for 2 seconds to load webpage properly
    time.sleep(2)

    # Click on Insert Template button
    driver.find_element_by_css_selector('#portal-mount > div:nth-child(2) > div > div.Modal__wrapper__KPSjL > div > '
                                        'div.Modal__content__24RSX.Modal__content-medium__14IIQ > div > '
                                        'div.CandidateTimelineModal__composer__11EH0 > div > div > '
                                        'div.EmailComposer__content__vg85Z.types__body__3w21D > '
                                        'div.EmailComposer__subject-block__3zYUa > div.EmailComposer__insert__3rdIi > '
                                        'div > div:nth-child(1) > button').click()

    # Wait for 2 seconds
    time.sleep(2)

    # Search template input field
    search_template = driver.find_element_by_css_selector('#portal-mount > div:nth-child(2) > div > '
                                                          'div.Modal__wrapper__KPSjL > div > '
                                                          'div.Modal__content__24RSX.Modal__content-medium__14IIQ > '
                                                          'div > '
                                                          'div.CandidateTimelineModal__composer__11EH0 > div > div > '
                                                          'div.EmailComposer__content__vg85Z.types__body__3w21D > '
                                                          'div.EmailComposer__subject-block__3zYUa > '
                                                          'div.EmailComposer__insert__3rdIi > div > '
                                                          'div.BaseSelect__options__2HneA.BaseSelect__footer'
                                                          '-active__3iOCv > '
                                                          'div.BaseSelect__header__NNuta > div > span > div > input['
                                                          'type=text]')

    # Wait for 2 seconds
    time.sleep(2)

    # Send the template name
    search_template.send_keys(f'{template}')

    # Wait for 2 seconds
    time.sleep(2)

    # Click on the searched template
    driver.find_element_by_css_selector('#portal-mount > div:nth-child(2) > div > div.Modal__wrapper__KPSjL > div > '
                                        'div.Modal__content__24RSX.Modal__content-medium__14IIQ > div > '
                                        'div.CandidateTimelineModal__composer__11EH0 > div > div > '
                                        'div.EmailComposer__content__vg85Z.types__body__3w21D > '
                                        'div.EmailComposer__subject-block__3zYUa > div.EmailComposer__insert__3rdIi > '
                                        'div > div.BaseSelect__options__2HneA.BaseSelect__footer-active__3iOCv > '
                                        'div:nth-child(2) > div > div').click()

    # Wait for 2 seconds
    time.sleep(2)

    # Click on Send button
    driver.find_element_by_css_selector('#portal-mount > div:nth-child(2) > div > div.Modal__wrapper__KPSjL > div > '
                                        'div.Modal__content__24RSX.Modal__content-medium__14IIQ > div > '
                                        'div.CandidateTimelineModal__composer__11EH0 > div > div > '
                                        'div.EmailComposer__footer__3XZtc > '
                                        'div.EmailComposer__button-group__24mIi.general__align-items-right__1IeWz'
                                        '.general__align-items__2XcUs > '
                                        'button.Button__secondary__2J5xH.Button__button__3GlfL').click()

    # Wait for 4 seconds
    time.sleep(4)

    # Close the email popup window
    driver.find_element_by_xpath('//*[@id="portal-mount"]/div[2]/div/div[2]/div/div[1]/div/div').click()

    # Wait for 2 seconds
    time.sleep(2)


# Move the candidate to desired stage
def move_candidate(stage):
    # Click on current stage
    driver.find_element_by_xpath('//*[@id="portal-mount"]/div/div/div[3]/div/div/div/div[2]/div/div[1]/div/div['
                                 '2]/div[1]/div/div/div/div[1]/div/div[1]/div').click()

    # Wait for 2 seconds
    time.sleep(2)

    # xpath of stage in which we want to move the candidate
    xpath2 = f'//*[@id="portal-mount"]/div/div/div[3]/div/div/div/div[2]/div/div[1]/div/div[2]/div[' \
             f'1]/div/div/div/div[1]/div/div[2]/div/div/div[{stage}] '

    # Click on the stage to move candidate
    driver.find_element_by_xpath(xpath2).click()

    # Wait for 5 seconds
    time.sleep(5)


# Function to check candidates
def check_candidates(job_url):
    # xpath of candidate in "Quiz link is sent" stage
    xpath1 = '/html/body/div[3]/div/div[2]/div/div[3]/div/div/div[3]/div/div/div[1]/a/div'

    i = 1

    # Check for candidates in "Quiz link is sent" stage
    while driver.find_element_by_xpath(xpath1):

        # Click on the candidate
        driver.find_element_by_xpath(xpath1).click()

        # Wait for 5 seconds to load modal candidate properly
        time.sleep(8)

        # Name of the candidate
        full_name = ''

        try:

            # Scrap full name of the candidate
            full_name = driver.find_element_by_xpath('.//*[@id="portal-mount"]/div/div/div[3]/div/div/div/div['
                                                     '2]/div/div[1]/div/div[2]/div[4]/div/div/div[1]/div[2]').text

            # Scrap email address of the candidate
            candidate_email = driver.find_element_by_xpath('.//*[@id="portal-mount"]/div/div/div[3]/div/div/div/div['
                                                           '2]/div/div[1]/div/div[2]/div[4]/div/div/div[2]/div['
                                                           '2]/button/span').text

            print(candidate_email, full_name)

            total_number_of_results = len(result_list)
            cd_result = 0

            # Check the result of the candidate
            for candidate_result in result_list:
                cd_result += 1
                if candidate_email == candidate_result['Email']:
                    print(candidate_email)
                    if candidate_result["Result"] > 60:
                        print("Pass")

                        r = candidate_result["Result"]

                        # Add result in comment
                        add_comment(r, "Passed", candidate_email)

                        # Wait for 2 seconds after adding comment
                        time.sleep(2)

                        # Try if Compose mail function is working properly or not
                        try:
                            # Send email with passed template
                            compose_mail("Sahil")

                        except Exception as mail_exception:
                            print(mail_exception)

                            # Shoot the Error mail
                            shoot_mail(subject=f'Error while send mail to {full_name}',
                                       body=f'Error - {mail_exception}')

                            # Close the browser
                            driver.quit()

                        # Try if move_candidate function is working properly or not
                        try:
                            # Move the candidate to "First Round" Stage
                            move_candidate(5)

                        except Exception as moving_exception:
                            print(moving_exception)

                            # Shoot the error mail
                            shoot_mail(subject=f'Error while changing the stage of {full_name}',
                                       body=f'Error - {moving_exception}')

                            # Close the browser
                            driver.quit()

                        # Wait for 2 seconds
                        time.sleep(2)

                        # Message body
                        message = f'Candidate Name - {full_name}\nMarks - {r}\nSuccessfully moved automatically to ' \
                                  f'First ' \
                                  f'Round '

                        # Shoot mail
                        shoot_mail(subject=f'{full_name}', body=message)

                        # Click on the job to
                        driver.get(job_url)

                        # Wait for 15 seconds to load job page page properly
                        time.sleep(15)
                        break
                    else:
                        print("Fail")

                        r = candidate_result["Result"]
                        # Add result in comment
                        add_comment(r, "Failed", candidate_email)

                        # Wait for 2 seconds after adding comment
                        time.sleep(2)

                        # Try if Compose mail function is working properly or not
                        try:
                            # Send email with disqualified template
                            compose_mail("Gordhan")

                        except Exception as mail_exception:
                            print(mail_exception)

                            # Shoot the Error mail
                            shoot_mail(subject=f'Error while send mail to {full_name}',
                                       body=f'Error - {mail_exception}')

                            # Close the browser
                            driver.quit()

                        # Try if move_candidate function is working properly or not
                        try:
                            # Move the candidate to "First Round" Stage
                            move_candidate(10)

                        except Exception as moving_exception:
                            print(moving_exception)

                            # Shoot the error mail
                            shoot_mail(subject=f'Error while changing the stage of {full_name}',
                                       body=f'Error - {moving_exception}')

                            # Close the browser
                            driver.quit()

                        # Wait for 2 seconds
                        time.sleep(2)

                        # Message body
                        message = f'Candidate Name - {full_name}\nMarks - {r}\nSuccessfully moved automatically to ' \
                                  f'Disqualified Stage '

                        # Shoot mail
                        shoot_mail(subject=f'{full_name}', body=message)

                        # Click on the job to
                        driver.get(job_url)

                        # Wait for 7 seconds to load job page page properly
                        time.sleep(7)
                        break

                elif cd_result == total_number_of_results and candidate_email != candidate_result['Email']:
                    print("Not in result list")
                    i += 1
                    xpath1 = f'/html/body/div[3]/div/div[2]/div/div[3]/div/div/div[3]/div/div/div[{i}]/a/div'
                    driver.get(job_url)
                    time.sleep(8)

        except Exception as exp:
            print(exp)

            # Shoot the error mail
            shoot_mail(subject=f'Some Error in {full_name}', body=f'Error - {exp}')

            # Close the browser
            driver.quit()


# Check job
def check_job():
    for job_xpath in engineering:
        print(job_xpath)

        # Click on job
        driver.find_element_by_xpath(job_xpath).click()

        # Wait for 20 seconds to load webpage properly
        time.sleep(20)
        # Store the current job url
        job_url = driver.current_url
        try:
            # Call check candidate function
            check_candidates(job_url)
        except Exception as ex:
            # Print the exception
            print(f'Error in Check_candidate function - {ex}')


try:
    # Call check_job function
    check_job()

except Exception as e:
    # Prints the error
    print(f'Error in Check_job function - {e}')
