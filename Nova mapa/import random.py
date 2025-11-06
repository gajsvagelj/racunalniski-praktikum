import random
import json

class TriviadorGame:
    def __init__(self):
        self.players = []
        self.territories = {}
        self.questions = self.load_questions()
        self.categories = list(set([q['category'] for q in self.questions]))
        
    def load_questions(self):
        """Naloži vprašanja v slogu Kviza Milijonar"""
        questions = [
            {
                'question': 'Katera je glavno mesto Slovenije?',
                'options': ['Ljubljana', 'Maribor', 'Koper', 'Celje'],
                'correct_answer': 'Ljubljana',
                'category': 'Geografija',
                'difficulty': 1
            },
            {
                'question': 'Koliko je 5 × 7?',
                'options': ['35', '30', '42', '28'],
                'correct_answer': '35',
                'category': 'Matematika',
                'difficulty': 1
            },
            {
                'question': 'Kdo je napisal Romeo in Julijo?',
                'options': ['William Shakespeare', 'Charles Dickens', 'Jane Austen', 'Mark Twain'],
                'correct_answer': 'William Shakespeare',
                'category': 'Literatura',
                'difficulty': 2
            },
            {
                'question': 'Katera planeta sta znana kot dvojčka?',
                'options': ['Zemlja in Mars', 'Venera in Mars', 'Uran in Neptun', 'Merkur in Venera'],
                'correct_answer': 'Uran in Neptun',
                'category': 'Znanost',
                'difficulty': 3
            },
            {
                'question': 'V katerem letu je potekala bitka pri Mohaču?',
                'options': ['1526', '1456', '1683', '1815'],
                'correct_answer': '1526',
                'category': 'Zgodovina',
                'difficulty': 4
            }
        ]
        return questions

    def initialize_game(self, player_names):
        """Inicializiraj igro z igralci in ozemlji"""
        self.players = [{'name': name, 'score': 1000, 'territories': []} for name in player_names]
        
        # Ustvari ozemlja
        territories = ['Sever', 'Jug', 'Vzhod', 'Zahod', 'Center', 'Otočje', 'Gorovje', 'Pustinja']
        for territory in territories:
            self.territories[territory] = {'owner': None, 'troops': 0}

    def assign_initial_territories(self):
        """Naključno dodeli začetna ozemlja igralcem"""
        available_territories = list(self.territories.keys())
        random.shuffle(available_territories)
        
        for i, territory in enumerate(available_territories):
            if i < len(self.players):
                owner = self.players[i % len(self.players)]
                self.territories[territory]['owner'] = owner['name']
                owner['territories'].append(territory)
                self.territories[territory]['troops'] = 10

    def display_map(self):
        """Prikaži trenutno stanje zemljevida"""
        print("\n" + "="*50)
        print("TEKOČE STANJE ZEMLJEVIDA")
        print("="*50)
        
        for territory, info in self.territories.items():
            owner = info['owner'] if info['owner'] else 'Brez lastnika'
            troops = info['troops']
            print(f"{territory}: {owner} ({troops} enot)")
        
        print("\nSTATISTIKA IGRALCEV:")
        for player in self.players:
            print(f"{player['name']}: {player['score']} točk, {len(player['territories'])} ozemelj")

    def ask_question(self, category=None):
        """Postavi vprašanje v slogu Kviza Milijonar"""
        if category:
            available_questions = [q for q in self.questions if q['category'] == category]
        else:
            available_questions = self.questions
            
        if not available_questions:
            available_questions = self.questions
            
        question_data = random.choice(available_questions)
        
        print(f"\nKATEGORIJA: {question_data['category']}")
        print(f"VPRAŠANJE: {question_data['question']}")
        print("MOŽNOSTI:")
        
        options = question_data['options'][:]
        random.shuffle(options)
        
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
            
        return question_data, options

    def battle(self, attacker, defender, territory):
        """Izvedi bitko med dvema igralcema"""
        print(f"\n  BITKA: {attacker['name']} napada {defender['name']} na ozemlju {territory}")
        
        # Izberi kategorijo
        print("\nIzberi kategorijo za bitko:")
        for i, category in enumerate(self.categories, 1):
            print(f"{i}. {category}")
        
        try:
            choice = int(input("Tvoja izbira (1-{}): ".format(len(self.categories)))) - 1
            selected_category = self.categories[choice]
        except:
            selected_category = random.choice(self.categories)
        
        # Postavi vprašanje obema igralcema
        question_data, shuffled_options = self.ask_question(selected_category)
        correct_answer = question_data['correct_answer']
        
        # Simuliraj odgovor napadalca (igralec)
        print(f"\n{attacker['name']}, odgovori:")
        try:
            attacker_choice = int(input("Tvoj odgovor (1-4): ")) - 1
            attacker_answer = shuffled_options[attacker_choice]
        except:
            attacker_answer = random.choice(shuffled_options)
        
        # Simuliraj odgovor branilca (računalnik)
        defender_answer = random.choice(shuffled_options)
        # Računalnik ima 70% verjetnost za pravilen odgovor
        if random.random() < 0.7:
            defender_answer = correct_answer
            
        print(f"{defender['name']} odgovori: {defender_answer}")
        
        # Ovrednoti bitko
        attacker_correct = attacker_answer == correct_answer
        defender_correct = defender_answer == correct_answer
        
        if attacker_correct and not defender_correct:
            print(f" {attacker['name']} zmaguje bitko!")
            return 'attacker'
        elif defender_correct and not attacker_correct:
            print(f" {defender['name']} zmaguje bitko!")
            return 'defender'
        elif attacker_correct and defender_correct:
            print(" Neodločeno - oba imata prav!")
            return 'draw'
        else:
            print(" Oba nista pravilno odgovorila!")
            return 'none'

    def play_round(self, current_player_index):
        """Izvedi eno rundo za igralca"""
        current_player = self.players[current_player_index]
        print(f"\n{'='*60}")
        print(f"NA VREDI JE: {current_player['name']}")
        print(f"{'='*60}")
        
        self.display_map()
        
        # Izberi akcijo
        print(f"\n{current_player['name']}, izberi akcijo:")
        print("1. Napadi ozemlje")
        print("2. Okrepi svoja ozemlja (cena: 100 točk)")
        print("3. Pridobi nova vprašanja (cena: 50 točk)")
        
        try:
            action = int(input("Tvoja izbira (1-3): "))
        except:
            action = 1
        
        if action == 1:  # Napad
            # Izberi ciljno ozemlje
            available_targets = [t for t, info in self.territories.items() 
                               if info['owner'] != current_player['name'] and info['owner'] is not None]
            
            if not available_targets:
                print("Ni več ozemelj za napad!")
                return
                
            print("\nIzberi ozemlje za napad:")
            for i, territory in enumerate(available_targets, 1):
                owner = self.territories[territory]['owner']
                print(f"{i}. {territory} (lastnik: {owner})")
            
            try:
                target_choice = int(input("Tvoja izbira (1-{}): ".format(len(available_targets)))) - 1
                target_territory = available_targets[target_choice]
            except:
                target_territory = random.choice(available_targets)
            
            defender_name = self.territories[target_territory]['owner']
            defender = next((p for p in self.players if p['name'] == defender_name), None)
            
            if defender:
                result = self.battle(current_player, defender, target_territory)
                
                if result == 'attacker':
                    # Napadalec osvoji ozemlje
                    self.territories[target_territory]['owner'] = current_player['name']
                    current_player['territories'].append(target_territory)
                    defender['territories'].remove(target_territory)
                    self.territories[target_territory]['troops'] = 15
                    current_player['score'] += 200
                    print(f" {current_player['name']} osvoji {target_territory}!")
                    
                elif result == 'defender':
                    # Branilec obdrži ozemlje
                    self.territories[target_territory]['troops'] += 5
                    defender['score'] += 100
                    print(f" {defender['name']} uspešno brani {target_territory}!")
        
        elif action == 2:  # Okrepi
            if current_player['score'] >= 100:
                current_player['score'] -= 100
                territory_to_boost = random.choice(current_player['territories'])
                self.territories[territory_to_boost]['troops'] += 10
                print(f" Okrepil si {territory_to_boost} z 10 novimi enotami!")
        
        elif action == 3:  # Nova vprašanja
            if current_player['score'] >= 50:
                current_player['score'] -= 50
                new_questions = [
                    {
                        'question': 'Kateri element ima kemijsko oznako Au?',
                        'options': ['Zlato', 'Srebro', 'Baker', 'Železo'],
                        'correct_answer': 'Zlato',
                        'category': 'Znanost',
                        'difficulty': 2
                    },
                    {
                        'question': 'Kdo je naslikal Mono Liso?',
                        'options': ['Leonardo da Vinci', 'Michelangelo', 'Rafael', 'Donatello'],
                        'correct_answer': 'Leonardo da Vinci',
                        'category': 'Umetnost',
                        'difficulty': 2
                    }
                ]
                self.questions.extend(new_questions)
                print(" Dodanih 2 novi vprašanji v bazo!")

    def check_win_condition(self):
        """Preveri, ali je kdo osvojil vse ozemlje"""
        for player in self.players:
            if len(player['territories']) == len(self.territories):
                return player
        return None

    def start_game(self):
        """Zaženi glavno zanko igre"""
        print(" DOBRODOŠLI V TRIVIADOR - KVIZ MILIJONAR BITKI!")
        print("="*60)
        
        # Nastavi igralce
        num_players = int(input("Vnesi število igralcev (2-4): ") or "2")
        player_names = []
        
        for i in range(num_players):
            name = input(f"Ime igralca {i+1}: ") or f"Igralec {i+1}"
            player_names.append(name)
        
        # Dodaj računalniške igralce, če je treba
        if num_players < 4:
            computer_names = ['Računalnik 1', 'Računalnik 2', 'Računalnik 3']
            for i in range(4 - num_players):
                player_names.append(computer_names[i])
        
        self.initialize_game(player_names)
        self.assign_initial_territories()
        
        # Glavna zanka igre
        round_count = 0
        while True:
            round_count += 1
            print(f"\n{'#'*60}")
            print(f"RONDA {round_count}")
            print(f"{'#'*60}")
            
            for i in range(len(self.players)):
                self.play_round(i)
                
                winner = self.check_win_condition()
                if winner:
                    print(f"\n {winner['name']} JE ZMAGOVALEC! ")
                    print(f"Osvojil si vseh {len(self.territories)} ozemelj!")
                    self.display_map()
                    return
            
            # Po vsaki rundi dodaj točke
            for player in self.players:
                player['score'] += 50 + len(player['territories']) * 20

# Zaženi igro
if __name__ == "__main__":
    game = TriviadorGame()
    game.start_game()