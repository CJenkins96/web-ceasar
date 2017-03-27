def alpha_posistion(char):
    alpha_pos = "abcdefghijklmnopqrstuvwxyz"
    rotate = alpha_pos.find(char)
    return rotate 

def rotate_by(char, rot):
    alpha_rot = "abcdefghijklmnopqrstuvwxyz"
    return alpha_rot[(alpha_posistion(char) + rot) % 26]

def encrypt(text, rot):
    rot_message = ""
    text = text.lower()
    for i in text:
        if i.isalpha():
            rot_message += rotate_by(i, rot)
        else:
            rot_message += i
    return rot_message.capitalize()