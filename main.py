from dataclasses import dataclass
from typing import Sequence

""""
This is a proof of concept framework for selecting job offers.

The general idea is to remove emotions from the decision
making process and first think about whats important to you, then
compare each offer against those things that are important to you.

Data below is for example purposes only and do not reflect my views about the companies


Python 3.7 Only!
"""


@dataclass
class Weights:
    """ How important is each category? (1-10 scale) """
    comp: int
    interesting_domain: int
    interesting_tools: int
    prestige: int
    location: int
    culture: int
    career_progression: int

    @property
    def as_list(self):
        return [i for i in  self.__dict__.values() if type(i) == int]

@dataclass
class JobOffer:
    """ Where does the job offer rank in each of the following categories (1-10 scale) """
    company: str

    comp: int
    interesting_domain: int
    interesting_tools: int
    prestige: int
    location: int
    culture: int
    career_progression: int

    def __str__(self):
        return self.company

    @property
    def as_list(self) -> list:
        return [i for i in  self.__dict__.values() if type(i) == int]

    def weighted_average(self, weights: Weights) -> int:
        """ Factor in the weights of each category """
        score = 0
        values = self.as_list
        weights = weights.as_list
        for x, y in zip(values, weights):
            score += x * y
        return score / sum(weights)


class DecisionMaker:
    def __init__(self, offers: Sequence[JobOffer], weights: Weights) -> None:
        self.category_weights = weights
        self.offers = offers

    def get_top_job(self) -> JobOffer:
        return next(iter(sorted(self.offers, key=lambda x: x.weighted_average(self.category_weights), reverse=True)))

    def main(self) -> str:
        return f'Take the job at {self.get_top_job()}'

if __name__ == '__main__':
    my_weights = Weights(
        comp=10,
        location=6,
        interesting_domain=9,
        interesting_tools=8,
        prestige=10,
        culture=8,
        career_progression=3
    )

    all_offers = [
        JobOffer(
            company='Uber',
            comp=10,
            interesting_domain=7,
            interesting_tools=10,
            prestige=10,
            location=7,
            culture=8,
            career_progression=10
        ),
        JobOffer(
            company='Yahoo',
            comp=8,
            interesting_domain=6,
            interesting_tools=6,
            prestige=5,
            location=10,
            culture=10,
            career_progression=10
        ),
        JobOffer(
            company='SpaceX',
            comp=10,
            interesting_domain=10,
            interesting_tools=4,
            prestige=8,
            location=8,
            culture=4,
            career_progression=9
        )

    ]
    print(DecisionMaker(all_offers, my_weights).main())
