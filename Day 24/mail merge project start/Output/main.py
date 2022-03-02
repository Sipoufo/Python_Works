from file import File

inputTemplate = File('../input/letters/starting_letter.txt')
inputName = File('../input/Names/invited_name.txt')
# output = File('./ReadToSend')

names = inputName.readFileList()
contentLetter = inputTemplate.readFile()

for name in names:
    name = name.strip()
    new_Letter = contentLetter.replace('[name]', name)
    with open(f'./ReadToSend/letter_for_{name}.txt', 'w') as fileOutput:
        fileOutput.write(new_Letter)