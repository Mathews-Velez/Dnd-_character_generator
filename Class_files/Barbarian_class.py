import random 
import Class_files.Weapons
def Barbarian(x):  
    
    #Print breif description
    print('\n\nYour class\n\nBarbarian\n -A fierce warrior of primitive background who can enter a battle rage')
    #Print Class Features
    print('For stat priority, highest stat should be strength followed by Constitution.')
    
    #Hit points
    #Hit Dice: 1d12 per barbarian level
    print('Hit Dice\n -D12')
    #Hit Points at 1st Level: 12 + your Constitution modifier
    print('Hit points at Level 1\n 12 + Constitution_mod')
    #Hit Points at Higher Levels: 1d12 (or 7) + your constitution modifier per barbarian level after 1st
    print('Hit Points at Higher Levels: 1d12 (or 7) + your constitution modifier per barbarian level after 1st')
     
    #Proficiencies
    print('Proficiencies')
    #Armor: Light armor, medium armor, shields
    print('Armour:\n -Light armor, medium armor, shields')
    #Weapons: Simple weapons, martial weapons
    print('Weapons:\n -Simple weapons, martial weapons')
    #Tools: None
    print('Tools:\n -None')
    #Saving Throws: Strength, Constitution
    print('Saving Throws:\n -Strength, Constitution')
    
    #Skills
    skills = ('Animal Handling','Athletics','Intimidation','Nature','Perception','Survival')
    #fetching 2 unique strings from the tuple skills
    chosen_skills = random.sample(skills,2)
    print(f'Skills:\n -{chosen_skills}')
    
    #equipment
    print('Equipment')
    #weapons
    
    print('Weapons')
    
    