from typing import List
import datetime
import itertools
import random


class ConstantVariable:
    restrict_s4l_to_lower_wins = False
    max_s4l_single_win_to_rtp = 4
    s4l_number_of_match_limit = 2


def get_potential_winning(data: List[int], prices: dict, jackpot: float) -> List[int]:
    base_price = prices[data[1][0]]
    sharing = {5: 1, 4: 1, 3: 0.6, 2: 0.6 * 0.5}
    if data[0] == 5:
        winning = jackpot
    else:
        winning = (
            (base_price * sharing[data[0]]) if not sharing[data[0]] == 5 else jackpot
        )
    return [*data, int(winning)]


def search_number_occurences(
    numlist1: List[int], numlist2: List[int], number_of_match_limit: int = 3
) -> int:
    match_count = sum(1 for number in numlist1 if number in numlist2)
    return match_count if match_count > (number_of_match_limit - 1) else False


class SalaryForLifeDraw:
    @staticmethod
    def draw(plays, rtp, line_prices, jackpot_amount, disburse_jackpot=False) -> dict:
        random_combo = list(itertools.combinations(range(1, 50), 5))
        random.shuffle(random_combo)
        const_obj = ConstantVariable()
        max_win_lim_ratio = const_obj.max_s4l_single_win_to_rtp
        best_match = 0
        best_winners = 0
        best_match_combo = []
        restrict_or_not = const_obj.restrict_s4l_to_lower_wins
        best_match_with_jkpt = 0
        best_match_with_jkpt_combo = []
        best_match_witho_jkpt = 0
        best_match_witho_jkpt_combo = []
        for combo in random_combo:
            occurences = map(
                lambda user_play: search_number_occurences(
                    combo, user_play, const_obj.s4l_number_of_match_limit
                ),
                plays,
            )
            over3ocurrences = list(filter(None, occurences))
            play_occurences_with_amount = (
                get_potential_winning(played, line_prices, jackpot_amount)
                for played in zip(over3ocurrences, plays)
                if played[0]
            )
            total_sum = sum(ocurrence[-1] for ocurrence in play_occurences_with_amount)
            has_jkpt = any(
                ocurrence[0] == 5 for ocurrence in play_occurences_with_amount
            )
            match = total_sum / rtp * 100
            winners = len(over3ocurrences)
            if (winners >= best_winners or match > best_match) and match < 100:
                if winners == best_winners and match < best_match and restrict_or_not:
                    best_match = match
                    best_winners = winners
                    best_match_combo = combo
                elif winners > best_winners:
                    best_match = match
                    best_winners = winners
                    best_match_combo = combo
                elif best_winners == 0:
                    best_match = match
                    best_winners = winners
                    best_match_combo = combo
                if match > best_match and winners >= best_winners:
                    best_match = match
                    best_winners = winners
                    best_match_combo = combo
            if match > best_match_with_jkpt and match < 20 and has_jkpt:
                best_match_with_jkpt = match
                best_match_with_jkpt_combo = combo
            if match > best_match_witho_jkpt and match < 20 and (not has_jkpt):
                best_match_witho_jkpt = match
                best_match_witho_jkpt_combo = combo
        return dict(
            best_match=best_match,
            best_match_combo=best_match_combo,
            best_match_with_jkpt=best_match_with_jkpt,
            best_match_with_jkpt_combo=best_match_with_jkpt_combo,
            best_match_witho_jkpt=best_match_witho_jkpt,
            best_match_witho_jkpt_combo=best_match_witho_jkpt_combo,
        )

    @staticmethod
    def filter_winnings(combo, plays, prices, jackpot_amount):
        const_obj = ConstantVariable()
        occurences = map(
            lambda user_play: search_number_occurences(
                combo, user_play, const_obj.s4l_number_of_match_limit
            ),
            plays,
        )
        play_occurences = zip(occurences, plays)
        over3ocurrences = list(filter(None, play_occurences))
        play_occurences_with_amount = (
            get_potential_winning(played, prices, jackpot_amount)
            for played in over3ocurrences
            if played[0]
        )
        return list(play_occurences_with_amount)


prices = {
    1: 5000.00 / 1 * 0.2,
    2: 15000.00 / 2 * 0.2,
    3: 50000.00 / 3 * 0.2,
    4: 150000.00 / 4 * 0.2,
    5: 250000.00 / 5 * 0.2,
    6: 500000.00 / 6 * 0.2,
    7: 750000.00 / 7 * 0.2,
    8: 900000.00 / 8 * 0.2,
    9: 1250000.00 / 9 * 0.2,
}

plays = [[2, [3, 2, 1, 4, 5]], [2, [3, 2, 1, 4, 5]], [2, [3, 2, 1, 4, 5]]]


x = SalaryForLifeDraw.draw(plays, 20000, prices, 20000)
