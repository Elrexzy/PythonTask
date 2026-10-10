def main_menu():
    menu = """
===== MAIN MENU =====
1. Phone book
2. Messages
3. Chat
4. Call register
5. Tones
6. Settings
7. Call divert
8. Music
9. Games
10. Calculator
11. Reminders
12. Clock
13. Profiles
14. Services
15. SIM services
16. Exit
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 1:
            phone_book_menu()
        case 2:
            messages_menu()
        case 3:
            chat_menu()
        case 4:
            call_register_menu()
        case 5:
            tones_menu()
        case 6:
            settings_menu()
        case 7:
            call_divert_menu()
        case 8:
            music_menu()
        case 9:
            games_menu()
        case 10:
            calculator_menu()
        case 11:
            reminders_menu()
        case 12:
            clock_menu()
        case 13:
            profiles_menu()
        case 14:
            services_menu()
        case 15:
            sim_services_menu()
        case 16:
            print("Let us do this again")
        case _:
            main_menu()


def phone_book_menu():
    menu = """
===== PHONE BOOK =====
1. Search
2. Service Nos.
3. Add name
4. Erase
5. Edit
6. Copy
7. Assign tone
8. Send b'card
9. Options
10. Speed dials
11. Voice tags
12. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 1:
            search_menu()
        case 2:
            service_nos_menu()
        case 3:
            add_name_menu()
        case 4:
            erase_menu()
        case 5:
            edit_menu()
        case 6:
            copy_menu()
        case 7:
            assign_tone_menu()
        case 8:
            send_business_card_menu()
        case 9:
            phone_book_options_menu()
        case 10:
            speed_dials_menu()
        case 11:
            voice_tags_menu()
        case 0:
            main_menu()
        case 100:
            main_menu()
        case _:
            phone_book_menu()


def search_menu():
    menu = """
===== SEARCH =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            phone_book_menu()
        case 100:
            main_menu()
        case _:
            search_menu()


def service_nos_menu():
    menu = """
===== SERVICE NOS. =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            phone_book_menu()
        case 100:
            main_menu()
        case _:
            service_nos_menu()


def add_name_menu():
    menu = """
===== ADD NAME =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            phone_book_menu()
        case 100:
            main_menu()
        case _:
            add_name_menu()


def erase_menu():
    menu = """
===== ERASE =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            phone_book_menu()
        case 100:
            main_menu()
        case _:
            erase_menu()


def edit_menu():
    menu = """
===== EDIT =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            phone_book_menu()
        case 100:
            main_menu()
        case _:
            edit_menu()


def copy_menu():
    menu = """
===== COPY =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            phone_book_menu()
        case 100:
            main_menu()
        case _:
            copy_menu()


def assign_tone_menu():
    menu = """
===== ASSIGN TONE =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            phone_book_menu()
        case 100:
            main_menu()
        case _:
            assign_tone_menu()


def send_business_card_menu():
    menu = """
===== SEND B'CARD =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            phone_book_menu()
        case 100:
            main_menu()
        case _:
            send_business_card_menu()


def phone_book_options_menu():
    menu = """
===== OPTIONS =====
1. Memory in use
2. Type of view
3. Memory status
4. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 1:
            memory_in_use_menu()
        case 2:
            type_of_view_menu()
        case 3:
            memory_status_menu()
        case 0:
            phone_book_menu()
        case 100:
            main_menu()
        case _:
            phone_book_options_menu()


def memory_in_use_menu():
    menu = """
===== MEMORY IN USE =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            phone_book_options_menu()
        case 100:
            main_menu()
        case _:
            memory_in_use_menu()


def type_of_view_menu():
    menu = """
===== TYPE OF VIEW =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            phone_book_options_menu()
        case 100:
            main_menu()
        case _:
            type_of_view_menu()


def memory_status_menu():
    menu = """
===== MEMORY STATUS =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            phone_book_options_menu()
        case 100:
            main_menu()
        case _:
            memory_status_menu()


def speed_dials_menu():
    menu = """
===== SPEED DIALS =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            phone_book_menu()
        case 100:
            main_menu()
        case _:
            speed_dials_menu()


def voice_tags_menu():
    menu = """
===== VOICE TAGS =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            phone_book_menu()
        case 100:
            main_menu()
        case _:
            voice_tags_menu()


def messages_menu():
    menu = """
===== MESSAGES =====
1. Write messages
2. Inbox
3. Outbox
4. Picture messages
5. Templates
6. Smileys
7. Message settings
8. Info service
9. Voice mailbox number
10. Service command editor
11. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 1:
            write_messages_menu()
        case 2:
            inbox_menu()
        case 3:
            outbox_menu()
        case 4:
            picture_messages_menu()
        case 5:
            templates_menu()
        case 6:
            smileys_menu()
        case 7:
            message_settings_menu()
        case 8:
            info_service_menu()
        case 9:
            voice_mailbox_number_menu()
        case 10:
            service_command_editor_menu()
        case 0:
            main_menu()
        case 100:
            main_menu()
        case _:
            messages_menu()


def write_messages_menu():
    menu = """
===== WRITE MESSAGES =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            messages_menu()
        case 100:
            main_menu()
        case _:
            write_messages_menu()


def inbox_menu():
    menu = """
===== INBOX =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            messages_menu()
        case 100:
            main_menu()
        case _:
            inbox_menu()


def outbox_menu():
    menu = """
===== OUTBOX =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            messages_menu()
        case 100:
            main_menu()
        case _:
            outbox_menu()


def picture_messages_menu():
    menu = """
===== PICTURE MESSAGES =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            messages_menu()
        case 100:
            main_menu()
        case _:
            picture_messages_menu()


def templates_menu():
    menu = """
===== TEMPLATES =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            messages_menu()
        case 100:
            main_menu()
        case _:
            templates_menu()


def smileys_menu():
    menu = """
===== SMILEYS =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            messages_menu()
        case 100:
            main_menu()
        case _:
            smileys_menu()


def message_settings_menu():
    menu = """
===== MESSAGE SETTINGS =====
1. Set 1
2. Common
3. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 1:
            set_one_menu()
        case 2:
            common_menu()
        case 0:
            messages_menu()
        case 100:
            main_menu()
        case _:
            message_settings_menu()


def set_one_menu():
    menu = """
===== SET 1 =====
1. Message centre number
2. Messages sent as
3. Message validity
4. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 1:
            message_centre_number_menu()
        case 2:
            messages_sent_as_menu()
        case 3:
            message_validity_menu()
        case 0:
            message_settings_menu()
        case 100:
            main_menu()
        case _:
            set_one_menu()


def message_centre_number_menu():
    menu = """
===== MESSAGE CENTRE NUMBER =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            set_one_menu()
        case 100:
            main_menu()
        case _:
            message_centre_number_menu()


def messages_sent_as_menu():
    menu = """
===== MESSAGES SENT AS =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            set_one_menu()
        case 100:
            main_menu()
        case _:
            messages_sent_as_menu()


def message_validity_menu():
    menu = """
===== MESSAGE VALIDITY =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            set_one_menu()
        case 100:
            main_menu()
        case _:
            message_validity_menu()


def common_menu():
    menu = """
===== COMMON =====
1. Delivery reports
2. Reply via same centre
3. Character support
4. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 1:
            delivery_reports_menu()
        case 2:
            reply_via_same_centre_menu()
        case 3:
            character_support_menu()
        case 0:
            message_settings_menu()
        case 100:
            main_menu()
        case _:
            common_menu()


def delivery_reports_menu():
    menu = """
===== DELIVERY REPORTS =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            common_menu()
        case 100:
            main_menu()
        case _:
            delivery_reports_menu()


def reply_via_same_centre_menu():
    menu = """
===== REPLY VIA SAME CENTRE =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            common_menu()
        case 100:
            main_menu()
        case _:
            reply_via_same_centre_menu()


def character_support_menu():
    menu = """
===== CHARACTER SUPPORT =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            common_menu()
        case 100:
            main_menu()
        case _:
            character_support_menu()


def info_service_menu():
    menu = """
===== INFO SERVICE =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            messages_menu()
        case 100:
            main_menu()
        case _:
            info_service_menu()


def voice_mailbox_number_menu():
    menu = """
===== VOICE MAILBOX NUMBER =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            messages_menu()
        case 100:
            main_menu()
        case _:
            voice_mailbox_number_menu()


def service_command_editor_menu():
    menu = """
===== SERVICE COMMAND EDITOR =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            messages_menu()
        case 100:
            main_menu()
        case _:
            service_command_editor_menu()


def chat_menu():
    menu = """
===== CHAT =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            main_menu()
        case 100:
            main_menu()
        case _:
            chat_menu()


def call_register_menu():
    menu = """
===== CALL REGISTER =====
1. Missed calls
2. Received calls
3. Dialled numbers
4. Erase recent call lists
5. Show call duration
6. Show call costs
7. Call cost settings
8. Prepaid credit
9. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 1:
            missed_calls_menu()
        case 2:
            received_calls_menu()
        case 3:
            dialled_numbers_menu()
        case 4:
            erase_recent_call_lists_menu()
        case 5:
            call_duration_menu()
        case 6:
            call_costs_menu()
        case 7:
            call_cost_settings_menu()
        case 8:
            prepaid_credit_menu()
        case 0:
            main_menu()
        case 100:
            main_menu()
        case _:
            call_register_menu()


def missed_calls_menu():
    menu = """
===== MISSED CALLS =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            call_register_menu()
        case 100:
            main_menu()
        case _:
            missed_calls_menu()


def received_calls_menu():
    menu = """
===== RECEIVED CALLS =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            call_register_menu()
        case 100:
            main_menu()
        case _:
            received_calls_menu()


def dialled_numbers_menu():
    menu = """
===== DIALLED NUMBERS =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            call_register_menu()
        case 100:
            main_menu()
        case _:
            dialled_numbers_menu()


def erase_recent_call_lists_menu():
    menu = """
===== ERASE RECENT CALL LISTS =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            call_register_menu()
        case 100:
            main_menu()
        case _:
            erase_recent_call_lists_menu()


def call_duration_menu():
    menu = """
===== SHOW CALL DURATION =====
1. Last call duration
2. All calls' duration
3. Received calls' duration
4. Dialled calls' duration
5. Clear timers
6. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 1:
            last_call_duration_menu()
        case 2:
            all_calls_duration_menu()
        case 3:
            received_calls_duration_menu()
        case 4:
            dialled_calls_duration_menu()
        case 5:
            clear_timers_menu()
        case 0:
            call_register_menu()
        case 100:
            main_menu()
        case _:
            call_duration_menu()


def last_call_duration_menu():
    menu = """
===== LAST CALL DURATION =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            call_duration_menu()
        case 100:
            main_menu()
        case _:
            last_call_duration_menu()


def all_calls_duration_menu():
    menu = """
===== ALL CALLS' DURATION =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            call_duration_menu()
        case 100:
            main_menu()
        case _:
            all_calls_duration_menu()


def received_calls_duration_menu():
    menu = """
===== RECEIVED CALLS' DURATION =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            call_duration_menu()
        case 100:
            main_menu()
        case _:
            received_calls_duration_menu()


def dialled_calls_duration_menu():
    menu = """
===== DIALLED CALLS' DURATION =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            call_duration_menu()
        case 100:
            main_menu()
        case _:
            dialled_calls_duration_menu()


def clear_timers_menu():
    menu = """
===== CLEAR TIMERS =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            call_duration_menu()
        case 100:
            main_menu()
        case _:
            clear_timers_menu()


def call_costs_menu():
    menu = """
===== SHOW CALL COSTS =====
1. Last call cost
2. All calls' cost
3. Clear counters
4. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 1:
            last_call_cost_menu()
        case 2:
            all_calls_cost_menu()
        case 3:
            clear_counters_menu()
        case 0:
            call_register_menu()
        case 100:
            main_menu()
        case _:
            call_costs_menu()


def last_call_cost_menu():
    menu = """
===== LAST CALL COST =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            call_costs_menu()
        case 100:
            main_menu()
        case _:
            last_call_cost_menu()


def all_calls_cost_menu():
    menu = """
===== ALL CALLS' COST =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            call_costs_menu()
        case 100:
            main_menu()
        case _:
            all_calls_cost_menu()


def clear_counters_menu():
    menu = """
===== CLEAR COUNTERS =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            call_costs_menu()
        case 100:
            main_menu()
        case _:
            clear_counters_menu()


def call_cost_settings_menu():
    menu = """
===== CALL COST SETTINGS =====
1. Call cost limit
2. Show costs in
3. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 1:
            call_cost_limit_menu()
        case 2:
            show_costs_in_menu()
        case 0:
            call_register_menu()
        case 100:
            main_menu()
        case _:
            call_cost_settings_menu()


def call_cost_limit_menu():
    menu = """
===== CALL COST LIMIT =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            call_cost_settings_menu()
        case 100:
            main_menu()
        case _:
            call_cost_limit_menu()


def show_costs_in_menu():
    menu = """
===== SHOW COSTS IN =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            call_cost_settings_menu()
        case 100:
            main_menu()
        case _:
            show_costs_in_menu()


def prepaid_credit_menu():
    menu = """
===== PREPAID CREDIT =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            call_register_menu()
        case 100:
            main_menu()
        case _:
            prepaid_credit_menu()


def tones_menu():
    menu = """
===== TONES =====
1. Ringing tone
2. Ringing volume
3. Incoming call alert
4. Message alert tone
5. Keypad tones
6. Warning tones
7. Vibrating alert
8. Screen saver
9. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 1:
            ringing_tone_menu()
        case 2:
            ringing_volume_menu()
        case 3:
            incoming_call_alert_menu()
        case 4:
            message_alert_tone_menu()
        case 5:
            keypad_tones_menu()
        case 6:
            warning_tones_menu()
        case 7:
            vibrating_alert_menu()
        case 8:
            screen_saver_menu()
        case 0:
            main_menu()
        case 100:
            main_menu()
        case _:
            tones_menu()


def ringing_tone_menu():
    menu = """
===== RINGING TONE =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            tones_menu()
        case 100:
            main_menu()
        case _:
            ringing_tone_menu()


def ringing_volume_menu():
    menu = """
===== RINGING VOLUME =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            tones_menu()
        case 100:
            main_menu()
        case _:
            ringing_volume_menu()


def incoming_call_alert_menu():
    menu = """
===== INCOMING CALL ALERT =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            tones_menu()
        case 100:
            main_menu()
        case _:
            incoming_call_alert_menu()


def message_alert_tone_menu():
    menu = """
===== MESSAGE ALERT TONE =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            tones_menu()
        case 100:
            main_menu()
        case _:
            message_alert_tone_menu()


def keypad_tones_menu():
    menu = """
===== KEYPAD TONES =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            tones_menu()
        case 100:
            main_menu()
        case _:
            keypad_tones_menu()


def warning_tones_menu():
    menu = """
===== WARNING TONES =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            tones_menu()
        case 100:
            main_menu()
        case _:
            warning_tones_menu()


def vibrating_alert_menu():
    menu = """
===== VIBRATING ALERT =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            tones_menu()
        case 100:
            main_menu()
        case _:
            vibrating_alert_menu()


def screen_saver_menu():
    menu = """
===== SCREEN SAVER =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            tones_menu()
        case 100:
            main_menu()
        case _:
            screen_saver_menu()


def settings_menu():
    menu = """
===== SETTINGS =====
1. Call settings
2. Phone settings
3. Security settings
4. Restore factory settings
5. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 1:
            call_settings_menu()
        case 2:
            phone_settings_menu()
        case 3:
            security_settings_menu()
        case 4:
            restore_factory_settings_menu()
        case 0:
            main_menu()
        case 100:
            main_menu()
        case _:
            settings_menu()


def call_settings_menu():
    menu = """
===== CALL SETTINGS =====
1. Automatic redial
2. Speed dialling
3. Call waiting options
4. Own number sending
5. Phone line in use
6. Automatic answer
7. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 1:
            automatic_redial_menu()
        case 2:
            speed_dialling_menu()
        case 3:
            call_waiting_options_menu()
        case 4:
            own_number_sending_menu()
        case 5:
            phone_line_in_use_menu()
        case 6:
            automatic_answer_menu()
        case 0:
            settings_menu()
        case 100:
            main_menu()
        case _:
            call_settings_menu()


def automatic_redial_menu():
    menu = """
===== AUTOMATIC REDIAL =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            call_settings_menu()
        case 100:
            main_menu()
        case _:
            automatic_redial_menu()


def speed_dialling_menu():
    menu = """
===== SPEED DIALLING =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            call_settings_menu()
        case 100:
            main_menu()
        case _:
            speed_dialling_menu()


def call_waiting_options_menu():
    menu = """
===== CALL WAITING OPTIONS =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            call_settings_menu()
        case 100:
            main_menu()
        case _:
            call_waiting_options_menu()


def own_number_sending_menu():
    menu = """
===== OWN NUMBER SENDING =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            call_settings_menu()
        case 100:
            main_menu()
        case _:
            own_number_sending_menu()


def phone_line_in_use_menu():
    menu = """
===== PHONE LINE IN USE =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            call_settings_menu()
        case 100:
            main_menu()
        case _:
            phone_line_in_use_menu()


def automatic_answer_menu():
    menu = """
===== AUTOMATIC ANSWER =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            call_settings_menu()
        case 100:
            main_menu()
        case _:
            automatic_answer_menu()


def phone_settings_menu():
    menu = """
===== PHONE SETTINGS =====
1. Language
2. Cell info display
3. Welcome note
4. Network selection
5. Confirm SIM service actions
6. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 1:
            language_menu()
        case 2:
            cell_info_display_menu()
        case 3:
            welcome_note_menu()
        case 4:
            network_selection_menu()
        case 5:
            confirm_sim_service_actions_menu()
        case 0:
            settings_menu()
        case 100:
            main_menu()
        case _:
            phone_settings_menu()


def language_menu():
    menu = """
===== LANGUAGE =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            phone_settings_menu()
        case 100:
            main_menu()
        case _:
            language_menu()


def cell_info_display_menu():
    menu = """
===== CELL INFO DISPLAY =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            phone_settings_menu()
        case 100:
            main_menu()
        case _:
            cell_info_display_menu()


def welcome_note_menu():
    menu = """
===== WELCOME NOTE =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            phone_settings_menu()
        case 100:
            main_menu()
        case _:
            welcome_note_menu()


def network_selection_menu():
    menu = """
===== NETWORK SELECTION =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            phone_settings_menu()
        case 100:
            main_menu()
        case _:
            network_selection_menu()


def confirm_sim_service_actions_menu():
    menu = """
===== CONFIRM SIM SERVICE ACTIONS =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            phone_settings_menu()
        case 100:
            main_menu()
        case _:
            confirm_sim_service_actions_menu()


def security_settings_menu():
    menu = """
===== SECURITY SETTINGS =====
1. PIN code request
2. Call barring service
3. Fixed dialling
4. Closed user group
5. Security level
6. Change access codes
7. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 1:
            pin_code_request_menu()
        case 2:
            call_barring_service_menu()
        case 3:
            fixed_dialling_menu()
        case 4:
            closed_user_group_menu()
        case 5:
            security_level_menu()
        case 6:
            change_access_codes_menu()
        case 0:
            settings_menu()
        case 100:
            main_menu()
        case _:
            security_settings_menu()


def pin_code_request_menu():
    menu = """
===== PIN CODE REQUEST =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            security_settings_menu()
        case 100:
            main_menu()
        case _:
            pin_code_request_menu()


def call_barring_service_menu():
    menu = """
===== CALL BARRING SERVICE =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            security_settings_menu()
        case 100:
            main_menu()
        case _:
            call_barring_service_menu()


def fixed_dialling_menu():
    menu = """
===== FIXED DIALLING =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            security_settings_menu()
        case 100:
            main_menu()
        case _:
            fixed_dialling_menu()


def closed_user_group_menu():
    menu = """
===== CLOSED USER GROUP =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            security_settings_menu()
        case 100:
            main_menu()
        case _:
            closed_user_group_menu()


def security_level_menu():
    menu = """
===== SECURITY LEVEL =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            security_settings_menu()
        case 100:
            main_menu()
        case _:
            security_level_menu()


def change_access_codes_menu():
    menu = """
===== CHANGE ACCESS CODES =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            security_settings_menu()
        case 100:
            main_menu()
        case _:
            change_access_codes_menu()


def restore_factory_settings_menu():
    menu = """
===== RESTORE FACTORY SETTINGS =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            settings_menu()
        case 100:
            main_menu()
        case _:
            restore_factory_settings_menu()


def call_divert_menu():
    menu = """
===== CALL DIVERT =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            main_menu()
        case 100:
            main_menu()
        case _:
            call_divert_menu()


def music_menu():
    menu = """
===== MUSIC =====
1. Music player
2. Radio
3. Recorder
4. Track list
5. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 1:
            music_player_menu()
        case 2:
            radio_menu()
        case 3:
            recorder_menu()
        case 4:
            track_list_menu()
        case 0:
            main_menu()
        case 100:
            main_menu()
        case _:
            music_menu()


def music_player_menu():
    menu = """
===== MUSIC PLAYER =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            music_menu()
        case 100:
            main_menu()
        case _:
            music_player_menu()


def radio_menu():
    menu = """
===== RADIO =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            music_menu()
        case 100:
            main_menu()
        case _:
            radio_menu()


def recorder_menu():
    menu = """
===== RECORDER =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            music_menu()
        case 100:
            main_menu()
        case _:
            recorder_menu()


def track_list_menu():
    menu = """
===== TRACK LIST =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            music_menu()
        case 100:
            main_menu()
        case _:
            track_list_menu()


def games_menu():
    menu = """
===== GAMES =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            main_menu()
        case 100:
            main_menu()
        case _:
            games_menu()


def calculator_menu():
    menu = """
===== CALCULATOR =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            main_menu()
        case 100:
            main_menu()
        case _:
            calculator_menu()


def reminders_menu():
    menu = """
===== REMINDERS =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            main_menu()
        case 100:
            main_menu()
        case _:
            reminders_menu()


def clock_menu():
    menu = """
===== CLOCK =====
1. Alarm clock
2. Clock settings
3. Date setting
4. Stopwatch
5. Countdown timer
6. Auto update of date and time
7. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 1:
            alarm_clock_menu()
        case 2:
            clock_settings_menu()
        case 3:
            date_setting_menu()
        case 4:
            stopwatch_menu()
        case 5:
            countdown_timer_menu()
        case 6:
            auto_update_of_date_and_time_menu()
        case 0:
            main_menu()
        case 100:
            main_menu()
        case _:
            clock_menu()


def alarm_clock_menu():
    menu = """
===== ALARM CLOCK =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            clock_menu()
        case 100:
            main_menu()
        case _:
            alarm_clock_menu()


def clock_settings_menu():
    menu = """
===== CLOCK SETTINGS =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            clock_menu()
        case 100:
            main_menu()
        case _:
            clock_settings_menu()


def date_setting_menu():
    menu = """
===== DATE SETTING =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            clock_menu()
        case 100:
            main_menu()
        case _:
            date_setting_menu()


def stopwatch_menu():
    menu = """
===== STOPWATCH =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            clock_menu()
        case 100:
            main_menu()
        case _:
            stopwatch_menu()


def countdown_timer_menu():
    menu = """
===== COUNTDOWN TIMER =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            clock_menu()
        case 100:
            main_menu()
        case _:
            countdown_timer_menu()


def auto_update_of_date_and_time_menu():
    menu = """
===== AUTO UPDATE OF DATE AND TIME =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            clock_menu()
        case 100:
            main_menu()
        case _:
            auto_update_of_date_and_time_menu()


def profiles_menu():
    menu = """
===== PROFILES =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            main_menu()
        case 100:
            main_menu()
        case _:
            profiles_menu()


def services_menu():
    menu = """
===== SERVICES =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            main_menu()
        case 100:
            main_menu()
        case _:
            services_menu()


def sim_services_menu():
    menu = """
===== SIM SERVICES =====
0. Back
100. Home
Select an option:"""

    user_choice = int(input(menu))

    match user_choice:
        case 0:
            main_menu()
        case 100:
            main_menu()
        case _:
            sim_services_menu()


main_menu()
