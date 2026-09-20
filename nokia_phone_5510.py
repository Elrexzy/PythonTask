main_menu = """
================================================
             WELCOME TO NOKIA
================================================
Press [Menu] and Select an [Option]

1  Phone book
2  Messages
3  Chat
4  Call register
5  Tones
6  Settings
7  Call divert
8  Music
9  Games
10 Calculator
11 Reminders
12 Clock
13 Profiles
14 Services
15 SIM services
================================================
"""

print(main_menu)

menu_choice = int(input("Enter your choice: "))

match menu_choice:
    case 1:

        print("Phone book")

        phone_book = """
        Press [Menu] and Select an [Option]

        1. Search
        2. Service Nos. 1
        3. Add name
        4. Erase
        5. Edit
        6. Copy
        7. Assign tone
        8. Send b'card
        9. Options
        10. Speed dials
        11. Voice tags
        """

        print(phone_book)

        phone_book_choice = int(input("Enter your choice: "))

        match phone_book_choice:

            case 1:
                print("Search")

            case 2:
                print("Service Nos. 1")

            case 3:
                print("Add name")

            case 4:
                print("Erase")

            case 5:
                print("Edit")

            case 6:
                print("Copy")

            case 7:
                print("Assign tone")

            case 8:
                print("Send b'card")

            case 9:

                print("""
                ============================================
                       Select an [Option]
                ============================================
                1. Memory in use
                2. Type of view
                3. Memory status
                """)

                options = int(input("Enter your choice: "))

                match options:

                    case 1:
                        print("Memory in use")

                    case 2:
                        print("Type of view")

                    case 3:
                        print("Memory status")

                    case _:
                        print("Invalid option")

            case 10:
                print("Speed dials")

            case 11:
                print("Voice tags")

            case _:
                print("Invalid Phone Book option")

    case 2:

        print("Messages")

        messages = """
        ============================================
                      MESSAGES
        ============================================
        Press [Menu] and Select an [Option]

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
        """

        print(messages)

        message_choice = int(input("Enter your choice: "))

        match message_choice:

            case 1:
                print("Write messages")

            case 2:
                print("Inbox")

            case 3:
                print("Outbox")

            case 4:
                print("Picture messages")

            case 5:
                print("Templates")

            case 6:
                print("Smileys")

            case 7:

                print("""
                ============================================
                      Select [Message settings]
                ============================================
                1. Set 1
                2. Common
                """)

                message_settings = int(input("Enter your choice: "))

                match message_settings:

                    case 1:

                        print("""
                        ============================================
                              Set 1 [select an option]
                        ============================================
                        1. Message centre number
                        2. Messages sent as
                        3. Message validity
                        """)

                        set1_choice = int(input("Enter your choice: "))

                        match set1_choice:

                            case 1:
                                print("Message centre number")

                            case 2:
                                print("Messages sent as")

                            case 3:
                                print("Message validity")

                            case _:
                                print("Invalid option")

                    case 2:

                        print("""
                        ============================================
                              Common [select an option]
                        ============================================
                        1. Delivery reports
                        2. Reply via same centre
                        3. Character support
                        """)

                        common_choice = int(input("Enter your choice: "))

                        match common_choice:

                            case 1:
                                print("Delivery reports")

                            case 2:
                                print("Reply via same centre")

                            case 3:
                                print("Character support")

                            case _:
                                print("Invalid option")

                    case _:
                        print("Invalid Message Settings option")

            case 8:
                print("Info service")

            case 9:
                print("Voice mailbox number")

            case 10:
                print("Service command editor")

            case _:
                print("Invalid Messages option")

    case 3:
        print("Chat")

    case 4:

        print("Call register")

        call_register = """
        =====================================================
                 Select call [Options]
        =====================================================
        1. Missed calls
        2. Received calls
        3. Dialled numbers
        4. Erase recent call lists
        5. Show call duration
        6. Show call costs
        7. Call cost settings
        8. Prepaid credit
        """

        print(call_register)

        call_options = int(input("Enter your choice: "))

        match call_options:

            case 1:
                print("Missed calls")

            case 2:
                print("Received calls")

            case 3:
                print("Dialed numbers")

            case 4:
                print("Erase recent call lists")

            case 5:

                print("""
                ============================================
                    Show call duration [select]
                ============================================
                1. Last call duration
                2. All calls' duration
                3. Received calls' duration
                4. Dialled calls' duration
                5. Clear timers
                """)

                show_call_duration = int(input("Enter your choice: "))

                match show_call_duration:

                    case 1:
                        print("Last call duration")

                    case 2:
                        print("All calls' duration")

                    case 3:
                        print("Received calls' duration")

                    case 4:
                        print("Dialled calls' duration")

                    case 5:
                        print("Clear timers")

                    case _:
                        print("Invalid option")

            case 6:

                print("""
                ============================================
                    Show call cost [select]
                ============================================
                1. Last call cost
                2. All calls' cost
                3. Clear counters
                """)

                show_call_cost = int(input("Enter your choice: "))

                match show_call_cost:

                    case 1:
                        print("Last call cost")

                    case 2:
                        print("All calls' cost")

                    case 3:
                        print("Clear counters")

                    case _:
                        print("Invalid option")

            case 7:

                print("""
                ============================================
                    Call cost settings [select]
                ============================================
                1. Call cost limit
                2. Show costs in
                """)

                call_cost_settings = int(input("Enter your choice: "))

                match call_cost_settings:

                    case 1:
                        print("Call cost limit")

                    case 2:
                        print("Show cost in")

                    case _:
                        print("Invalid option")

            case 8:
                print("Prepaid credit")

            case _:
                print("Invalid option")

    case 5:

        print("Tones")

        tones = """
        =====================================================
                         [Options]
        =====================================================
        1. Ringing tone
        2. Ringing volume
        3. Incoming call alert
        4. Message alert tone
        5. Keypad tones
        6. Warning tones
        7. Vibrating alert
        8. Screen saver
        """

        print(tones)

        tone_choices = int(input("Enter your choice: "))

        match tone_choices:

            case 1:
                print("Ringing tone")

            case 2:
                print("Ringing volume")

            case 3:
                print("Incoming call alert")

            case 4:
                print("Message alert tone")

            case 5:
                print("Keypad tones")

            case 6:
                print("Warning tones")

            case 7:
                print("Vibrating alert")

            case 8:
                print("Screen saver")

            case _:
                print("Invalid option")

    case 6:

        print("""
        =====================================================
                   Settings select an [option]
        =====================================================
        1. Call settings
        2. Phone settings
        3. Security settings
        4. Restore factory settings
        """)

        settings = int(input("Enter your choice: "))

        match settings:
            case 1:

                print("""
                ======================================================
                       Call settings select an [option]
                ======================================================
                1. Automatic redial
                2. Speed dialling
                3. Call waiting options
                4. Own number sending
                5. Phone line in use
                6. Automatic answer
                """)

                call_settings = int(input("Enter your choice: "))

                match call_settings:

                    case 1:
                        print("Automatic redial")

                    case 2:
                        print("Speed dialling")

                    case 3:
                        print("Call waiting options")

                    case 4:
                        print("Own number sending")

                    case 5:
                        print("Phone line in use")

                    case 6:
                        print("Automatic answer")

                    case _:
                        print("Invalid option")

            case 2:

                print("""
                ===============================================================
                       Phone settings select an [option]
                ===============================================================
                1. Language
                2. Cell info display
                3. Welcome note
                4. Network selection
                5. Confirm SIM service actions
                """)

                phone_settings = int(input("Enter your choice: "))

                match phone_settings:

                    case 1:
                        print("Language")

                    case 2:
                        print("Cell info display")

                    case 3:
                        print("Welcome note")

                    case 4:
                        print("Network selection")

                    case 5:
                        print("Confirm SIM service actions")

                    case _:
                        print("Invalid option")

            case 3:

                print("""
                =====================================================================
                       Security settings select an [option]
                =====================================================================
                1. PIN code request
                2. Call barring service
                3. Fixed dialling
                4. Closed user group
                5. Security level
                6. Change access codes
                """)

                security_settings = int(input("Enter your choice: "))

                match security_settings:

                    case 1:
                        print("PIN code request")

                    case 2:
                        print("Call barring service")

                    case 3:
                        print("Fixed dialling")

                    case 4:
                        print("Closed user group")

                    case 5:
                        print("Security level")

                    case 6:
                        print("Change access codes")

                    case _:
                        print("Invalid option")


            case 4:
                print("Restore factory settings")

            case _:
                print("Invalid Settings option")

    case 7:
        print("Call divert")

    case 8:

        print("Music")

        music = """
        ==============================================
                       Music [Options]
        ==============================================
        1. Music player
        2. Radio
        3. Recorder
        4. Track list
        """

        print(music)

        music_option = int(input("Enter your choice: "))

        match music_option:

            case 1:
                print("Music player")

            case 2:
                print("Radio")

            case 3:
                print("Recorder")

            case 4:
                print("Track list")

            case _:
                print("Invalid option")

    case 9:
        print("Games")

    case 10:
        print("Calculator")

    case 11:
        print("Reminders")

    case 12:

        print("Clock")

        print("""
        =================================================
                         Clock [options]
        =================================================
        1. Alarm clock
        2. Clock settings
        3. Date setting
        4. Stopwatch
        5. Countdown timer
        6. Auto update of date and time
        """)

        clock_options = int(input("Enter your choice: "))

        match clock_options:

            case 1:
                print("Alarm clock")

            case 2:
                print("Clock settings")

            case 3:
                print("Date setting")

            case 4:
                print("Stopwatch")

            case 5:
                print("Countdown timer")

            case 6:
                print("Auto update of date and time")

            case _:
                print("Invalid option")

    case 13:
        print("Profiles")

    case 14:
        print("Services")

    case 15:
        print("SIM services")

    case _:
        print("Invalid main menu option")
