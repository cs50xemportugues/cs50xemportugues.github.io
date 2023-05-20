Cybersecurity
=============

*   [Cybersecurity](#cybersecurity-1)
*   [Passwords](#passwords)
*   [Phone Security](#phone-security)
*   [Two-factor Authentication](#two-factor-authentication)
*   [Password Managers](#password-managers)
*   [Encryption](#encryption)
*   [Incognito Mode](#incognito-mode)
*   [Summing Up](#summing-up)

Cybersecurity
-------------

*   Today will be a high-level overview of some of the cybersecurity-related topics that are discussed in our course, CS50.

Passwords
---------

*   Passwords are one method used to secure data online.
*   There are common passwords that people use:
    
        1. 123456
        2. 123456789
        3. 12345
        4. qwerty
        5. password
        6. 12345678
        7. 11111
        8. 123123
        9. 1234567890
        10. 1234567
        
    
*   If you have one of the passwords above, most likely, millions of people have the same password as you!
*   Adversaries in the world will start this list.
*   Bad guys can also guess most of the heuristics you use to add symbols to your password.
*   Your password is likely not likely as secure as you think it is.

Phone Security
--------------

*   Many phones are secured by a four-digit code.
*   The most simple form of attack would be to “brute-force” type all possible passwords.
*   There are 10,000 possible passwords when using a four-digit code.
*   If it takes one guess per second, it will take 10,000 seconds to crack the password.
*   However, if a programmer creates a program to generate all possible codes, the time required would be minimal. Consider the following code in Python:
    
        from string import digits
        from itertools import product
        
        for passcode in product(digits, repeat=4):
            print(*passcode)
        
    
*   It should be quite disconcerting that the code above could take only a few seconds (at most!) to discover your password.
*   We could improve our security by switching to a four-letter password. This would result in 7,311,616 possible passwords.
*   Including uppercase and lowercase characters would create over 78 million possibilities.
*   Consider how we could modify your code to discover these passwords:
    
        from string import ascii_letters
        from itertools import product
        
        for passcode in product(ascii_letters, repeat=4):
            print(*passcode)
        
    
*   We could even add the ability to look at all possible four-digit passwords with letters, numbers, and punctations:
    
        from string import ascii_letters, digits, punctuation
        from itertools import product
        
        for passcode in product(ascii_letters + digits + punctuation, repeat=4):
            print(*passcode)
        
    
*   Expanding to eight characters, including upper and lowercase letters, numbers, and symbols, would result in 6,095,689,385,410,816 possible combinations.
*   Consider how the following code could look through all possibilities as follows:
    
        from string import ascii_letters, digits, punctuation
        from itertools import product
        
        for passcode in product(ascii_letters + digits + punctuation, repeat=8):
            print(*passcode)
        
    
*   In the digital world, you simply want your password to be better than other peoples’ passwords such that others would be attacked far before you—as you are a much least convenient target.
*   A downside of using such a long password is the downside of having to remember it.
*   Accordingly, there are other defenses that could be employed to slow down an attacker. For example, some phone manufacturers lock out those that guess a password incorrectly.
*   Security is about finding a “sweet spot” between the trade-offs of enhanced security while maintaining convenience.

Two-factor Authentication
-------------------------

*   Adding another means by which you must authenticate adds further security. However, there is a human cost as you might not have access to your second factor.
*   Always, security policy attempt to balance the needs of security and human convenience.

Password Managers
-----------------

*   Password managers can be used to create very challenging passwords and remember them for you.
*   The probability of a password secured by a password manager being broken is very, very low.
*   You’d hope that such password managers are secure. However, if one gains access to your password manager, they would have access to all your passwords.
*   In the end, you are far less likely to be at risk by those you live with—and much more likely to be at risk by the billions of other people on the internet.
*   As mentioned prior, you can make a decision based on a balance between security and convenience.

Encryption
----------

*   Encryption is a way by which data is obscured such that only the sender and intended receiver can be read.
*   Early in this course, we learned a very simple algorithm to “shift” the text by one or more characters as a rudimentary form of encryption.
*   End-to-end encryption is a way by which encrypting and decrypting happens on the same system without a middleman. This prevents the middleman or a malicious actor from being able to snoop on your data.
*   Full-disk encryption is a way by which the contents of your device are only able to able to be opened without a password. You should absolutely enable this feature on your computer (but don’t forget the password!).
*   Ransomware is a malicious attack where your data is encrypted by an adversary. Quite literally, someone holds your data for ransom.

Incognito Mode
--------------

*   In Chrome, incognito mode prevents your computer from recalling what websites you have browsed and throws away any locally stored information about these websites. Cookies, a small file that is used to track your website visits, are discarded in incognito mode.

Summing Up
----------

*   Use a password manager.
*   Use two-factor authentication.
*   Use (end-to-end) encryption.