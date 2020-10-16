def convert(number):
    sounds = {3: 'Pling', 5: 'Plang', 7: 'Plong'}
    word = ''
    for factor, sound in sounds.items():
        if number % factor == 0:
            word = word + sound
    
    return word if word else str(number)
