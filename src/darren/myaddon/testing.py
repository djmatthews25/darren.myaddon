# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import darren.myaddon


class DarrenMyaddonLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=darren.myaddon)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'darren.myaddon:default')


DARREN_MYADDON_FIXTURE = DarrenMyaddonLayer()


DARREN_MYADDON_INTEGRATION_TESTING = IntegrationTesting(
    bases=(DARREN_MYADDON_FIXTURE,),
    name='DarrenMyaddonLayer:IntegrationTesting',
)


DARREN_MYADDON_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(DARREN_MYADDON_FIXTURE,),
    name='DarrenMyaddonLayer:FunctionalTesting',
)


DARREN_MYADDON_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        DARREN_MYADDON_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='DarrenMyaddonLayer:AcceptanceTesting',
)
