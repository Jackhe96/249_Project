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


def basic_button():
    '''
    basic button component
    '''
    comp = BasicButton("BaseBut")
    return LibraryComponent('BaseButC', comp)

def basic_led():
    '''
    basic led component
    '''
    comp = BasicLED('BaseLED')
    return LibraryComponent('BaseLEDC', comp)

def delayed_led():
    '''
    led component that lights up eventually
    '''
    comp = DelayedLED('DelayLED')
    return LibraryComponent('DelayLEDC', comp)


def gen_lib():
    '''
    returns a populated library with a button, a basic led and a delayed led
    '''
    button = basic_button()
    b_led = basic_led()
    d_led = delayed_led()
    library = ContractLibrary('lib')

    library.add(button)
    library.add(b_led)
    #library.add(d_led)

    #add type compatibilities
    library.add_type(ToggleT)
    library.add_type(ActuatorT)
    library.add_type(PhysicalOutputT)
    library.verify_library()

    return library


def test_synth_2led_1b_1c():
    '''
    Performs simple synthesis
    '''
    library = gen_lib()
    spec1 = LightUpPlease('G1')

    interface = SynthesisInterface(library, [spec1])

    interface.same_block_constraint([spec1.press1, spec1.light1])
    interface.transform_eventually(5)
    res = None
    try:
        print "Synthesizing"
        interface.synthesize(filename="button_led_test", visualize=False, decompose=False)
    except NotSynthesizableError:
        res = False
    else:
        res = True
    return res

if __name__ == "__main__":
    res = test_synth_2led_1b_1c()
    if res:
        print "success"
    else:
        print "unsynthesizable"
