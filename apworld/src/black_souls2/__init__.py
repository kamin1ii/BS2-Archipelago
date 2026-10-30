from BaseClasses import ItemClassification
from worlds.AutoWorld import WebWorld, World

from .Items import ITEM_TABLE, ITEM_NAME_TO_ID, BS2Item, FILLER_ITEM_NAME
from .Locations import LOCATION_TABLE, LOCATION_NAME_TO_ID, VICTORY_LOCATION
from . import Regions
from .Regions import create_regions as _create_regions
from .Options import BS2Options
from .Shuffle import BOSSES, ENEMIES

class BS2Web(WebWorld):
    theme = "grass"                                 
    bug_report_page = "https://discord.gg/T5bcsVHByx"                  
    tutorials = []

class _EmptyCollectionState:
    def has(self, item_name, player):
        return False

class BS2World(World):

    game = "black_souls2"                                                 
                                                             
    author: str = "CthulhusShoes / MayruhiShiinamiya / SpearOfLies"
    options_dataclass = BS2Options
    options: BS2Options
    web = BS2Web()

    item_name_to_id = {**ITEM_NAME_TO_ID, **Regions.LOCKED_EVENT_ITEM_IDS}
    location_name_to_id = LOCATION_NAME_TO_ID

                                                                       
                                                                      
                                                                        
                                                                      
                                                                       
                                                                      
                                                                          
                                                                      
                                                                         
                                                                         
                                                                          
                                                                   
                                                             
                                     
    BOSS_SOUL_LOCATIONS = {
        "ASH: Arbiter's Scythe",
        "BFM: Soul of the Bellcaller", "CC: Soul of the Head-Hunting Beast",
        "CR: Soul of Conceit", "CR: Soul of the Jabberwock",
        "CNG: Soul of Florence",
        "CNG: Soul of the Wet Nurses",
        "DS: Soul of the Deep Sea Knight", "FF: Soul of the Bandersnatch",
        "IF: Soul of the Pregnant Cake", "LT: Soul of Distraction",
        "MV: Soul of the Giant's Home", "MW: Soul of the Gray Eagle",
        "OWU: Soul of the Dean", "PoBT: Soul of Queen of Torture Tools",
        "QL: Soul of the Slave Emperor", "QL: Soul of the Slave Empress",
        "RCF: Soul of the Knight of Clubs", "RCF: Soul of the Knight of Hearts",
        "RCF: Soul of the Knight of Spades", "SCT: Soul of the Bright Star",
        "SCT: Soul of the Jubjub", "SF: Soul of the Old Knight",
        "SH: Soul of the Butcher", "SG: Soul of the God's Odd Fish",
        "ULT: Soul of Jack", "WCT: Soul of the Winterbell's Wind",
        "WCT: Soul of the White Lion", "WCT: Soul of the White Unicorn",
    }

                                                                     
                                                                      
                                                                    
                                  
    TALE_LOCATIONS = {
        'BFM: Fairy Tale [Adventures of Sinbad]',
        'BFM: Fairy Tale [The Crab and The Monkey]',
        'CR: Fairy Tale [Dog of Flanders]',
        'CR: Fairy Tale [Goose That Laid Golden Eggs]',
        'CR: Fairy Tale [The Dog and The Shadow]',
        'FF: Fairy Tale [Mt. Kachi Kachi]',
        'FF: Fairy Tale [Robin Hood]',
        "FF: Folk Tale [Jeanne d'Arc]",
        'DS: Fairy Tale [Pinocchio]',
        'GotH: Fairy Tale [The Fox and The Grapes]',
        'IF: Fairy Tale [Hansel and Gretel]',
        'LC: Fairy Tale [Wolf and \u00d7\u00d7\u00d7 Young Goats]',
        'LD: Fairy Tale [Rascal]',
        'LT: Fairy Tale Scrap Three',
        'LT: Fairy Tale Scrap Two',
        'LT: Fairy Tale [The Little Match Girl]',
        'LT: Fairy Tale [The Ugly Duckling]',
        'MW: Fairy Tale [Iron Hans]',
        'MW: Fairy Tale [Wizard of Oz]',
        'NF: Fairy Tale [The Gigantic Turnip]',
        'OWU: Folk Tale [Saint of Alexandria]',
        'PoBT: Fairy Tale [Bluebeard]',
        'PoBT: Folk Tale [Elizabeth Bathory]',
        'QL: Fairy Tale [Daddy-Long-Legs]',
        'QL: Fairy Tale [Pooh Bear]',
        'RCF: Fairy Tale [The King with Donkey Ears]',
        'RH: Fairy Tale [Black Rabbit of Inaba]',
        'SCT: Fairy Tale [The Little Prince]',
        'SF: Fairy Tale [Knight in Armor]',
        'SH: Fairy Tale [Musicians of Bremen]',
        'ULT: Fairy Tale Scrap One',
        'ULT: Fairy Tale [Boy Who Cried Wolf]',
    }

    def create_regions(self) -> None:
        _create_regions(self, self.player)

    def set_rules(self) -> None:
                                                              
                                                                           
                                                               
                                                                  
                                                                        
                                                                       
                                                                     
        DLC_REGIONS = Regions.DLC_REGIONS

        dlc_option = getattr(self.options, "dlc_enabled", None)
        dlc_on = dlc_option.value if dlc_option is not None else True

                                                                         
                                                                     
                                                                        
                                                  
                                                       
                                                                    
                                                           
                                                       
                                                                       
                                                                           
                                                                        
                                                                   
                                                                       
                            
                                                                        
                                                             
         
                                                                     
                                                                      
                                                                         
                                                                     
                                                                   
                                           
        RESTRICTED_ITEM_NAMES = {"Edith's Ring", "Gear of Madness", "Train Ticket",
                                  "Gate Pass", "Blackwell's Letter", "Mystery of Night Sky",
                                  "Leaf's Ring", "Drink Me"}

                                                                        
                                                                        
                                                                
                                                                       
                                                                        
                                                                      
                                                                        
                                                                       
                                                                    
                                    
        DLC_MIST_ITEM_NAMES = {"Mist Crimean Nursing Graveyard", "Mist Florence Arena",
                                "Mist Windless Valley", "Mist Black Knight Arena",
                                "Mist White Castletown"}
        BASE_MIST_ITEM_NAMES = {name for name in ITEM_TABLE
                                 if name.startswith("Mist ") and name not in DLC_MIST_ITEM_NAMES}

                                                                      
                                                                       
                                                                         
                                                                      
                                                                   
                                                                      
                                                                       
                                                                     
                                                                 
        BASE_COVENANT_ITEM_NAMES = {name for name in ITEM_TABLE
                                     if name.startswith("Covenant: ") and name != "Covenant: Sho"}

        ALL_DLC_RESTRICTED_NAMES = RESTRICTED_ITEM_NAMES | BASE_MIST_ITEM_NAMES | BASE_COVENANT_ITEM_NAMES

                                                                         
                                                                       
                                                                         
                                                                  
        if dlc_on:
            for loc_name, data in LOCATION_TABLE.items():
                if loc_name == VICTORY_LOCATION:
                    continue
                if data.region in DLC_REGIONS:
                    location = self.multiworld.get_location(loc_name, self.player)
                    location.item_rule = lambda item, names=ALL_DLC_RESTRICTED_NAMES: item.name not in names

                                                                          
                                                                         
                                                                   
                                                                      
                                                                         
                                                                      
                                                                        
                                                                       
                                                                        
                                                                        
        FRAGILE_CROSSROADS_ITEM_NAMES = {"Mist Crash Chamber", "Mist Dodgson Bridge"}
        pobt_fairy_tale = self.multiworld.get_location(
            "PoBT: Folk Tale [Elizabeth Bathory]", self.player)
        existing_rule = getattr(pobt_fairy_tale, "item_rule", None)
        if existing_rule is not None:
            pobt_fairy_tale.item_rule = lambda item, names=FRAGILE_CROSSROADS_ITEM_NAMES, prev=existing_rule: item.name not in names and prev(item)
        else:
            pobt_fairy_tale.item_rule = lambda item, names=FRAGILE_CROSSROADS_ITEM_NAMES: item.name not in names

                                                                         
                                                                      
                                                                       
                                                                   
                                                                        
                                                                       
                                                                         
                                                                     
                                                                        
                                                                   
                                                                        
         
                                                                    
                                                                         
                                                                         
                                                                
        ALL_MIST_ITEM_NAMES = {name for name in ITEM_TABLE if name.startswith("Mist ")}
        for loc_name in self.BOSS_SOUL_LOCATIONS:
                                                                    
                                                                         
                                                                        
                                                                     
            if not dlc_on and LOCATION_TABLE[loc_name].region in DLC_REGIONS:
                continue
            location = self.multiworld.get_location(loc_name, self.player)
            existing_rule = getattr(location, "item_rule", None)
            if existing_rule is not None:
                location.item_rule = lambda item, names=ALL_MIST_ITEM_NAMES, prev=existing_rule: item.name not in names and prev(item)
            else:
                location.item_rule = lambda item, names=ALL_MIST_ITEM_NAMES: item.name not in names

                                                                        
                                                                        
                                                                      
                                                                   
                                                                  
                                                                       
                                                                        
        ALL_COVENANT_ITEM_NAMES = {name for name in ITEM_TABLE if name.startswith("Covenant: ")}
        TALE_RESTRICTED_NAMES = ALL_MIST_ITEM_NAMES | ALL_COVENANT_ITEM_NAMES
        for loc_name in self.TALE_LOCATIONS:
            location = self.multiworld.get_location(loc_name, self.player)
            existing_rule = getattr(location, "item_rule", None)
            if existing_rule is not None:
                location.item_rule = lambda item, names=TALE_RESTRICTED_NAMES, prev=existing_rule: item.name not in names and prev(item)
            else:
                location.item_rule = lambda item, names=TALE_RESTRICTED_NAMES: item.name not in names

                                                                 
                                                                         
                                                                         
                                                                        
                                                                         
                                                                      
                                                                    
                                                                       
                                                                    
                                                                         
                                                                       
                                                                        
                                                                        
                                                                       
                                                                        
                                     
        RH_FF_RESTRICTED_NAMES = {"Mist Crash Chamber", "Drink Me"}
        RH_FF_REGIONS = {"Rabbit Hole", "Fuming Forest"}
        for r in self.multiworld.regions:
            if r.name not in RH_FF_REGIONS:
                continue
            for location in r.locations:
                existing_rule = getattr(location, "item_rule", None)
                if existing_rule is not None:
                    location.item_rule = lambda item, names=RH_FF_RESTRICTED_NAMES, prev=existing_rule: item.name not in names and prev(item)
                else:
                    location.item_rule = lambda item, names=RH_FF_RESTRICTED_NAMES: item.name not in names

                                                                       
                                                                         
                                                                     
                                                                 
                                                                    
                                                                       
                                                                     
                                                                    
        QL_RESTRICTED_NAMES = {"Mist Queensland", "Covenant: Best Girl Prickett"}
        QL_RESTRICTED_LOCATIONS = {"QL: Soul of the Slave Emperor", "QL: Soul of the Slave Empress"}
        for loc_name in QL_RESTRICTED_LOCATIONS:
            location = self.multiworld.get_location(loc_name, self.player)
            existing_rule = getattr(location, "item_rule", None)
            if existing_rule is not None:
                location.item_rule = lambda item, names=QL_RESTRICTED_NAMES, prev=existing_rule: item.name not in names and prev(item)
            else:
                location.item_rule = lambda item, names=QL_RESTRICTED_NAMES: item.name not in names

    def create_item(self, name: str) -> BS2Item:
                                                                          
                                                                       
                                                                         
                                                                       
                                                                  
                                                                  
                                                                     
                                   
        for event_item_name, event_classification in Regions.LOCKED_EVENTS.values():
            if event_item_name == name:
                code = Regions.LOCKED_EVENT_ITEM_IDS[name]
                classification = getattr(ItemClassification, event_classification)
                return BS2Item(name, classification, code, self.player)
        data = ITEM_TABLE[name]
        return BS2Item(name, data.classification, data.code, self.player)

    def create_items(self) -> None:
        trap_names = [name for name, data in ITEM_TABLE.items()
                      if data.classification == ItemClassification.trap]

                                                                 
                                                                        
                                                                    
                                                                     
                                                                       
                                                                     
        mist_on = getattr(self.options, "mist_randomization", None)
        mist_on = mist_on.value if mist_on is not None else True
        mist_names = [name for name in ITEM_TABLE if name.startswith("Mist ")]

                                                                         
                                                                          
                                                                          
                                                                      
                                                                        
                        
        covenant_on = getattr(self.options, "covenant_gating", None)
        covenant_on = covenant_on.value if covenant_on is not None else True
        covenant_names = [
            "Covenant: Node", "Covenant: Bill", "Covenant: Dodo",
            "Covenant: Tweedledee & Tweedledum", "Covenant: Shisha",
            "Covenant: Mock Turtle", "Covenant: Walrus",
            "Covenant: Queen of Hearts", "Covenant: Hatta", "Covenant: Maid Victoria",
            "Covenant: Best Girl Prickett", "Covenant: Kuti", "Covenant: Bandersnatch",
            "Covenant: Sho", "Covenant: Margaret", "Covenant: Jabberwock",
        ]

                                                                 
                                                                        
                                                                 
                                                                        
                                                                        
                                                                      
                                                               
                                                             
         
                                                                         
                                                                          
                                                                      
                                                                      
                                                                        
                                                                       
                                                                      
                                                                    
                                                                 
                                                                          
                                                                      
                                                                    
                                                               
        dlc_on = getattr(self.options, "dlc_enabled", None)
        dlc_on = dlc_on.value if dlc_on is not None else True
        dlc_only_names = set(Regions.dlc_only_item_names()) if not dlc_on else set()
        dlc_dependent_names = set(Regions.dlc_dependent_item_names()) if not dlc_on else set()

                                                                
                                                                     
                                                                       
                                       
        gear_start = getattr(self.options, "gear_of_madness_start", None)
        gear_start = gear_start.value if gear_start is not None else False

        pool = []
        for name, data in ITEM_TABLE.items():
            if name in dlc_only_names:
                continue
            if name in dlc_dependent_names:
                continue
            if not mist_on and name in mist_names:
                for _ in range(data.count):
                    self.multiworld.push_precollected(self.create_item(name))
                continue
            if not covenant_on and name in covenant_names:
                for _ in range(data.count):
                    self.multiworld.push_precollected(self.create_item(name))
                continue
            if gear_start and name == "Gear of Madness":
                for _ in range(data.count):
                    self.multiworld.push_precollected(self.create_item(name))
                continue
            for _ in range(data.count):
                pool.append(self.create_item(name))

                                                                        
                                                                     
                                                                      
                                                                           
                                                                       
                                                                         
                                                         
        if trap_names and getattr(self.options, "filler_traps", None):
            percent = self.options.filler_traps.value
            if percent > 0:
                filler_indices = [i for i, item in enumerate(pool)
                                   if item.classification == ItemClassification.filler]
                num_to_convert = round(len(filler_indices) * percent / 100)
                chosen = self.random.sample(filler_indices, min(num_to_convert, len(filler_indices)))
                for i in chosen:
                    pool[i] = self.create_item(self.random.choice(trap_names))

                                                                     
                                                                   
                                                                       
                                                                          
        if not mist_on:
            filler_name = self.get_filler_item_name()
            removed_count = sum(ITEM_TABLE[name].count for name in mist_names
                                 if name not in dlc_only_names and name not in dlc_dependent_names)
            for _ in range(removed_count):
                pool.append(self.create_item(filler_name))

                                                                     
                                                                        
                                                                   
                                                                   
                                                                   
                     
        if not covenant_on:
            filler_name = self.get_filler_item_name()
            removed_count = sum(ITEM_TABLE[name].count for name in covenant_names
                                 if name not in dlc_only_names and name not in dlc_dependent_names)
            for _ in range(removed_count):
                pool.append(self.create_item(filler_name))

                                                           
        if gear_start:
            filler_name = self.get_filler_item_name()
            for _ in range(ITEM_TABLE["Gear of Madness"].count):
                pool.append(self.create_item(filler_name))

        self._force_early_items = {}
        force_early_names = ["Mist Crash Chamber", "Mist Dodgson Bridge"]
        if self.options.force_covenant_node_early.value:
            force_early_names.append("Covenant: Node")
        for name in force_early_names:
            idx = next((i for i, item in enumerate(pool) if item.name == name), None)
            if idx is not None:
                self._force_early_items[name] = pool.pop(idx)

        self.multiworld.itempool += pool

    def pre_fill(self) -> None:
                                                                        
                                                                       
                                                                           
                                                                       
                                                                      
                                                                         
                                                                          
         
                                                                          
                                                                     
                                                                        
                                                                        
                                                                         
                                                                  
                                                                
                                                                        
                                                                     
                                                                 
                                                                     
                                                                         
                                                              
                                                                  
         
                                                                       
                                                                        
                                                                      
                                                                     
                                                         
        zero_item_state = _EmptyCollectionState()

        reachable_regions = set()
        stack = [self.multiworld.get_region("Menu", self.player)]
        while stack:
            region = stack.pop()
            if region.name in reachable_regions:
                continue
            reachable_regions.add(region.name)
            for exit_ in region.exits:
                if exit_.connected_region and exit_.access_rule(zero_item_state):
                    stack.append(exit_.connected_region)

        candidate_locations = []
        for region in self.multiworld.regions:
            if region.player != self.player or region.name not in reachable_regions:
                continue
            for location in region.locations:
                if location.item is not None:
                    continue
                if location.name in self.BOSS_SOUL_LOCATIONS or location.name in self.TALE_LOCATIONS:
                    continue
                if not location.access_rule(zero_item_state):
                    continue
                candidate_locations.append(location)
        self.random.shuffle(candidate_locations)

        force_early_items = getattr(self, "_force_early_items", {})

        for item_name in list(force_early_items.keys()):
            item = force_early_items.pop(item_name, None)
            if item is None:
                continue
            if not candidate_locations:
                self.multiworld.itempool.append(item)
                continue
            loc = candidate_locations.pop()
            loc.place_locked_item(item)

    def get_pre_fill_items(self) -> list:
        return list(getattr(self, "_force_early_items", {}).values())

    def get_filler_item_name(self) -> str:
                                                                           
                                                                           
                                                                          
                                                                         
                                                                       
                                                                          
                                                                 
        for name, data in ITEM_TABLE.items():
            if data.classification == ItemClassification.filler:
                return name
        return next(iter(ITEM_TABLE))

    def shuffle_troops(self, pool: list, scale: bool) -> list:
        if not self.options.dlc_enabled:
            pool = [t for t in pool if not t["dlc"]]
        placed = pool[:]
        self.random.shuffle(placed)
        swaps = []
        for slot, troop in zip(pool, placed):
            if slot["troop"] == troop["troop"]:
                continue
            hp, atk = 1.0, 1.0
            if scale:
                hp = max(0.05, min(20.0, slot["hp"] / troop["hp"]))
                atk = max(0.1, min(10.0, slot["atk"] / max(troop["atk"], 1)))
            swaps.append([slot["troop"], troop["troop"], round(hp, 4), round(atk, 4)])
        return swaps

    def fill_slot_data(self) -> dict:
        boss_swaps = self.shuffle_troops(BOSSES, bool(self.options.boss_scaling)) if self.options.boss_shuffle else []
        enemy_swaps = self.shuffle_troops(ENEMIES, True) if self.options.enemy_shuffle else []
        return {
            "boss_shuffle": bool(self.options.boss_shuffle.value),
            "enemy_shuffle": bool(self.options.enemy_shuffle.value),
            "boss_troops": [b["troop"] for b in BOSSES],
            "boss_swaps": boss_swaps,
            "enemy_swaps": enemy_swaps,
            "goal": self.options.goal.current_key,
            "death_link": bool(self.options.death_link.value),
            "auto_meet_red_hood": bool(self.options.auto_meet_red_hood.value),
            "prevent_covenant_purge": bool(self.options.prevent_covenant_purge.value),
            "start_with_run_like_dodo": bool(self.options.start_with_run_like_dodo.value),
            "ring_link": bool(self.options.ring_link.value),
            "ring_link_gold_per_ring": int(self.options.ring_link_gold_per_ring.value),
        }
