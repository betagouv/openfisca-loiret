# -*- coding: utf-8 -*-
from __future__ import division

# Import from openfisca-core the common python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_france.entities import *


class loiret_apa(Variable):
    column = FloatCol
    entity = Famille
    definition_period = MONTH
    label = u"Montant de l'Allocation Personnalisée d'Autonomie pour le département du Loiret"

    def formula(famille, period, parameters):
        forfait = parameters(period).loiret.apa.forfait
        return 0 * famille.nb_persons(role = Famille.PARENT) * forfait


class loiret_test(Variable):
    column = FloatCol
    entity = Famille
    definition_period = MONTH
    label = u"Variable utilisée pour tester l'extension"

    def formula(famille, period, parameters):
        forfait = parameters(period).loiret.apa.forfait
        return famille.nb_persons(role = Famille.PARENT) * forfait
