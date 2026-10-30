from BaseClasses import Region
from .Locations import LOCATION_TABLE, BS2Location, VICTORY_LOCATION
from .Rules import REGION_RULE_SRC, LOCATION_RULE_SRC, compile_rule
from .Items import ITEM_TABLE

REGION_CONNECTIONS = {
    'Crash Chamber': ['Rabbit Hole', 'Pond of Bloody Tears', 'Lutwidge Town', 'Crash Chamber Arena'],
    'Rabbit Hole': ['Fuming Forest', 'Mental Ward'],
    'Library Dream': [],
    'Pond of Bloody Tears': ['Spore Forest', 'Liddell Cemetary', 'Nameless Forest'],
    'Fuming Forest': ['Rabbit Hole', 'Billingsgate Fish Market'],
    'Spore Forest': ['Mushroom Village', "Duchess' Mansion"],
    'Mushroom Village': [],
    'Liddell Cemetary': ['Pond of Bloody Tears', 'Ripon Grand Cathedral', 'Lutwidge Town', 'Garden of the Heart'],
    'Ripon Grand Cathedral': [],
    'Lutwidge Town': ['Park of Fog', 'Billingsgate Fish Market', 'Mental Ward'],
    'Mental Ward': ['Lutwidge Town'],
    'Park of Fog': ['Upper Lutwidge Town'],
    'Upper Lutwidge Town': ['Ox Ward University'],
    'Ox Ward University': ['Carroll River', 'Endless Tea Party'],
    'Carroll River': ['Ox Ward University', 'Hidden Snow Garden', 'Riverside'],
    'Hidden Snow Garden': ['Crimean Nursing Graveyard'],
    'Crimean Nursing Graveyard': ['Florence Arena'],
    'White Castletown': ['Black Knight Arena'],
    'Winterbell': [],
    'Slaughterhouse': ['Carroll River', 'Ox Ward University'],
    'Billingsgate Fish Market': ['Fuming Forest', 'Slaughterhouse', 'Beach of Grief'],
    'Sick Clock Tower': ["Jubjub's Nest"],
    'Nameless Forest': ['Abandoned Station Hanover'],
    'Abandoned Station Hanover': ['Queensland'],
    'Queensland': ['Chaos Dungeon'],
    'Garden of the Heart': ['Red Castle Frissel'],
    'Red Castle Frissel': [],
    "Duchess' Mansion": ['Infinite Food'],
    'Infinite Food': [],
    'Beach of Grief': ["Oysters' Rotted Sea"],
    "Oysters' Rotted Sea": ['Ship Graveyard'],
    'Ship Graveyard': ['Deep Sea'],
    'Deep Sea': [],
    'Chaos Dungeon': [],
    'Florence Arena': ['Windless Valley'],
    'Windless Valley': ['White Castletown'],
    'Black Knight Arena': ['Winterbell'],
    "Jubjub's Nest": [],
    'Riverside': ["Jabberwock's Lair"],
    "Jabberwock's Lair": [],
    'Crash Chamber Arena': [],
    'Endless Tea Party': ['Sick Clock Tower'],
}

STARTING_REGIONS = ['Crash Chamber', 'Library Dream']

LOCKED_EVENTS = {'CC: Entered Rabbit Hole': ('Entered Rabbit Hole', 'progression'), 'OWU: Through Oxward Gate': ('Through Oxward Gate', 'progression'), 'PoBT: Door to Elizabeth': ('Door to Elizabeth', 'progression'), 'LT: Door to PoF': ('Door to PoF', 'progression'), 'LD: Progression 1': ('Progression 1', 'progression'), 'LD: Progression 2': ('Progression 2', 'progression'), 'LD: Progression 3': ('Progression 3', 'progression'), 'LD: Progression 4': ('Progression 4', 'progression'), 'LD: Progression 5': ('Progression 5', 'progression'), 'LD: Progression 6': ('Progression 6', 'progression'), 'LD: Progression 7': ('Progression 7', 'progression'), 'LD: Progression 8': ('Progression 8', 'progression'), 'LD: Progression 9': ('Progression 9', 'progression'), 'LD: Progression 10': ('Progression 10', 'progression'), 'LD: Ending G Achieved': ('Ending G Achieved', 'progression'), 'FF: Elevator to BFM': ('Elevator to BFM', 'progression'), 'ASH: Defeated Hein': ('Defeated Hein', 'progression'), 'CR: Alice Flame': ('Alice Flame CR', 'progression'), 'BoG: Alice Flame': ('Alice Flame BoG', 'progression'), 'RCF: Alice Flame': ('Alice Flame RCF', 'progression'), 'OWU: Alice Flame': ('Alice Flame OWU', 'progression'), 'ETP: Alice Flame': ('Alice Flame ETP', 'progression'), 'QL: Alice Flame': ('Alice Flame QL', 'progression'), 'BS2: Red Hood Met 1': ('Red Hood Met 1', 'progression'), 'BS2: Red Hood Met 2': ('Red Hood Met 2', 'progression'), 'BS2: Red Hood Met 3': ('Red Hood Met 3', 'progression'), 'BS2: Red Hood Met 4': ('Red Hood Met 4', 'progression'), 'BS2: Red Hood Met 5': ('Red Hood Met 5', 'progression'), 'BS2: Red Hood Met 6': ('Red Hood Met 6', 'progression'), 'BS2: Red Hood Met 7': ('Red Hood Met 7', 'progression'), 'BS2: Red Hood Met 8': ('Red Hood Met 8', 'progression'), 'BS2: Red Hood Met 9': ('Red Hood Met 9', 'progression'), 'BS2: Red Hood Met 10': ('Red Hood Met 10', 'progression'), 'LD: Ending G Obtainable': ('Ending G Obtainable', 'progression')}
LOCKED_EVENT_ITEM_IDS = {'Entered Rabbit Hole': 396500350, 'Through Oxward Gate': 396500351, 'Door to Elizabeth': 396500352, 'Door to PoF': 396500353, 'Progression 1': 396500354, 'Progression 2': 396500355, 'Progression 3': 396500356, 'Progression 4': 396500357, 'Progression 5': 396500358, 'Progression 6': 396500359, 'Progression 7': 396500360, 'Progression 8': 396500361, 'Progression 9': 396500362, 'Progression 10': 396500363, 'Ending G Achieved': 396500364, 'Elevator to BFM': 396500365, 'Defeated Hein': 396500366, 'Alice Flame CR': 396500367, 'Alice Flame BoG': 396500368, 'Alice Flame RCF': 396500369, 'Alice Flame OWU': 396500370, 'Alice Flame ETP': 396500371, 'Alice Flame QL': 396500372, 'Red Hood Met 1': 396500373, 'Red Hood Met 2': 396500374, 'Red Hood Met 3': 396500375, 'Red Hood Met 4': 396500376, 'Red Hood Met 5': 396500377, 'Red Hood Met 6': 396500378, 'Red Hood Met 7': 396500379, 'Red Hood Met 8': 396500380, 'Red Hood Met 9': 396500381, 'Red Hood Met 10': 396500382, 'Ending G Obtainable': 396500383}

                                                                   
                                                                      
                                                                    
DLC_REGIONS = {
    "Hidden Snow Garden", "Crimean Nursing Graveyard", "Florence Arena",
    "Windless Valley", "White Castletown", "Black Knight Arena", "Winterbell",
}

def _location_item_name(loc_name):
    suffix = loc_name.split(": ", 1)[-1] if ": " in loc_name else loc_name
    if suffix in ITEM_TABLE:
        return suffix
    for item_name in ITEM_TABLE:
        if suffix.startswith(item_name + " ("):
            return item_name
    return None

def dlc_only_item_names():
    dlc_sourced = set()
    non_dlc_sourced = set()
    for loc_name, data in LOCATION_TABLE.items():
        if loc_name == VICTORY_LOCATION or loc_name in LOCKED_EVENTS:
            continue
        item_name = _location_item_name(loc_name)
        if item_name is None:
            continue
        if data.region in DLC_REGIONS:
            dlc_sourced.add(item_name)
        else:
            non_dlc_sourced.add(item_name)
    return dlc_sourced - non_dlc_sourced

def dlc_dependent_location_names():
    dlc_only = dlc_only_item_names()
    dependent_locs = set()
    for loc_name, data in LOCATION_TABLE.items():
        if loc_name == VICTORY_LOCATION or loc_name in LOCKED_EVENTS:
            continue
        item_name = _location_item_name(loc_name)
        if item_name is None or item_name in dlc_only:
            continue
        req_src = LOCATION_RULE_SRC.get(loc_name)
        if not req_src:
            continue
        for dlc_item in dlc_only:
            if repr(dlc_item) in req_src:
                dependent_locs.add(loc_name)
                break
    return dependent_locs

def dlc_dependent_item_names():
    return {_location_item_name(loc_name) for loc_name in dlc_dependent_location_names()}

def create_regions(world, player):
    multiworld = world.multiworld

    dlc_option = getattr(world.options, "dlc_enabled", None)
    dlc_on = dlc_option.value if dlc_option is not None else True

    menu = Region("Menu", player, multiworld)
    multiworld.regions.append(menu)

    region_objs = {"Menu": menu}
    for name in REGION_CONNECTIONS:
        if not dlc_on and name in DLC_REGIONS:
            continue
        r = Region(name, player, multiworld)
        region_objs[name] = r
        multiworld.regions.append(r)

    for name in STARTING_REGIONS:
        if name in region_objs:
            menu.connect(region_objs[name])

    for name, connects in REGION_CONNECTIONS.items():
        if name not in region_objs:
            continue
        for dest in connects:
            if dest not in region_objs:
                continue
            rule = compile_rule(REGION_RULE_SRC.get(dest))
            entrance = region_objs[name].connect(region_objs[dest])
            if rule:
                entrance.access_rule = lambda state, player=player, rule=rule: rule(state, player)

    dlc_dependent_locs = dlc_dependent_location_names() if not dlc_on else set()

    for loc_name, data in LOCATION_TABLE.items():
        if loc_name == VICTORY_LOCATION or loc_name in LOCKED_EVENTS:
            continue
        if data.region not in region_objs:
            continue
                                                                    
                                                                    
                                                                      
                                                                 
                                                                       
                                                                        
                                                                     
                                                                     
                             
        if loc_name in dlc_dependent_locs:
            continue
        region = region_objs[data.region]
        region.add_locations({loc_name: data.code}, BS2Location)
        rule = compile_rule(LOCATION_RULE_SRC.get(loc_name))
        if rule:
            location = multiworld.get_location(loc_name, player)
            location.access_rule = lambda state, player=player, rule=rule: rule(state, player)

    if VICTORY_LOCATION:
        victory_data = LOCATION_TABLE[VICTORY_LOCATION]
        victory_region = region_objs[victory_data.region]
        victory_loc = BS2Location(player, VICTORY_LOCATION, None, victory_region)
        victory_region.locations.append(victory_loc)
        rule = compile_rule(LOCATION_RULE_SRC.get(VICTORY_LOCATION))
        if rule:
            victory_loc.access_rule = lambda state, player=player, rule=rule: rule(state, player)
        from BaseClasses import Item, ItemClassification
        victory_item = Item("Victory", ItemClassification.progression, None, player)
        victory_loc.place_locked_item(victory_item)
        multiworld.completion_condition[player] = lambda state, player=player: state.has("Victory", player)

    for event_loc_name, (event_item_name, event_classification) in LOCKED_EVENTS.items():
        event_data = LOCATION_TABLE.get(event_loc_name)
        if event_data is None or event_data.region not in region_objs:
            continue
        event_region = region_objs[event_data.region]
        event_loc = BS2Location(player, event_loc_name, event_data.code, event_region)
        event_region.locations.append(event_loc)
        rule = compile_rule(LOCATION_RULE_SRC.get(event_loc_name))
        if rule:
            event_loc.access_rule = lambda state, player=player, rule=rule: rule(state, player)
        from BaseClasses import Item, ItemClassification
        event_cls = getattr(ItemClassification, event_classification)
        event_item = Item(event_item_name, event_cls, LOCKED_EVENT_ITEM_IDS[event_item_name], player)
        event_loc.place_locked_item(event_item)
