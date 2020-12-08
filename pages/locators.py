

"""login page"""""
xpath_for_user_name = '//*[@id="login-username"]'
xpath_for_next_button = '//*[@id="login-signin"]'
xpath_for_password = '//*[@id="login-passwd"]'
xpath_for_signin_button = '//*[@id="login-signin"]'
xpath_for_compose_email_button = '//*[@id="app"]/div[2]/div/div[1]/nav/div/div[1]/a'
xpath_for_done_button_on_theme_popup = '//*[@id="modal-outer"]/div/div/div[3]/div[5]/button/span'
xpath_for_invalid_username_message = '//*[@data-error="messages.INVALID_USERNAME"]'
xpath_for_invalid_password_message = '//*[@id="password-challenge"]/form/p'
class_for_invalid_password_message = 'error-msg'
xpath_for_user_setting_button = '//*[@id="ybar-inner-wrap"]/div[2]/div/div[3]/div[1]/div/label/span'
xpath_for_logout_button = "//*[text()='Sign out']"

"""email filter"""""
xpath_for_mail_checkbox = "//*[@type='button' and @title = 'Checkbox, not checked' and @aria-label='Select message' and @class]//ancestor::div[2]/child::div"
xpath_for_mail_menu = "//*[@type='button' and @title='More options' and @tabindex='-1']"
xpath_for_filter_option = "//*[@class='D_F' and @title='Filter messages like this...']"
xpath_for_filter_dropdown = "//*[@id='modal-outer']/div/div/div[2]/div[2]/div/div[1]/div/span[2]"
xpath_for_filter_add_new_filter = "//*[@data-iskeynav='true' and @class='D_F ab_C r_P cdPFi_Z281SGl ir3_1JO2M7 it3_dRA I4_T W_6D6F']"
xpath_for_add_text_in_filter = "//*[@aria-label='Enter folder name [Press enter to create folder]' and @class='q_T y_Z2hYGcu je_0 jb_0 X_eo6 N_fq7 W_6D6F k_w H_6LEV b_0 I_2bfYWg']"
xpath_for_save_filter = "//*[@id='modal-outer']/div/div/div[3]/button[1]"
xpath_for_label_success_message = "//*[@id='app']/div[5]/div/div/div/div[2]/span"

"""compose email"""""
xpath_to_click_compose_email_button = "//*[text()='Compose' and @data-test-id='compose-button']" #"//*[@href='/d/compose/']"
xpath_to_enter_email_address = "//*[@id='message-to-field']"
xpath_to_enter_email_subject = "//*[@data-test-id='compose-subject']"
xpath_to_enter_email_body = "//*[@data-test-id='rte' and @aria-label='Message body']"
xpath_to_send_email = "//*[@data-test-id='compose-send-button' and @title='Send this email']"
xpath_to_click_on_attachment_button = "//*[@data-test-id='icon-btn-attach' and @aria-label='Attach files']"
xpath_to_click_upload_file_from_computer = "//*[text()='Attach files from computer']//ancestor::span//parent::button"