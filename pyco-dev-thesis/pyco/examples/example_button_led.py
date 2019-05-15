'''
example_eps.py

In this file there is a collection of tests related to the Electrical Power System (EPS)
problem.
Add reference

Authors: Jack He and Eric Jan
'''


from pyco.contract import Contract, BaseTypeBool as BaseType
from pyco.library import (ContractLibrary, LibraryComponent,
                          LibraryPortMapping, LibraryCompositionMapping)
from pyco.synthesis import SynthesisInterface
from pyco import LOG

#let's start with types
class ToggleT(BaseType):
    '''
    anything that can be toggled
    '''
    pass

class IncompatibleOutputT(BaseType):
    '''
    bad part type
    '''
    pass

class IncompatibleInputT(BaseType):
    '''
    bad part type
    '''
    pass


class ActuatorT(BaseType):
    '''
    an actuator
    '''
    pass

class PhysicalOutputT(BaseType):
    '''
    a physical result
    '''
    pass


# COMPONENTS
class BasicButton(Contract):
    '''
    basic button that outputs 'on' on the next step
    after receiving 'press input'
    '''
    INPUT_PORTS = [('press', ToggleT)]
    OUTPUT_PORTS = [('on', ActuatorT)]
    ASSUMPTIONS = 'true'
    GUARANTEES = 'G(press -> X on)'

class BadButton(Contract):
    '''
    basic button that never turns on
    '''
    INPUT_PORTS = [('press', ToggleT)]
    OUTPUT_PORTS = [('on', ActuatorT)]
    ASSUMPTIONS = 'true'
    GUARANTEES = 'G(!on)'

class IncompatibleOutputButton(Contract):
    '''
    basic button that outputs 'on' on the next step
    after receiving 'press input'
    '''
    INPUT_PORTS = [('press', ToggleT)]
    OUTPUT_PORTS = [('on', IncompatibleOutputT)]
    ASSUMPTIONS = 'true'
    GUARANTEES = 'G(press -> X on)'

class IncompatibleInputButton(Contract):
    '''
    basic button that outputs 'on' on the next step
    after receiving 'press input'
    '''
    INPUT_PORTS = [('press', IncompatibleInputT)]
    OUTPUT_PORTS = [('on', ActuatorT)]
    ASSUMPTIONS = 'true'
    GUARANTEES = 'G(press -> X on)'

class Delayed2Button(Contract):
    '''
    basic button that outputs 'on' 5 steps later
    after receiving 'press input'
    '''
    INPUT_PORTS = [('press', ToggleT)]
    OUTPUT_PORTS = [('on', ActuatorT)]
    ASSUMPTIONS = 'true'
    GUARANTEES = 'G(press -> X2 on)'

class Delayed3Button(Contract):
    '''
    basic button that outputs 'on' 5 steps later
    after receiving 'press input'
    '''
    INPUT_PORTS = [('press', ToggleT)]
    OUTPUT_PORTS = [('on', ActuatorT)]
    ASSUMPTIONS = 'true'
    GUARANTEES = 'G(press -> X3 one)'

class Delayed4Button(Contract):
    '''
    basic button that outputs 'on' 5 steps later
    after receiving 'press input'
    '''
    INPUT_PORTS = [('press', ToggleT)]
    OUTPUT_PORTS = [('on', ActuatorT)]
    ASSUMPTIONS = 'true'
    GUARANTEES = 'G(press -> X4 on)'

class Delayed8Button(Contract):
    '''
    basic button that outputs 'on' 5 steps later
    after receiving 'press input'
    '''
    INPUT_PORTS = [('press', ToggleT)]
    OUTPUT_PORTS = [('on', ActuatorT)]
    ASSUMPTIONS = 'true'
    GUARANTEES = 'G(press -> ((X5 on) & !(on) & !(X on) & !(X2 on) & !(X3 on) & !(X4 on)))'

class EventuallyButton(Contract):
    '''
    basic button that outputs 'on' eventually
    after receiving 'press input'
    '''
    INPUT_PORTS = [('press', ToggleT)]
    OUTPUT_PORTS = [('on', ActuatorT)]
    ASSUMPTIONS = 'true'
    GUARANTEES = 'G(press -> F on)'

class BasicLED(Contract):
    '''
    LED that lights up 4 cycles after toggled on
    '''
    INPUT_PORTS = [('on', ActuatorT)]
    OUTPUT_PORTS = [('light', PhysicalOutputT)]
    ASSUMPTIONS = 'true'
    #GUARANTEES = 'G(on -> (X !light & X2 !light & X3 !light & X4 light))'
    GUARANTEES = 'G(on -> X light)'

class BadLED(Contract):
    '''
    LED that lights up 4 cycles after toggled on
    '''
    INPUT_PORTS = [('on', ActuatorT)]
    OUTPUT_PORTS = [('light', PhysicalOutputT)]
    ASSUMPTIONS = 'true'
    GUARANTEES = 'G(!light)'

class Delayed2LED(Contract):
    '''
    LED that lights up eventually after toggled on
    '''
    INPUT_PORTS = [('on', ActuatorT)]
    OUTPUT_PORTS = [('light', PhysicalOutputT)]
    ASSUMPTIONS = 'true'
    GUARANTEES = 'G(on -> X2 light)'

class Delayed3LED(Contract):
    '''
    LED that lights up eventually after toggled on
    '''
    INPUT_PORTS = [('on', ActuatorT)]
    OUTPUT_PORTS = [('light', PhysicalOutputT)]
    ASSUMPTIONS = 'true'
    GUARANTEES = 'G(on -> X3 light)'

class Delayed4LED(Contract):
    '''
    LED that lights up eventually after toggled on
    '''
    INPUT_PORTS = [('on', ActuatorT)]
    OUTPUT_PORTS = [('light', PhysicalOutputT)]
    ASSUMPTIONS = 'true'
    GUARANTEES = 'G(on -> X4 light)'

class Delayed5LED(Contract):
    '''
    LED that lights up eventually after toggled on
    '''
    INPUT_PORTS = [('on', ActuatorT)]
    OUTPUT_PORTS = [('light', PhysicalOutputT)]
    ASSUMPTIONS = 'true'
    GUARANTEES = 'G(on -> X5 light)'

class Delayed10LED(Contract):
    '''
    LED that lights up eventually after toggled on
    '''
    INPUT_PORTS = [('on', ActuatorT)]
    OUTPUT_PORTS = [('light', PhysicalOutputT)]
    ASSUMPTIONS = 'true'
    GUARANTEES = 'G(on -> X10 light)'

class DelayedLED(Contract):
    '''
    LED that lights up eventually after toggled on
    '''
    INPUT_PORTS = [('on', ActuatorT)]
    OUTPUT_PORTS = [('light', PhysicalOutputT)]
    ASSUMPTIONS = 'true'
    GUARANTEES = 'G(on -> F light)'

class IncompatibleOutputLED(Contract):
    '''
    LED with incompatible output
    '''
    INPUT_PORTS = [('on', ActuatorT)]
    OUTPUT_PORTS = [('light', IncompatibleOutputT)]
    ASSUMPTIONS = 'true'
    GUARANTEES = 'G(on -> X light)'

class IncompatibleInputLED(Contract):
    '''
    LED with incompatible input
    '''
    INPUT_PORTS = [('on', IncompatibleInputT)]
    OUTPUT_PORTS = [('light', PhysicalOutputT)]
    ASSUMPTIONS = 'true'
    GUARANTEES = 'G(on -> X light)'


# SPECIFICATIONS
class LightUpPlease(Contract):
    '''
    '''
    INPUT_PORTS = [('press', ToggleT)]
    OUTPUT_PORTS = [('light', PhysicalOutputT)]
    ASSUMPTIONS = 'true'
    GUARANTEES = 'G(press -> F light)'

class LightUpPleaseAfter7(Contract):
    '''
    '''
    INPUT_PORTS = [('press', ToggleT)]
    OUTPUT_PORTS = [('light', PhysicalOutputT)]
    # ASSUMPTIONS = 'G(press | !press) & ! (press) & ! (X press)'
    # ASSUMPTIONS = 'G(press | !press) & ! (press) & ! (X1 press) & ! (X2 press) & ! (X3 press) & ! (X4 press) & ! (X4 press)'
    ASSUMPTIONS = 'true'

    # GUARANTEES = 'G(press -> F light) & ! light & ! (X10 light) & ! (X11 light) & ! (X13 light) & ! (X14 light) & ! (X15 light) & ! (X16 light) & ! (X17 light) & ! (X18 light) & ! (X19 light)'
    GUARANTEES = 'G(press -> F light)'