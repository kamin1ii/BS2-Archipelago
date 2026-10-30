"""
Generated from options.json.
"""
from dataclasses import dataclass
from Options import Toggle, DefaultOnToggle, Range, Choice, DeathLink, PerGameCommonOptions


class FillerTrapPercent(Range):
    """How many fillers will be replaced with traps. 0 means no additional
    traps, 100 means all fillers are traps. (options.json recommends 20.)"""
    display_name = "Filler Trap Percent"
    range_start = 0
    range_end = 100
    default = 0


class DLCEnabled(DefaultOnToggle):
    """Is the DLC enabled?."""
    display_name = "DLC Enabled"


class MistRandomization(DefaultOnToggle):
    """Turned on by default. Makes it so crossing a mist into a boss area requires a corresponding Mist item."""
    display_name = "Mist Randomization"


class CovenantGating(DefaultOnToggle):
    """Turned on by default. Makes it so speaking to a covenant NPC requires a corresponding Covenant Item."""
    display_name = "Covenant Gating"


class GearOfMadnessStart(Toggle):
    """Off By default. If enabled, Player starts with Gear of Madness."""
    display_name = "Gear of Madness Start"


class StartWithRunLikeDodo(Toggle):
    """Off by default. If enabled, player starts with Run Like Dodo."""
    display_name = "Start with Run Like Dodo"


class AutoMeetRedHood(DefaultOnToggle):
    """On by default. Sets the First meeting with Red Hood as true no matter what."""
    display_name = "Auto-Meet Red Hood"


class PreventCovenantPurge(DefaultOnToggle):
    """On by default. When turned on, prevents Jubjub from enacting her reign of suffering at progression 10."""
    display_name = "Prevent Covenant Purge"


class ForceCovenantNodeEarly(DefaultOnToggle):
    """On by default (disable if playing without Covenant Gating). If enabled, forces Node's unlock item to spawn early into the game."""
    display_name = "Force Covenant Node Early"


class RingLink(Toggle):
    """Off by default. If enabled, gold is shared with every other player in the
    multiworld who also has Ring Link on: gold you gain or spend is sent as
    rings, and rings from other games arrive as gold. Gains and spending both link."""
    display_name = "Ring Link"


class RingLinkGoldPerRing(Range):
    """How much gold one ring is worth, in both directions. Only used if Ring Link is on.
    At the default of 100, spending 300 gold sends -3 rings, and receiving 5 rings gives you 500 gold."""
    display_name = "Ring Link Gold Per Ring"
    range_start = 1
    range_end = 10000
    default = 100


class Goal(Choice):
    """Which ending would you like to set as goal?"""
    display_name = "Goal"
    option_true_ending = 0
    option_good_ending = 1
    option_common_endings = 2
    option_ending_f = 3
    default = 0


@dataclass
class BS2Options(PerGameCommonOptions):
    death_link: DeathLink
    filler_traps: FillerTrapPercent
    dlc_enabled: DLCEnabled
    mist_randomization: MistRandomization
    covenant_gating: CovenantGating
    gear_of_madness_start: GearOfMadnessStart
    start_with_run_like_dodo: StartWithRunLikeDodo
    auto_meet_red_hood: AutoMeetRedHood
    prevent_covenant_purge: PreventCovenantPurge
    force_covenant_node_early: ForceCovenantNodeEarly
    ring_link: RingLink
    ring_link_gold_per_ring: RingLinkGoldPerRing
    goal: Goal
