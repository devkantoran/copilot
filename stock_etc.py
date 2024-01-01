import string


def money_made(num_shares, purchase_share_price, current_share_price):
    """
    num_shares is the number of shares of a stock that we purchased.
    purchase_share_price is the price of each of those shares.
    current_share_price is the current share price.
    Return the amount of money we have earned on the stock.
    """
    return num_shares * (current_share_price - purchase_share_price)


def is_strong_password(password):
    """
    A strong password has at least one uppercase character,
    at least one number, and at least one punctuation.

    Return True if the password is a strong password, False if not.
    """
    return (
        any(c in string.ascii_uppercase for c in password)
        and any(c in string.digits for c in password)
        and any(c in string.punctuation for c in password)
    )


def get_strong_password():
    """
    Keep asking the user for a password until it is a strong 
    password, and return that strong password.
    """
    password = input("Enter a password: ")
    while not is_strong_password(password):
        print("That password is not strong enough.")
        password = input("Enter a password: ")
    return password

def num_points(word): 
    """ 
    Each letter is worth the following points: 
    a, e, i, o, u, l, n, s, t, r: 1 point 
    d, g: 2 points 
    b, c, m, p: 3 points 
    f, h, v, w, y: 4 points 
    k: 5 points 
    j, x: 8 points 
    q, z: 10 points 

    word is a word consisting of lowercase characters. 
    Return the sum of points for each letter in word. 
    """
    points = 0 
    for letter in word: 
        if letter in "aeioulnstr": 
            points += 1 
        elif letter in "dg": 
            points += 2 
        elif letter in "bcmp": 
            points += 3 
        elif letter in "fhvwy": 
            points += 4 
        elif letter in "k": 
            points += 5 
        elif letter in "jx": 
            points += 8 
        elif letter in "qz": 
            points += 10 
    return points

def best_word(word_list):
    """
    word_list is a list of words.
    
    Return the word worth the most points.
    """
    best_word = None
    best_points = 0
    for word in word_list:
        points = num_points(word)
        if points > best_points:
            best_word = word
            best_points = points
    return best_word