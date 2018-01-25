import fischertechnik.factories as txtFactory
txtController = txtFactory.controller_factory.create_graphical_controller()
I2 = txtFactory.input_factory.create_push_button(txtController, 2)
I3 = txtFactory.input_factory.create_push_button(txtController, 3)
I1 = txtFactory.input_factory.create_light_sensor(txtController, 1)
O5 = txtFactory.output_factory.create_lamp(txtController, 5)
O7 = txtFactory.output_factory.create_lamp(txtController, 7)
O3 = txtFactory.output_factory.create_lamp(txtController, 3)
M1 = txtFactory.output_factory.create_encoder_motor(txtController, 1)
