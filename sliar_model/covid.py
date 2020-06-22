from .infection import Infection
from .statuses import infected, asymptomatic, latent

class Covid(Infection):
    transmission_rate = {
        latent: .2,
        infected: .7,
        asymptomatic: .3
    }
    mortality_rate = .01
    incubation_period_range = (24, 100)
    infection_period_range = (100, 200)
    asymptomatic_proportion = .2