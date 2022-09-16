# atbash

def atbash(message):
    alphabet = u'A B C D E F G H I J K L M N Ñ O P Q R S T U V W X Y Z a b c d e f g h i j k l m n ñ o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9'.split()
    backward = u'Z Y X W V U T S R Q P O Ñ N M L K J I H G F E D C B A z y x w v u t s r q p o ñ n m l k j i h g f e d c b a 9 8 7 6 5 4 3 2 1 0'.split()
    cipher = []
    
    for letter in message:
        if letter in alphabet:
            for i in range(len(alphabet)):
                if alphabet[i] == letter:
                    pos = i
            cipher.append(backward[pos])
        else:
            cipher.append(letter)
    
    newMessage = ''.join(cipher)
    return newMessage

crypt = atbash(u'My name is Gaby')
print (crypt)
