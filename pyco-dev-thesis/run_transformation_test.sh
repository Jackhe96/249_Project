#!/bin/bash

#stop in case of errors
set -e
IS_CONCURRENT=false

AMP='&'
if ! $IS_CONCURRENT
then
  AMP=''
fi

START=5
REPS=5

# rm -f test_adc_int_*


# time eval "py.test --timeout=1000 -s pyco/tests/test_spi.py::test_adc4_int >> test_adc_int_4_1 2>&1" $AMP
# time eval "py.test --timeout=1000 -s pyco/tests/test_spi.py::test_adc4_int >> test_adc_int_4_2 2>&1" $AMP
# time eval "py.test --timeout=1000 -s pyco/tests/test_spi.py::test_adc4_int >> test_adc_int_4_3 2>&1" $AMP

# time eval "py.test --transform=3 --timeout=1000 -s pyco/tests/test_spi.py::test_adc4_int >> test_adc_int_4_4 2>&1" $AMP
# time eval "py.test --transform=3 --timeout=1000 -s pyco/tests/test_spi.py::test_adc4_int >> test_adc_int_4_5 2>&1" $AMP
# time eval "py.test --transform=3 --timeout=1000 -s pyco/tests/test_spi.py::test_adc4_int >> test_adc_int_4_6 2>&1" $AMP

# for (( i=$START; i<=$REPS; i++ ))
# do
#     time eval "py.test --lib2 --timeout=1000 -s pyco/tests/test_eps_facs.py::test_synth_6_10_dc_9spec >> test_synth_6_10_dc_9_lib20_${i} 2>&1"
# done

#rm -f test_synth_*

# for (( i=$START; i<=$REPS; i++ ))
# do
#     time eval "py.test --transform=${i} --orthogonalize --lib2 --timeout=1000 -s pyco/tests/test_eps_facs.py::test_synth_6_10_dc_9spec >> test_synth_6_10_dc_9_lib20_with_transform_${i} 2>&1" $AMP
# done

# time eval "parallel -j0 --verbose --halt now,success=1 'py.test --transform={} --orthogonalize --lib2 --timeout=1000 -s pyco/tests/test_button_led.py::test_synth_2led_1b_1c >> test_led_with_transform_{} 2>&1' ::: 1 2 3"

#eval "py.test --lib2 --timeout=1000 -s pyco/tests/test_button_led.py::test_synth_5led_5b_1c"
#eval "py.test --lib2 --timeout=1000 -s pyco/tests/test_eps_facs.py::test_synth_5led_5b_1c"
eval "py.test --lib2 --timeout=1000 -s pyco/tests/test_spi.py::test_adc2_int_OR"
