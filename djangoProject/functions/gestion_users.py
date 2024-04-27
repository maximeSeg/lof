import sqlite3


def creer_user(riotid, username, password, email):
    if riotid_exists(riotid):
        return False
    else:
        conn = sqlite3.connect('main.user.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO user (RiotID, username, password, email) VALUES (?, ?, ?, ?)",
                       (riotid, username, password, email))
        conn.commit()
        conn.close()
        return True


def riotid_exists(riotid):
    conn = sqlite3.connect('main.user.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user WHERE RiotID = ?", (riotid,))
    result = cursor.fetchone()
    conn.close()
    return result is not None


def user_is_logged_in(request):
    if request.user.is_authenticated:
        return True
    else:
        return False
