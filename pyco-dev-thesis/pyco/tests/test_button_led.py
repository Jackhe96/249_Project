'''
test_eps.py

In this file there is a collection of tests related to the Button LED
problem.
It uses files from pycox/examples/example_button_led
Add reference

Author: Jack He
'''


import pytest
from pyco.examples.example_button_led import *
from pyco.synthesis import NotSynthesizableError, OptimizationError

@pytest.fixture
def basic_button():
    '''
    basic button component
    '''
    comp = BasicButton("BaseBut")
    return LibraryComponent('BaseButC', comp)

@pytest.fixture
def bad_button():
    '''
    bad button component that never presses
    '''
    comp = BadButton("BadBut")
    return LibraryComponent('BadButC', comp)

@pytest.fixture
def delayed2_button():
    '''
    bad button component that never presses
    '''
    comp = BadButton("Delayed2But")
    return LibraryComponent('Delayed2ButC', comp)

@pytest.fixture
def delayed3_button():
    '''
    bad button component that never presses
    '''
    comp = BadButton("Delayed3But")
    return LibraryComponent('Delayed3ButC', comp)

@pytest.fixture
def delayed4_button():
    '''
    bad button component that never presses
    '''
    comp = BadButton("Delayed4But")
    return LibraryComponent('Delayed4ButC', comp)

@pytest.fixture
def delayed5_button():
    '''
    bad button component that never presses
    '''
    comp = BadButton("Delayed5But")
    return LibraryComponent('Delayed5ButC', comp)

@pytest.fixture
def incompatible_input_button():
    '''
    bad button component that has incompatible input
    '''
    comp = IncompatibleInputButton("IncompatibleInputBut")
    return LibraryComponent('IncompatibleInputButC', comp)

@pytest.fixture
def incompatible_output_button():
    '''
    bad button component that has incompatible input
    '''
    comp = IncompatibleOutputButton("IncompatibleOutputBut")
    return LibraryComponent('IncompatibleOutputButC', comp)

@pytest.fixture
def basic_led():
    '''
    basic led component
    '''
    comp = BasicLED('BaseLED')
    return LibraryComponent('BaseLEDC', comp)

@pytest.fixture
def bad_led():
    '''
    bad led component that never turns on
    '''
    comp = BadLED('BadLED')
    return LibraryComponent('BadLEDC', comp)

@pytest.fixture
def incompatible_input_led():
    '''
    led component with ncompatible ouput
    '''
    comp = IncompatibleInputLED('IncompatibleInputLED')
    return LibraryComponent('IncompatibleInputLEDC', comp)

@pytest.fixture
def incompatible_output_led():
    '''
    led component with incompatible ouput
    '''
    comp = IncompatibleOutputLED('IncompatibleOutputLED')
    return LibraryComponent('IncompatibleOutputLEDC', comp)

@pytest.fixture
def delayed_led():
    '''
    led component that lights up eventually
    '''
    comp = DelayedLED('DelayedLED')
    return LibraryComponent('DelayedLEDC', comp)

@pytest.fixture
def delayed2_led():
    '''
    led component that lights up eventually
    '''
    comp = DelayedLED('Delayed2LED')
    return LibraryComponent('Delayed2LEDC', comp)

@pytest.fixture
def delayed3_led():
    '''
    led component that lights up eventually
    '''
    comp = DelayedLED('Delayed3LED')
    return LibraryComponent('Delayed3LEDC', comp)

@pytest.fixture
def delayed4_led():
    '''
    led component that lights up eventually
    '''
    comp = DelayedLED('Delayed4LED')
    return LibraryComponent('Delayed4LEDC', comp)

@pytest.fixture
def delayed5_led():
    '''
    led component that lights up eventually
    '''
    comp = DelayedLED('Delayed5LED')
    return LibraryComponent('Delayed5LEDC', comp)

@pytest.fixture
def delayed10_led():
    '''
    led component that lights up eventually
    '''
    comp = DelayedLED('Delayed10LED')
    return LibraryComponent('Delayed10LEDC', comp)

@pytest.fixture
def led_lib_delayed(basic_button, bad_button, incompatible_input_button, incompatible_output_button,
                    basic_led, bad_led, delayed_led, incompatible_input_led, incompatible_output_led):
    '''
    returns a populated library with a button, a basic led and a delayed led
    '''
    library = ContractLibrary('lib')

    library.add(basic_button)
    library.add(bad_button)
    library.add(incompatible_input_button)
    library.add(incompatible_output_button)
    library.add(basic_led)
    library.add(bad_led)
    library.add(delayed_led)
    library.add(incompatible_input_led)
    library.add(incompatible_output_led)

    #add type compatibilities
    library.add_type(ToggleT)
    library.add_type(ActuatorT)
    library.add_type(PhysicalOutputT)
    library.add_type(IncompatibleInputT)
    library.add_type(IncompatibleOutputT)
    library.verify_library()

    return library

@pytest.fixture
def led_lib_delayed_after7(basic_button,delayed2_button,delayed3_button,delayed4_button,delayed5_button,
                    basic_led,delayed2_led,delayed3_led,delayed4_led,delayed5_led):
    '''
    returns a populated library with a button, a basic led and a delayed led
    '''
    library = ContractLibrary('lib')

    library.add(basic_button)
    library.add(delayed2_button)
    library.add(delayed3_button)
    library.add(delayed4_button)
    library.add(delayed5_button)


    library.add(basic_led)
    library.add(delayed2_led)
    library.add(delayed3_led)
    library.add(delayed4_led)
    library.add(delayed5_led)

    #add type compatibilities
    library.add_type(ToggleT)
    library.add_type(ActuatorT)
    library.add_type(PhysicalOutputT)
    library.verify_library()

    return library

@pytest.fixture
def led_lib_simple(basic_button, basic_led):
    '''
    returns a populated library with a button, a basic led and a delayed led
    '''
    library = ContractLibrary('lib')

    library.add(basic_button)
    library.add(basic_led)

    #add type compatibilities
    library.add_type(ToggleT)
    library.add_type(ActuatorT)
    library.add_type(PhysicalOutputT)
    library.verify_library()

    return library

def test_synth_5led_5b_1c(led_lib_delayed_after7, transform, orthogonalize):
    '''
    Performs simple synthesis
    '''
    library = led_lib_delayed_after7
    spec1 = LightUpPleaseAfter7('G1')

    interface = SynthesisInterface(library, [spec1])

    interface.same_block_constraint([spec1.press, spec1.light])
    interface.transform_eventually(transform,orthogonalize)
    interface.synthesize(filename="button_led_delayed_after7_test", visualize=True, decompose=False)

def test_synth_2led_1b_1c(led_lib_delayed, transform, orthogonalize):
    '''
    Performs simple synthesis
    '''
    library = led_lib_delayed
    spec1 = LightUpPlease('G1')

    interface = SynthesisInterface(library, [spec1])

    interface.same_block_constraint([spec1.press, spec1.light])
    interface.transform_eventually(transform,orthogonalize)
    interface.synthesize(filename="button_led_delayed_test", visualize=True, decompose=False)

def test_synth_1led_1b_1c(led_lib_simple, transform, orthogonalize):
    '''
    Performs simple synthesis
    '''
    library = led_lib_simple
    spec1 = LightUpPlease('G1')

    interface = SynthesisInterface(library, [spec1])

    interface.same_block_constraint([spec1.press, spec1.light])
    interface.transform_eventually(transform,orthogonalize)
    print "Synthesizing"
    interface.synthesize(filename="button_led_simple_test", visualize=True, decompose=False)

